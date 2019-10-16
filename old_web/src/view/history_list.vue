<template>
    <div style="margin-top: 2%">
        <Card>
            <p slot="title">文章历史修改列表</p>
            <CellGroup>
                <Cell :title="article.date" v-for="article in articles" :label="'修改人：'+article.username"
                      :to="{name:'history_article_view',query:{id:article.id}}"></Cell>
            </CellGroup>
            <h1 style="text-align: center" v-if="articles.length===0">该文章暂无历史记录</h1>
        </Card>
    </div>
</template>

<script>
    export default {
        name: "history_list",
        data() {
            return {
                articles: []
            }
        },
        methods: {
            get_history() {
                this.$api.article.get_history(this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.articles = res.data.data;
                    }
                })
            }
        },
        mounted() {
            this.get_history();
        }
    }
</script>

<style scoped>

</style>
