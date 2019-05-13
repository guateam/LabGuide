<template>
    <div>
        <h3 v-text="article.title"></h3>
        <div v-html="article.content"></div>
    </div>
</template>
<script>
export default {
    name:"article",
    data(){
        return{
            article:null,
        }
    },
    methods:{
        baseUrl:"",
    },
    mounted(){
        let that = this;
        let id= this.$route.query.article_id;
        this.$api.article.get_article(id).then((res)=>{
            if(res.data.code === 1){
                that.article = res.data.data;
                that.baseUrl = process.env.BASE_URL;
            }else{
                that.$router.push({name:'login'});
            }
        })
    },
}
</script>