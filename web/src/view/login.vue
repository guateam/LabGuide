<template>
    <div id="login" class="bg">
        <card :bordered="false" :class="{login:photo_hidden,loginCamera:!photo_hidden}">
            <p slot="title" v-text="photo_hidden?'登录实验室':'人脸验证'"></p>
            <i-form ref="login_form" :model="info" :rules="rule" :hidden="!photo_hidden"  @submit.native.prevent>
                <form-item :label="'用户名或学号'" prop="username">
                    <i-input size="large" v-model="info.username" :placeholder="'输入用户名或学号'"/>
                </form-item>
                <form-item label="密码" prop="password">
                    <i-input type="password" size="large" v-model="info.password" placeholder="输入密码"/>
                </form-item>
                <form-item style="text-align:center">
                    <i-button size="large" type="primary" style="width: 40%;margin-top: 1%" @click="check_account">登录
                    </i-button>
                    <i-button size="large" type="success" style="width: 40%;margin-top: 1%;margin-left:1%;"
                              @click="jump">注册
                    </i-button>
                </form-item>
            </i-form>
            <i-form :hidden="photo_hidden" @submit.native.prevent>
                <FormItem>
                    <video height="auto" width="100%" autoplay="autoplay"
                           style="max-width: 100%;max-height: 50vh"></video>
                    <canvas id="canvas1" :hidden="true" style="width: 100%"></canvas>
                </FormItem>
                <FormItem>
                    <i-button type="primary" @click="draw_photo" :disabled="!button_enable"
                              v-text="'手动拍照'" size="large">
                    </i-button>
                    <i-button type="primary" @click="getMedia" v-if="!open_camera" style="margin-left: 1%" size="large">
                        开启摄像头
                    </i-button>
                    <i-button type="success" @click="change_camera" v-if="exArray.length>1" style="margin-left: 1%"
                              size="large">
                        切换摄像头
                    </i-button>
                    <p v-text="alert_info"></p>
                </FormItem>
<<<<<<< HEAD
                <form-item style="text-align:center">
                    <i-button size="large" type="primary" style="width: 40%;margin-top: 1%" @click="check_account">登录
                    </i-button>
                    <i-button size="large" type="success" ghost style="width: 45%;margin-top: 1%;margin-left:8%;"
                              @click="jump">注册
                    </i-button>
                </form-item>
            </i-form>
            <!--<i-form :hidden="photo_hidden" @submit.native.prevent>
                <FormItem>
                    <i-button type="primary" @click="draw_photo" :disabled="!button_enable"
                              v-text="button_text" size="large"></i-button>
                    <i-button type="primary" ghost @click="getMedia" v-if="open_camera" style="margin-left: 1%" size="large">
                        开启摄像头
                    </i-button>
                    <i-button type="success" ghost @click="change_camera" v-if="exArray.length>1" style="margin-left: 1%"
                              size="large">
                        切换摄像头
                    </i-button>
                </FormItem>
            </i-form>-->
=======
            </i-form>
>>>>>>> master
        </card>
        <modal
                title="提示"
                v-model="closable_modal"
        >
            <p v-text="alert_info"></p>
        </modal>

    </div>
</template>

