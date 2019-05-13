<template>
    <div id="login" :style="bg">
        <card id="login" :hidden="login_hidden" :bordered="false" style="position:absolute;left:35%;width:30%;top:25%">
            <p slot="title">登录实验室</p>
            <i-form ref="login_form" :model="info" :rules="rule">
                <form-item label="用户名" prop="username">
                    <i-input size="large" v-model="info.username" placeholder="输入用户名"/>
                </form-item>
                <form-item label="密码" prop="password">
                    <i-input type="password" size="large" v-model="info.password" placeholder="输入密码"/>
                </form-item>
                <form-item>
                    <i-button size="large" type="primary" style="width:120px" @click="check_account">登录</i-button>
                    <i-button size="large" type="success" style="margin-left:10px;width:120px;" @click="jump">注册
                    </i-button>
                </form-item>
            </i-form>
        </card>
        <card id="photo" :hidden="photo_hidden" :bordered="false" style="position:absolute;left:35%;width:30%;top:25%">
            <p slot="title">人脸验证</p>
            <i-button type="primary" @click="getMedia">开启摄像头</i-button>
            <br>
            <video height="120px" width="120px" autoplay="autoplay"></video>
            <canvas id="canvas1" :hidden="true" width="1000px" height="800px"></canvas>
            <i-button type="primary" @click="draw_photo" :disabled="!button_enable" v-text="button_text"></i-button>
        </card>
        <modal
                title="提示"
                v-model="closable_modal"
        >
            <p v-text="alert_info"></p>
        </modal>
        <modal
                title="请稍候"
                v-model="loading_modal"
                :closable="false"
                :mask-closable="false"
                :loading="true"
        >
            <p>正在进行人脸检测...</p>
        </modal>
    </div>
</template>

