<template>
    <div id="register" :style="bg">
        <card id="register" :bordered="false" style="position:absolute;left:35%;width:30%;top:25%">
            <p slot="title">注册到实验室</p>
            <i-form ref="check_form" :model="info" :rules="snum_rule" :hidden="!newcome">
              <form-item label="学号" prop="snum">
                <i-input size="large" v-model="info.snum" placeholder="输入学号"/>
              </form-item>
              <form-item >
                <i-button size="large" type="success" style="margin-left:10px;width:120px;" @click="check_snum">检测学号</i-button>
              </form-item>
            </i-form>
            <i-form ref="register_form" :model="info" :rules="rule" :hidden="newcome">
              <form-item label="用户名" prop="username">
                <i-input size="large" v-model="info.username" placeholder="输入用户名"/>
              </form-item>
              <form-item label="密码" prop="password">
                <i-input size="large" type="password"  v-model="info.password" placeholder="输入密码"/>
              </form-item>
              <form-item label="重复密码" prop="repassword">
                <i-input size="large" type="password"  v-model="info.repassword" placeholder="重复密码"/>
              </form-item>
              <form-item label="人脸录入" prop="face">
                <video height="120px" autoplay="autoplay"></video>
                <canvas id="canvas1" :hidden="true"  width="1000px" height="800px" ></canvas>
                <i-button type="primary" @click="draw_photo" :disabled="camera_close" v-text="button_text"></i-button>
              </form-item>
              <form-item >
                <i-button size="large" type="success" style="margin-left:10px;width:120px;" @click="register">注册</i-button>
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
  components: {
  },
  data(){
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
        bg:{
            backgroundImage: "url(" + require("../../public/img/bg.jpg") + ")",
            backgroundRepeat: "no-repeat",
            width:"100%",
            height:"100%",
            position:"absolute",
            backgroundSize: "100% 100%",
            verticalAlign: "middle",
      },
    info:{
        username:"",
        password:"",
        repassword:"",
        face:null,
        snum:"",
      },
      rule:{
        username: [
            { required: true, message: '用户名不能为空', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '密码不能为空', trigger: 'blur' },
          { type: 'string', min: 6, message: '密码长度必须大于6位', trigger: 'blur' }
        ],
        repassword:[
            { required: true, message: '重复密码不能为空', trigger: 'blur' },
            { validator: password_check, trigger: 'blur'}
        ],
        face:[
            {required:true,message:"请录入人脸"}
        ]
        
      },
      snum_rule:{
        snum:[
            { required: true, message: '学号不能为空', trigger: 'blur' },
        ]
      },
      video:null,
      exArray: [], //存储设备源ID  
      canvas:null,
      context:null,
      camera_close:true,
      button_text:"收集人脸",
      newcome:true, //新来的，默认为true表示未加入实验室
      closable_modal:false,
      alert_info:"",
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
                        'audio':false
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
        that.closable_modal = true;
        that.alert_info = "错误:"+e;
    },
    draw_photo(){
        let that = this;
        that.context.drawImage(that.video, 0, 0,1000,800);  
        let data = that.canvas.toDataURL( 'image/png', 1 );
        data = data.replace(/data:image\/(jpeg|png|gif|bmp);base64,/i,'')
        that.info.face = data;
        that.button_text="收集完成"
        that.button
    },
    register(){
        let that = this;
        this.$refs["register_form"].validate((valid)=>{
            if(valid){
                let data = {
                    username:that.info.username,
                    password:that.info.password,
                    snum:that.info.snum,
                    face:that.info.face,
                }
                this.$api.account.register(data).then((res)=>{
                    if(res.data.code === 1){
                        that.$router.push({name:'login'})
                    }else{
                        that.closable_modal = true;
                        that.alert_info = "注册失败,请重试"
                    }
                })
            }
        })
    },
    check_snum(){
        let that = this;
        this.$refs["check_form"].validate((valid)=>{
        if(valid){
          this.$api.account.check_snum(that.info).then((res)=>{
            if(res.data.code === 1){
                that.newcome = false;
            }else{
                alert("您未加入本实验室，禁止注册账号")
            }
          })
        }
      })
    }
  },
  mounted(){
    this.video = document.querySelector('video')
    this.canvas = document.getElementById('canvas1');  
    this.context= this.canvas.getContext('2d');  
    this.getMedia();
  },
}
</script>