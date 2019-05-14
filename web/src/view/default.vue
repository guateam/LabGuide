<template>
    <div style="text-align: center">
        <b style="font-size:40px;display:block">实验室基本技术栈</b>
        <b  style="font-size:30px;display:block">软件下载安装以及教程引导</b>
        <p  style="font-size:20px;margin-top:20px;margin-bottom:20px">
        左侧菜单栏选择查阅资料的标签，选中后就会出现符合标签的文章资料
        右上角按钮点击后展开选项，进行登出等操作
        </p>
        <div style="buttom:0px">
            <h4>感谢以下开源项目：</h4>
            <a style="font-size: 17px;margin-right:15px" href="https://github.com/vuejs/vue" target="_blank">Vue.js</a>
            <a style="font-size: 17px" href="https://github.com/iview/iview" target="_blank" >iview.js</a>
            <br>
            <img style="width:48px;height:48px;margin-right: 5px;margin-left:-8px" :src="png2">
            <img style="width:48px;height:48px" :src="png1">
            <br><br><br>
            <h6>制作：smhhyyz hanerx</h6>
        </div>
    </div>
</template>

<script>
    export default {
        name: "default",
        data(){
            return{
                png1:require("../../public/img/iview.png"),
                png2:require("../../public/img/vue.png"),
            }
        }
    }
</script>

<style scoped>

</style>