<script>
    export default {
        name: 'login',
        components: {},
        data() {
            return {
                bg: {
                    backgroundImage: "url(" + require("../../public/img/bg.jpg") + ")",
                    backgroundRepeat: "no-repeat",
                    width: "100%",
                    height: "100%",
                    position: "absolute",
                    backgroundSize: "100% 100%",
                    verticalAlign: "middle",
                },
                info: {
                    username: "",
                    password: "",
                },
                rule: {
                    username: [
                        {required: true, message: '用户名不能为空', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不能为空', trigger: 'blur'},
                        {type: 'string', min: 6, message: '密码长度必须大于6位', trigger: 'blur'}
                    ]
                },
                login_hidden: false,
                photo_hidden: true,
                video: null,
                exArray: [], //存储设备源ID
                canvas: null,
                context: null,
                button_text: "人脸识别",
                button_enable: false,
                alert_info: "",
                closable_modal: false,
                loading_modal: false,
            }
        },
        methods: {
            check_account() {
                let that = this;
                //先判断用户名密码是否输入正确
                this.$refs["login_form"].validate((valid) => {
                    if (valid) {
                        this.$api.account.check_account(this.info).then((res) => {
                            if (res.data.code === 1) {
                                //正确之后进行人脸检测
                                that.goto_photo();
                            } else {
                                that.alert_info = "用户名或密码错误";
                                that.closable_modal = true;
                                that.loading_modal = false;
                            }
                        })
                    }
                })
            },
            goto_photo() {
                this.login_hidden = true;
                this.photo_hidden = false;
            },
            goto_login() {
                this.login_hidden = false;
                this.photo_hidden = true;
            },

            getMedia() {
                let that = this;

                navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
                window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL;

                navigator.mediaDevices.enumerateDevices().then((sourceInfos) => {
                    for (var i = 0; i != sourceInfos.length; ++i) {
                        var sourceInfo = sourceInfos[i];
                        //这里会遍历audio,video，所以要加以区分
                        if (sourceInfo.kind === 'video') {
                            that.exArray.push(sourceInfo.id);
                        }
                    }
                })

                if (navigator.getUserMedia) {
                    navigator.getUserMedia({
                        'video': {
                            'optional': [{
                                'sourceId': that.exArray[0] //0为前置摄像头，1为后置
                            }]
                        },
                        'audio': false
                    }, that.successFunc, that.errorFunc);    //success是获取成功的回调函数
                } else {
                    alert('Native device media streaming (getUserMedia) not supported in this browser.');
                }
            },
            successFunc(stream) {
                if (this.video.mozSrcObject !== undefined) {
                    //Firefox中，video.mozSrcObject最初为null，而不是未定义的，我们可以靠这个来检测Firefox的支持
                    this.video.mozSrcObject = stream;
                } else {
                    // this.video.src = window.URL && window.URL.createObjectURL(stream) || stream;
                    this.video.srcObject = stream;
                }
                this.video.play();
                this.button_enable = true
            },
            errorFunc(e) {
                alert('Error！' + e);
            },
            draw_photo() {
                var that = this;
                that.button_text = "正在检测";
                that.button_enable = false;
                setTimeout(() => {
                    that.button_enable = true;
                    that.button_text = "请重新识别";
                }, 5000);
                that.context.drawImage(that.video, 0, 0, 1000, 800);
                var data = that.canvas.toDataURL('image/png', 1);
                data = data.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i, '')
                let pack = {
                    username: that.info.username,
                    face: data,
                };
                this.$api.face.check(pack).then((res) => {
                    if (res.data.code === 1) {
                        if (res.data.data > 80) {
                            that.$api.account.login(that.info).then((res) => {
                                if (res.data.code === 1) {
                                    // 保存token
                                    import('js-cookie').then(Cookies => {
                                        Cookies.set('token', res.data.data.token)
                                        that.$store.commit('save', res.data.data);
                                        that.$store.commit('update_token', res.data.data.token)
                                        that.loading_modal = false;
                                        that.$router.push({name: "mainpage"})
                                    });

                                }
                            })
                        }
                    }
                })

                if (navigator.getUserMedia) {
                    navigator.getUserMedia({
                        'video': {
                            'optional': [{
                                'sourceId': that.exArray[0] //0为前置摄像头，1为后置
                            }]
                        },
                        'audio': false
                    }, that.successFunc, that.errorFunc);    //success是获取成功的回调函数
                } else {
                    alert('Native device media streaming (getUserMedia) not supported in this browser.');
                }
            },
            successFunc(stream) {
                if (this.video.mozSrcObject !== undefined) {
                    //Firefox中，video.mozSrcObject最初为null，而不是未定义的，我们可以靠这个来检测Firefox的支持
                    this.video.mozSrcObject = stream;
                } else {
                    // this.video.src = window.URL && window.URL.createObjectURL(stream) || stream;
                    this.video.srcObject = stream;
                }
                this.video.play();
                this.button_enable = true
            },
            errorFunc(e) {
                alert('Error！' + e);
            },
            draw_photo() {
                var that = this;
                that.button_text = "正在检测";
                that.button_enable = false;
                setTimeout(() => {
                    that.button_enable = true;
                }, 5000)
                that.context.drawImage(that.video, 0, 0, 160, 120);
                var data = that.canvas.toDataURL('image/png', 1);
                data = data.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i, '')
                let pack = {
                    username: that.info.username,
                    face: data,
                }
                this.$api.face.check(pack).then((res) => {
                    if (res.data.code === 1) {
                        if (res.data.data > 80) {
                            that.$api.account.login(that.info).then((res) => {
                                if (res.data.code === 1) {
                                    // 保存token
                                    import('js-cookie').then(Cookies => {
                                        Cookies.set('token', res.data.data.token);
                                        Cookies.set('group', res.data.data.group);
                                        that.$store.commit('save', res.data.data);
                                        that.$store.commit('update_token', res.data.data.token);
                                        that.loading_modal = false;
                                        that.$router.push({name: "default"})
                                    });

                                }
                            })
                        } else {
                            that.alert_info = "人脸相似度过低，请重新校验"
                            that.closable_modal = true;
                            that.loading_modal = false;
                            that.button_enable = true;
                        }

                    } else {
                        that.alert_info = "人脸校验失败"
                        that.closable_modal = true;
                        that.loading_modal = false;
                        that.button_enable = true;
                    }
                })

            },
            jump() {
                this.$router.push({name: 'register'})
            }
        },
        mounted() {
            this.video = document.querySelector('video')
            this.canvas = document.getElementById('canvas1');
            this.context = this.canvas.getContext('2d');
        },
    }
</script>
