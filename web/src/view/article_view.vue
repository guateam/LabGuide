<template>
    <Card style="margin-top: 20px">
        <div slot="title"><h3 style="margin-bottom: 5px">{{content.title}}</h3> <span style="margin-top: 5px">更新日期：{{content.time}}</span>
        </div>
        <div slot="extra">
            <Button v-if="$Cookies.get('group')==0" type="warning" size="large"
                    @click="$router.push({name:'change_article',query:{id:$route.query.id}})">修改文章
            </Button>
            <Button v-if="$Cookies.get('group')==0" type="error" size="large" style="margin-left: 8px" @click="delete_article">清除文章</Button>
        </div>

        <div v-html="content.content"></div>
    </Card>
</template>
<script>
    export default {
        name: "article_view",
        data() {
            return {
                content: {
                    title: '加载中',
                    content: '<p>Loading...</p>'
                },
            }
        },
        watch:{
            "$route":"get_articles"
        },
        methods:{
            delete_article(){

            }
        },
        mounted() {
            let id = this.$route.query.id;
            this.$api.article.get_article(id).then((res) => {
                if (res.data.code === 1) {
                    this.content = res.data.data;
                } else {
                    this.$router.push({name: 'login'});
                }
            })
        },
    }
</script>
<style>
    span:hover[style="background-color: rgb(0, 0, 0);"] {
        background-color: white !important;
    }

    span[style="background-color: rgb(0, 0, 0);"] {
        color: black !important;
    }
</style>
