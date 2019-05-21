<template>
    <div id="login" class="bg">
        <div style="width:100%">
            <h1 class="title">实验室指导资料库</h1>
        </div>
        <card :bordered="false" :class="{login:!login_hidden,loginCamera:!photo_hidden}">
            <p slot="title" class="form_title">{{!login_hidden?'登录实验室':'人脸验证'}}</p>
            <i-form ref="login_form" :model="info" :rules="rule" :hidden="login_hidden" @submit.native.prevent>
                <form-item label="登录方式" prop="way">
                    <br>
                    <RadioGroup v-model="info.way">
                        <Radio label="用户名"></Radio>
                        <Radio label="学号" ></Radio>
                    </RadioGroup>
                </form-item>
                <form-item :label="info.way" prop="username">
                    <i-input size="large" v-model="info.username" :placeholder="'输入'+info.way"/>
                </form-item>
                <form-item label="密码" prop="password">
                    <i-input type="password" size="large" v-model="info.password" placeholder="输入密码"/>
                </form-item>
                <form-item style="text-align:center" >
                    <i-button size="large" type="primary" ghost style="width: 45%;margin-top: 1%" @click="check_account">登录
                    </i-button>
                    <i-button size="large" type="success" ghost style="width: 45%;margin-top: 1%;margin-left:8%;"
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
                    <i-button type="primary" ghost @click="draw_photo" :disabled="!button_enable"
                              v-text="button_text" size="large"></i-button>
                    <i-button type="primary" ghost @click="getMedia" v-if="open_camera" style="margin-left: 1%" size="large">
                        开启摄像头
                    </i-button>
                    <i-button type="success" ghost @click="change_camera" v-if="exArray.length>1" style="margin-left: 1%"
                              size="large">
                        切换摄像头
                    </i-button>
                </FormItem>
            </i-form>
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
    <card :bordered="false" :class="{login:!login_hidden,loginCamera:!photo_hidden}" class="card">
      <p slot="title" class="form_title">{{!login_hidden?'登录实验室':'人脸验证'}}</p>
      <i-form
        class="form"
        ref="login_form"
        :model="info"
        :rules="rule"
        :hidden="login_hidden"
        @submit.native.prevent
      >
        <form-item label="用户名" prop="username">
          <i-input size="large" v-model="info.username" placeholder="输入用户名"/>
        </form-item>
        <form-item label="密码" prop="password">
          <i-input type="password" size="large" v-model="info.password" placeholder="输入密码"/>
        </form-item>
        <form-item style="text-align:center">
          <i-button
            size="large"
            type="primary"
            ghost
            style="width: 45%;margin-top: 1%"
            @click="check_account"
          >登录</i-button>
          <i-button
            size="large"
            type="success"
            ghost
            style="width: 45%;margin-top: 1%;margin-left:8%;"
            @click="jump"
          >注册</i-button>
        </form-item>
      </i-form>
      <i-form :hidden="photo_hidden" @submit.native.prevent>
        <FormItem>
          <video
            height="auto"
            width="100%"
            autoplay="autoplay"
            style="max-width: 100%;max-height: 50vh"
          ></video>
          <canvas id="canvas1" :hidden="true" style="width: 100%"></canvas>
        </FormItem>
        <FormItem style="text-align:center">
          <i-button
            type="primary"
            ghost
            @click="draw_photo"
            :disabled="!button_enable"
            v-text="button_text"
            size="large"
          ></i-button>
          <i-button
            type="primary"
            ghost
            @click="getMedia"
            v-if="open_camera"
            style="margin-left: 1%"
            size="large"
          >开启摄像头</i-button>
          <i-button
            type="success"
            ghost
            @click="change_camera"
            v-if="exArray.length>1"
            style="margin-left: 1%"
            size="large"
          >切换摄像头</i-button>
        </FormItem>
      </i-form>
    </card>
    <modal title="提示" v-model="closable_modal">
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
        data() {
            return {
                open_camera: false,
                info: {
                    username: "",
                    password: "",
                    way:"用户名",
                },
                rule: {
                    username: [
                        {required: true, message: '用户名不能为空', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '密码不能为空', trigger: 'blur'},
                        {type: 'string', min: 6, message: '密码长度必须大于6位', trigger: 'blur'}
                    ],
                    way:[
                        {required: true, message: '登录方式不能为空', trigger: 'blur'},
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
                exnum: 0
            }
          });
        }
      });
    },
    goto_photo() {
      this.login_hidden = true;
      this.photo_hidden = false;
      this.getMedia();
    },
    goto_login() {
      this.login_hidden = false;
      this.photo_hidden = true;
    },
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

      navigator.getUserMedia =
        navigator.getUserMedia ||
        navigator.webkitGetUserMedia ||
        navigator.mozGetUserMedia ||
        navigator.msGetUserMedia;
      window.URL =
        window.URL || window.webkitURL || window.mozURL || window.msURL;

      navigator.mediaDevices.enumerateDevices().then(sourceInfos => {
        for (var i = 0; i != sourceInfos.length; ++i) {
          var sourceInfo = sourceInfos[i];
          //这里会遍历audio,video，所以要加以区分
          if (sourceInfo.kind === "video") {
            that.exArray.push(sourceInfo.id);
          }
        }
      });

      if (navigator.getUserMedia) {
        navigator.getUserMedia(
          {
            video: {
              optional: [
                {
                  sourceId: that.exArray[this.exnum] //0为前置摄像头，1为后置
                }
              ]
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
                this.closable_modal = true;
                this.alert_info = "错误:" + e;
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
                this.open_camera = true;
            },
            draw_photo() {
                var that = this;
                that.button_text = "正在检测";
                that.button_enable = false;
                setTimeout(() => {
                    that.button_enable = true;
                }, 5000)
                document.getElementById('canvas1').height = this.video.offsetHeight;
                that.context.drawImage(that.video, 0, 0, this.video.offsetWidth, this.video.offsetHeight);
                var data = that.canvas.toDataURL('image/png', 1);
                data = data.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i, '')
                let pack = {
                    username: that.info.username,
                    face: data,
                    way:that.info.way
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
                            that.alert_info = "人脸相似度为" + parseInt(res.data.data)  +"%,过低，请重新校验";
                            that.closable_modal = true;
                            that.loading_modal = false;
                            that.button_enable = true;
                        }
                    } else if( res.data.code === 0 ) {
                        that.alert_info = "百度人脸验证提供的ACCESS TOKEN已过期，请通知管理员进行更新";
                        that.closable_modal = true;
                        that.loading_modal = false;
                        that.button_enable = true;
                    } else if(res.data.code === -1){
                        that.alert_info = "人脸识别服务器繁忙，请重试";
                        that.closable_modal = true;
                        that.loading_modal = false;
                        that.button_enable = true;
                    } else {
                        that.alert_info = "验证失败，请重试";
                        that.closable_modal = true;
                        that.loading_modal = false;
                        that.button_enable = true;
                        console.log(res.data.data)
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
  },
  mounted() {
    this.video = document.querySelector("video");
    this.canvas = document.getElementById("canvas1");
    this.context = this.canvas.getContext("2d");
  }
};
</script>
<style scoped>
@media screen and (min-width: 1000px) {
    .title {
    color: white;
    font-size: 2em;
    letter-spacing: 20px;
    text-align: center;
    margin: 4% auto;
    text-shadow: 0 0 23px #4cc6fe9c;
  }
  .card {
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
  .title {
    color: white;
    font-size: 30px;
    letter-spacing: 10px;
    text-align: center;
    margin: 3% auto;
    text-shadow: 0 0 23px #4cc6fe9c;
  }
  .card {
    position: absolute;
    left: 25%;
    width: 50%;
    top: 30%;
    background-color: #0a1e3cde;
    box-shadow: 0 0 15px #4cc6fe54;
  }
  .form_title {
    text-align: center;
    color: white;
    font-size: initial;
    font-weight: 500;
    letter-spacing: 10px;
  }
  .loginCamera {
    position: absolute;
    left: 25%;
    width: 50%;
    top: 30%;
  }
}

@media screen and (max-width: 800px) {
  .title {
    color: white;
    font-size: 2em;
    width: 70%;
    letter-spacing: 5px;
    text-align: center;
    margin: 17% auto;
    text-shadow: 0 0 23px #4cc6fe9c;
  }
  .card {
    position: absolute;
    left: 5%;
    width: 90%;
    top: 30%;
    background-color: #0a1e3cde;
    box-shadow: 0 0 15px #4cc6fe54;
  }
  .form_title {
    text-align: center;
    color: white;
    font-size: initial;
    font-weight: 500;
    letter-spacing: 10px;
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

.form >>> .ivu-form-item-label{
    color: rgba(255, 255, 255, 0.836) !important;
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
