<template>
    <div id="register">
        <card id="login" :hidden="login_hidden" :bordered="false" style="position:absolute;left:35%;width:30%;top:25%">
            <p slot="title">注册到实验室</p>
            <i-form ref="login_form" :model="info" :rules="rule">
              <form-item label="用户名" prop="username">
                <i-input size="large" v-model="info.username" placeholder="输入用户名"/>
              </form-item>
              <form-item label="密码" prop="password">
                <i-input size="large"  v-model="info.password" placeholder="输入密码"/>
              </form-item>
              <form-item label="重复密码" prop="repassword">
                <i-input size="large"  v-model="info.password" placeholder="输入密码"/>
              </form-item>
              <form-item label="人脸录入" prop="face">
                <video height="120px" autoplay="autoplay"></video>
                <i-button type="primary" @click="draw_photo" :disabled="camera_close" v-text="button_text"></i-button>
              </form-item>
              <form-item >
                <i-button size="large" type="success" style="margin-left:10px;width:120px;" @click="">注册</i-button>
              </form-item>
            </i-form>
        </card>
    </div>
</template>
<script>

export default {
  name: 'register',
  components: {
  },
  data(){
    return {
      video:null,
      exArray: [], //存储设备源ID  
      canvas:null,
      context:null,
      camera_close:true,
      button_text:"收集人脸"
    }
  },
  methods:{
    getMedia(){
        let that = this;

        navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;  
        window.URL = window.URL || window.webkitURL || window.mozURL || window.msURL;  

        navigator.mediaDevices.enumerateDevices().then((sourceInfos)=>{
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
                        'audio':true  
                    }, that.successFunc, that.errorFunc);    //success是获取成功的回调函数  
                }  
                else {  
                    alert('Native device media streaming (getUserMedia) not supported in this browser.');  
        }  
    },
    successFunc(stream){
            if (this.video.mozSrcObject !== undefined) {  
                //Firefox中，video.mozSrcObject最初为null，而不是未定义的，我们可以靠这个来检测Firefox的支持  
                this.video.mozSrcObject = stream;  
            }  
            else {  
                // this.video.src = window.URL && window.URL.createObjectURL(stream) || stream;  
                this.video.srcObject =stream;  
            }  
            this.video.play();  
            this.camera_close = false
    },
    errorFunc(e){
        alert('Error！'+e);  
    },
    draw_photo(){
        var that = this;
        that.context.drawImage(that.video, 0, 0,160,120);  
        var data = that.canvas.toDataURL( 'image/png', 1 );

    },
  },
  mounted(){
    this.video = document.querySelector('video')
    this.canvas = document.getElementById('canvas1');  
    this.context= this.canvas.getContext('2d');  
    this.getMedia();
  },
}
</script>