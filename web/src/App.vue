<template>
  <div id="app" :style="bg">
        <card :bordered="false" style="position:absolute;left:35%;width:30%;top:25%">
            <p slot="title">登录实验室</p>
            <i-form :model="info">
              <form-item label="用户名">
                <i-input size="large" v-model="info.username" placeholder="输入用户名"/>
              </form-item>
              <form-item label="密码">
                <i-input size="large"  v-model="info.password" placeholder="输入密码"/>
              </form-item>
              <form-item >
                <i-button size="large" type="primary" style="width:120px">登录</i-button>
                <i-button size="large" type="success" style="margin-left:10px;width:120px;" >注册</i-button>
              </form-item>
            </i-form>
        </card>
  </div>
</template>

<script>

export default {
  name: 'app',
  components: {
  },
  data(){
    return {
      bg:{
            backgroundImage: "url(" + require("../public/img/bg.jpg") + ")",
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
      },

    }
  }
}
</script>