<script>

    export default {
        name: 'login',
        data() {
            return {
                open_camera: false,
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
                    ],
                },
                video: null,
                exArray: [], //存储设备源ID
                canvas: null,
                context: null,
                button_text: "人脸识别",
                button_enable: false,
                alert_info: "开启摄像头后自动检测",
                closable_modal: false,
                exnum: 0,
                interval_id:"",
                photo_num:0,//拍照的次数
                photo_hidden:true,
            }
        },
        methods: {
            check_account() {
                let that = this;
                //先判断用户名密码是否输入正确
                this.$refs["login_form"].validate((valid) => {
                    if (valid) {
                        this.$api.account.check_account(that.info).then((res) => {
                            if (res.data.code === 1) {
                               that.photo_hidden = false;
                               that.getMedia();
                            } else {
                                that.alert_info = "用户名或密码错误";
                                that.closable_modal = true;
                            }
                        })
                    }
                })
            },
            change_camera() {
                if (this.exnum < this.exArray.length) {
                    this.exnum++;
                } else {
                    this.exnum = 0;
                }
                if (navigator.getUserMedia) {
                    navigator.getUserMedia({
                        'video': {
                            'optional': [{
                                'sourceId': that.exArray[this.exnum] //0为前置摄像头，1为后置
                            }]
                        },
                        'audio': false
                    }, that.successFunc, that.errorFunc);    //success是获取成功的回调函数

                } else {
                    alert('Native device media streaming (getUserMedia) not supported in this browser.');
                }

            },
            getMedia() {
                let that = this;
                //如果已经开启了摄像头就不再执行,或者当用户名未输入时，不执行
                if(that.open_camera || that.info.username === "")return;

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
                                'sourceId': that.exArray[this.exnum] //0为前置摄像头，1为后置
                            }]
                        },
                        'audio': false
                    }, that.successFunc, that.errorFunc);    //success是获取成功的回调函数

                } else {
                    alert('Native device media streaming (getUserMedia) not supported in this browser.');
                }
            },
            successFunc(stream) {
                let that = this;
                if (this.video.mozSrcObject !== undefined) {
                    //Firefox中，video.mozSrcObject最初为null，而不是未定义的，我们可以靠这个来检测Firefox的支持
                    this.video.mozSrcObject = stream;
                } else {
                    // this.video.src = window.URL && window.URL.createObjectURL(stream) || stream;
                    this.video.srcObject = stream;
                }
                if(that.interval_id == "")that.interval_id = setInterval(that.draw_photo,2500);
                this.open_camera = true;
                this.video.play();
            },
            errorFunc(e) {
                this.closable_modal = true;
                this.alert_info = "错误:" + e;
            },
            draw_photo() {
                var that = this;
                //如果用户名未输入，则不执行
                if(that.info.username === "")return;

                that.photo_num +=1;
                //手动检测开始后，对按钮的处理
                if(that.photo_num > 3){
                    that.button_enable = false;
                    setTimeout(() => {
                        that.button_enable = true;
                    }, 5000)
                }
                that.alert_info = "正在检测..."
                document.getElementById('canvas1').height = this.video.offsetHeight;
                that.context.drawImage(that.video, 0, 0, this.video.offsetWidth, this.video.offsetHeight);
                var data = that.canvas.toDataURL('image/png', 1);
                data = data.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i, '')
                let pack = {
                    username: that.info.username,
                    face: data,
                }

                this.$api.face.check(pack).then((res) => {
                    if (res.data.code === 1) {
                        if (res.data.data > 80) {
                            that.alert_info = "人脸认证通过"
                            that.stop_auto_check();
                            that.$api.account.login(this.info).then((res) => {
                                if (res.data.code === 1) {
                                    import('js-cookie').then(Cookies => {
                                            Cookies.set('token', res.data.data.token);
                                            Cookies.set('group', res.data.data.group);
                                            that.$store.commit('save', res.data.data);
                                            that.$store.commit('update_token', res.data.data.token);
                                            that.$router.push({name: "default"})
                                        });
                                } else {
                                    that.alert_info = "用户名或密码错误";
                                    that.closable_modal = true;
                                }
                            })
                        } else {
                            that.alert_info = "人脸相似度为" + parseInt(res.data.data)  +"%,过低，请重新校验";
                            that.button_enable = true;
                        }
                    } else if( res.data.code === 0 ) {
                        that.alert_info = "百度人脸验证提供的ACCESS TOKEN已过期，请通知管理员进行更新";
                        that.button_enable = true;
                    } else if(res.data.code === -1){
                        that.alert_info = "人脸识别服务器繁忙，请重试";
                        that.button_enable = true;
                    } else {
                        that.alert_info = "验证失败，请重试";
                        that.button_enable = true;
                        console.log(res.data.data)
                    }
                    //三次自动后若还未通过，则停止自动检测,启用手动检测
                    if(res.data.code !== 1 || (res.data.code === 1 && res.data.data <= 80)){
                        if(that.photo_num == 3){
                            that.stop_auto_check()
                            that.button_enable = true;
                            that.closable_modal = true;
                            that.alert_info = "自动检测失败次数过多，请手动检测"
                        }
                    }
                })

            },
            stop_auto_check(){
                clearInterval(this.interval_id)
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
<style scoped>
    @media screen and (min-width: 1000px) {
        .login {
            position: absolute;
            left: 35%;
            width: 30%;
            top: 25%;
            background-color: #0a1e3cde;
            box-shadow: 0 0 15px #4cc6fe54;
        }
        .form_title {
            text-align: center;
            color: white;
            font-size: initial;
            font-weight: 600;
            letter-spacing: 10px;
        }
        .loginCamera {
            position: absolute;
            left: 35%;
            width: 30%;
            top: 25%;
        }
    }

    @media screen and (max-width: 1000px) {
        .login {
            position: absolute;
            left: 25%;
            width: 50%;
            top: 30%;
            background-color: #0a1e3cde;
            box-shadow: 0 0 15px #4cc6fe54;
        }

        .loginCamera {
            position: absolute;
            left: 25%;
            width: 50%;
            top: 30%;
        }
    }

    @media screen and (max-width: 800px) {
        .login {
            position: absolute;
            left: 5%;
            width: 90%;
            top: 30%;
            background-color: #0a1e3cde;
            box-shadow: 0 0 15px #4cc6fe54;
        }

        .loginCamera {
            position: absolute;
            left: 5%;
            width: 90%;
            top: 5%;
            transition: top 0.5s;
            -moz-transition: top 0.5s; /* Firefox 4 */
            -webkit-transition: top 0.5s; /* Safari 和 Chrome */
            -o-transition: top 0.5s; /* Opera */
        }
    }
    .title{
        color: white;
        font-size: 30px;
        letter-spacing: 20px;
        text-align: center;
        margin: 3% auto;
        text-shadow:0 0 23px #4cc6fe9c;
    }

    .bg {
        background-image: url("../../public/img/bg2.jpg");
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -10;
        zoom: 1;
        background-color: #fff;
        background-repeat: no-repeat;
        background-size: cover;
        -webkit-background-size: cover;
        -o-background-size: cover;
        background-position: center 0;
        overflow: scroll;
    }
</style>
