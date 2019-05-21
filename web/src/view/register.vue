<template>
    <div class="bg">
        <card id="register" :bordered="false" :class="{login:true,top:!newcome}" style="margin-bottom: 10%">
            <p slot="title">注册到实验室</p>
            <i-form ref="check_form" :model="info" :rules="snum_rule" :hidden="!newcome" @submit.native.prevent>
                <form-item label="学号" prop="snum">
                    <i-input size="large" v-model="info.snum" placeholder="输入学号"/>
                </form-item>
                <form-item style="text-align:center">
                    <i-button size="large" type="success" style="width:40%;margin-top: 1%" @click="check_snum">
                        检测学号
                    </i-button>
                    <i-button size="large" style="margin-left:1%;width:40%;margin-top: 1%" @click="$router.back()">
                        取消
                    </i-button>
                </form-item>
            </i-form>
            <i-form ref="register_form" :model="info" :rules="rule" :hidden="newcome" @submit.native.prevent>
                <form-item label="用户名" prop="username">
                    <i-input size="large" v-model="info.username" placeholder="输入用户名"/>
                </form-item>
                <form-item label="密码" prop="password">
                    <i-input size="large" type="password" v-model="info.password" placeholder="输入密码"/>
                </form-item>
                <form-item label="重复密码" prop="repassword">
                    <i-input size="large" type="password" v-model="info.repassword" placeholder="重复密码"/>
                </form-item>
                <form-item label="人脸录入" prop="face">
                    <video width="100%" autoplay="autoplay" ></video>
                    <canvas id="canvas1" :hidden="true"></canvas>
                    <div v-if="exArray.length<=1">
                        <i-button type="primary" long @click="draw_photo" :disabled="camera_close"
                                  v-text="button_text"></i-button>
                    </div>
                    <div style="text-align:center" v-if="exArray.length>1">
                        <i-button type="primary" style="width: 45%;margin-top: 1%" @click="draw_photo"
                                  :disabled="camera_close"
                                  v-text="button_text"></i-button>
                        <i-button type="success" style="width: 45%;margin-top: 1%;margin-left:1%;"
                                  @click="change_camera" :disabled="camera_close"
                                  v-text="button_text"></i-button>
                    </div>
                </form-item>
                <form-item style="text-align:center">
                    <i-button size="large" type="success" long style="margin-left:10px;width:40%;margin-top: 1%"
                              @click="register">
                        注册
                    </i-button>
                    <i-button size="large" type="" long style="margin-left:1%;width:40%;margin-top: 1%"
                              @click="$router.back()">
                        取消
                    </i-button>
                </form-item>
            </i-form>
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
        name: 'register',
        components: {},
        data() {
            const password_check = (rule, value, callback) => {
                if (this.info.password != '' && value == '') {
                    callback(new Error('确认密码不能为空'));
                } else if (this.info.password != value) {
                    callback(new Error('新密码和确认密码应相同'));
                } else {
                    callback();
                }
            };
            return {
                info: {
                    username: "",
                    password: "",
                    repassword: "",
                    face: null,
                    snum: "",
                },
                rule: {
                    username: [
                        {required: true, message: '用户名不能为空', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不能为空', trigger: 'blur'},
                        {type: 'string', min: 6, message: '密码长度必须大于6位', trigger: 'blur'}
                    ],
                    repassword: [
                        {required: true, message: '重复密码不能为空', trigger: 'blur'},
                        {validator: password_check, trigger: 'blur'}
                    ],
                    face: [
                        {required: true, message: "请录入人脸"}
                    ]

                },
                snum_rule: {
                    snum: [
                        {required: true, message: '学号不能为空', trigger: 'blur'},
                    ]
                },
                video: null,
                exArray: [], //存储设备源ID
                canvas: null,
                context: null,
                camera_close: true,
                button_text: "收集人脸",
                newcome: true, //新来的，默认为true表示未加入实验室
                closable_modal: false,
                alert_info: "",
                exnum: 0
            }
        },
        methods: {
            change_camera() {
                if (this.exnum < this.exArray.length) {
                    this.exnum++;
                    this.getMedia();
                } else {
                    this.exnum = 0;
                    this.getMedia();
                }
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
                if (this.video.mozSrcObject !== undefined) {
                    //Firefox中，video.mozSrcObject最初为null，而不是未定义的，我们可以靠这个来检测Firefox的支持
                    this.video.mozSrcObject = stream;
                } else {
                    // this.video.src = window.URL && window.URL.createObjectURL(stream) || stream;
                    this.video.srcObject = stream;
                }
                this.video.play();
                this.camera_close = false

            },
            errorFunc(e) {
                this.closable_modal = true;
                this.alert_info = "错误:" + e;
            },
            draw_photo() {
                let that = this;
                document.getElementById('canvas1').height = this.video.offsetHeight;
                document.getElementById('canvas1').width = this.video.offsetWidth;
                that.context.drawImage(that.video, 0, 0, this.video.offsetWidth, this.video.offsetHeight);
                let data = that.canvas.toDataURL('image/png', 1);
                data = data.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i, '')
                that.button_text = "正在检测人脸"
                //暂时关闭人脸收集，直到获得检测结果
                that.camera_close = true;
                this.$api.face.exist({face: data,h:this.video.offsetHeight,w: this.video.offsetWidth}).then((res) => {
                    if (res.data.code === 1) {
                            that.info.face = data;
                            that.button_text = "收集完成"
                            that.camera_close = false;
                    } else {
                        if(res.data.code === 0){
                                that.closable_modal = true;
                                that.alert_info = "人脸位置太偏，请将人脸尽量处于正中间"
                        } else if (res.data.code === -1){
                                that.closable_modal = true;
                                that.alert_info = "人脸数量过多，最多只能出现一个人脸"
                        } else if (res.data.code === -2) {
                            if (res.data.data == 18 ){
                                that.closable_modal = true;
                                that.alert_info = "人脸识别服务器繁忙，请重试"
                            }
                            else if(res.data.data == 222202){
                                that.closable_modal = true;
                                that.alert_info = "未检测到人脸，请重新收集"
                            }
                        } else if (res.data.code === -3){
                            that.closable_modal = true;
                            that.alert_info = "未知错误，采集失败"
                        } else if(res.data.code === -4){
                            that.closable_modal = true;
                            that.alert_info = "人脸距离摄像头过近，导致人脸太大，请适当远离摄像头"
                        }
                        that.camera_close = false;
                        that.button_text = "收集人脸"
                    }
                })


            },
            register() {
                let that = this;
                this.$refs["register_form"].validate((valid) => {
                    if (valid) {
                        let data = {
                            username: that.info.username,
                            password: that.info.password,
                            snum: that.info.snum,
                            face: that.info.face,
                        }
                        this.$api.account.register(data).then((res) => {
                            if (res.data.code === 1) {
                                that.$router.push({name: 'login'})
                            } else if(res.data.code === -2) {
                                that.closable_modal = true;
                                that.alert_info = "用户名重复，请重试"
                            } else {
                                that.closable_modal = true;
                                that.alert_info = "注册失败,请重试"
                            }
                        })
                    }
                })
            },
            check_snum() {
                let that = this;
                this.$refs["check_form"].validate((valid) => {
                    if (valid) {
                        this.$api.account.check_snum(that.info).then((res) => {
                            if (res.data.code === 1) {
                                that.newcome = false;
                            } else if (res.data.code === 0) {
                                that.closable_modal = true;
                                that.alert_info = "该学号未加入本实验室，无法注册"
                            } else if (res.data.code === -1) {
                                that.closable_modal = true;
                                that.alert_info = "该学号已经被注册"
                            }
                        })
                    }
                })
            }
        },
        mounted() {
            this.video = document.querySelector('video')
            this.canvas = document.getElementById('canvas1');
            this.context = this.canvas.getContext('2d');
            this.getMedia();
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
        }

        .top {
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
        }

        .top {
            position: absolute;
            left: 35%;
            width: 30%;
            top: 25%;
        }
    }

    @media screen and (max-width: 800px) {
        .login {
            position: absolute;
            left: 5%;
            width: 90%;
            top: 30%;
        }

        .top {
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

    .bg {
        background-image: url("../../public/img/bg.jpg");
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
