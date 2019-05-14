<template>
    <Card style="margin-top: 20px;text-align: center">

        <h1 slot="title">实验室基本技术栈</h1>
        <h2>软件下载安装以及教程引导</h2>

        <p style="font-size:20px;margin-top:20px;margin-bottom:20px">
            左侧菜单栏选择查阅资料的标签，选中后就会出现符合标签的文章资料
            右上角按钮点击后展开选项，进行登出等操作
        </p>
        <p>侧边栏中所有星号项（*）均为进阶内容，请酌情学习</p>
        <span class="black">其实后面都是要学的</span>
        <div style="buttom:0px">
            <h4>感谢以下开源项目：</h4>
            <a style="font-size: 17px;margin-right:15px" href="https://github.com/vuejs/vue" target="_blank">Vue.js</a>
            <a style="font-size: 17px" href="https://github.com/iview/iview" target="_blank">iview.js</a>
            <br>
            <img style="width:48px;height:48px;margin-right: 5px;margin-left:-8px" :src="png2">
            <img style="width:48px;height:48px" :src="png1">
            <br><br><br>
            <h6>制作：smhhyyz hanerx</h6>
        </div>
    </Card>
</template>

<script>
    export default {
        name: "default",
        data() {
            return {
                png1: "https://file.iviewui.com/dist/2ecd3b0452aa197097d5131afacab7b8.png",
                png2: require("../../public/img/vue.png"),
            }
        }
    }
</script>

<style scoped>
    .black:hover{
        background-color: white;
    }
    .black{
        color: black !important;
        background-color: black;
    }
</style>
