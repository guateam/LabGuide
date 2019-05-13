<template>
    <div style="margin-top: 20px">
        <Card>
            <p slot="title">标签文章列表</p>
            <CellGroup>
                <Cell :title="article.title" v-for="article in articles"
                      @click="$router.push({name:'article',query:{id:article.ID}})"></Cell>
            </CellGroup>
        </Card>
    </div>
</template>

<script>
    export default {
        name: "article_list",
        data() {
            return {
                articles: []
            }
        },
        methods: {
            get_articles() {
                this.$api.tag.get_articles(this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.articles = res.data.data;
                    }
                })
            }
        },
        mounted() {
            this.get_articles();
        }
    }
</script>

<style scoped>

</style>
