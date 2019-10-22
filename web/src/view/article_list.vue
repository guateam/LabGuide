<template>
    <div style="margin-top: 2%">
        <Card>
            <p slot="title">标签文章列表</p>
            <div slot="extra">
                <Button type="success" v-if="rights.add_article"
                        @click="$router.push({name:'add_article',query:{id:$route.query.id}})">添加文章
                </Button>
            </div>

            <CellGroup>
                <Cell :title="article.title" v-for="article in articles" :label="'更新时间：'+article.time"
                      :to="{name:'article_view',query:{id:article.ID}}"></Cell>
            </CellGroup>
            <h1 style="text-align: center" v-if="articles.length===0">该标签下暂无文章</h1>
        </Card>
    </div>
</template>

<script>
    export default {
        name: "article_list",
        data() {
            return {
                articles: [],
                rights: {
                    add_article: false
                }
            }
        },
        watch: {
            "$route": "get_articles"
        },
        methods: {
            get_articles() {
                this.$api.tag.get_articles(this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.articles = res.data.data;
                    }
                });
                this.$api.right.get_right(6, this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.rights.add_article = true
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
