<template>
    <Card style="margin-top: 20px">
        <div slot="title"><h3 style="margin-bottom: 5px">{{content.title}}</h3> <span style="margin-top: 5px">更新日期：{{content.time}}</span>
        </div>
        <div slot="extra">
            <Button v-if="$Cookies.get('group')==0" type="warning" size="large"
                    @click="$router.push({name:'change_article',query:{id:$route.query.id}})">修改文章
            </Button>
            <Button v-if="$Cookies.get('group')==0" type="error" size="large" style="margin-left: 8px"
                    @click="delete_article">清除文章
            </Button>
        </div>

        <!--<div v-html="content.content" style="margin-left: 5px;margin-right: 5px"></div>-->
        <quill-editor
                v-model="content.content"
                :options="options"
                disabled
        ></quill-editor>
    </Card>
</template>
<script>
    import * as Quill from 'quill'  //引入编辑器
    import ImageResize from 'quill-image-resize-module'
    import {ImageExtend, QuillWatch} from 'quill-image-extend-module'

    Quill.register('modules/imageResize', ImageResize);
    Quill.register('modules/ImageExtend', ImageExtend);
    export default {
        name: "article_view",
        data() {
            return {
                content: {
                    title: '加载中',
                    content: '<p>Loading...</p>',
                },
                options: {
                    readOnly: true,
                    modules: {
                        toolbar:null
                    }
                }
            }
        },
        watch: {
            "$route": "get_articles"
        },
        methods: {
            delete_article() {
                let data = {
                    article_id: this.$route.query.id,
                    token: this.$Cookies.get('token')
                };
                this.$api.article.delete_article(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag_tree();
                        this.$router.back();
                    }
                })
            },
            get_tag_tree() {
                this.$api.tag.get_tag_tree().then(res => {
                    if (res.data.code === 1) {
                        this.$store.commit('update_tag', res.data.data);
                    }
                })
            }
        },
        mounted() {
            let id = this.$route.query.id;
            this.$api.article.get_article(id).then((res) => {
                if (res.data.code === 1) {
                    this.content = res.data.data;
                } else {
                    this.$router.back();
                }
            })
        },
    }
</script>
<style>
    @import url("https://cdn.quilljs.com/1.3.6/quill.core.css");
    @import url("https://cdn.quilljs.com/1.3.6/quill.snow.css");
    @import url("https://cdn.quilljs.com/1.3.6/quill.bubble.css");

    :hover[style="background-color: rgb(0, 0, 0);"] {
        background-color: white !important;
    }

    [style="background-color: rgb(0, 0, 0);"] {
        color: black !important;
    }

    img {
        max-width: 100%;
    }

</style>
