<template>
    <Card class="card-top">
        <div slot="title"><h3 style="margin-bottom: 5px">{{content.title}}</h3> <span style="margin-top: 5px">更新日期：{{content.time}} 作者：{{content.author}} <span
                v-if="content.changer!=''">修改人：{{content.changer}}</span></span>
        </div>
        <div slot="extra" v-if="width">
            <Button v-if="$Cookies.get('group')==0" type="warning" size="large"
                    @click="$router.push({name:'change_article',query:{id:$route.query.id}})">修改文章
            </Button>
            <Button v-if="$Cookies.get('group')==0" type="error" size="large" style="margin-left: 8px"
                    @click="delete_article">清除文章
            </Button>
        </div>
        <div style="margin: 5px;text-align:center" v-if="!width">
            <Button v-if="$Cookies.get('group')==0" type="warning" size="large"
                    @click="$router.push({name:'change_article',query:{id:$route.query.id}})">修改文章
            </Button>
            <Button v-if="$Cookies.get('group')==0" type="error" size="large" style="margin-left: 8px"
                    @click="show_delete=true">清除文章
            </Button>
        </div>
        <!--<div v-html="content.content" style="margin-left: 5px;margin-right: 5px"></div>-->
        <div>
            <div id="toolbar" hidden></div>
            <quill-editor
                    v-model="content.content"
                    :options="options"
                    disabled
            ></quill-editor>
        </div>

        <Modal
                v-model="show_delete"
                title="是否清除"
                @on-ok="delete_article"
                @on-cancel="show_delete=false">
            <p>你确定要清除这篇文章吗</p>
        </Modal>
    </Card>

</template>
<script>
    import hljs from 'highlight.js'
    import 'highlight.js/styles/monokai-sublime.css'
    import * as Quill from 'quill'  //引入编辑器
    import ImageResize from 'quill-image-resize-module'
    import {ImageExtend, QuillWatch} from 'quill-image-extend-module'

    const quillTable = require('quill-table');

    Quill.register(quillTable.TableCell);
    Quill.register(quillTable.TableRow);
    Quill.register(quillTable.Table);
    Quill.register(quillTable.Contain);
    Quill.register('modules/table', quillTable.TableModule);
    Quill.register('modules/imageResize', ImageResize);
    Quill.register('modules/ImageExtend', ImageExtend);
    const maxRows = 10;
    const maxCols = 5;
    const tableOptions = [];
    for (let r = 1; r <= maxRows; r++) {
        for (let c = 1; c <= maxCols; c++) {
            tableOptions.push('newtable_' + r + '_' + c);
        }
    }
    export default {
        name: "article_view",
        data() {
            return {
                show_delete: false,
                width: true,
                content: {
                    title: '加载中',
                    content: '<p>Loading...</p>',
                },
                options: {
                    readOnly: true,
                    modules: {
                        syntax: {
                            highlight: text => hljs.highlightAuto(text).value
                            // or
                            /*
                            highlight(text) {
                              const result = window.hljs.highlightAuto(text)
                              return result.value
                            }
                            */
                        },
                        table: {},
                        toolbar: '#toolbar'
                    }
                }
            }
        },
        watch: {
            "$route": "get_article"
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
            },
            get_article() {
                this.content = '加载中...';
                let id = this.$route.query.id;
                this.$api.article.get_article(id).then((res) => {
                    if (res.data.code === 1) {
                        this.content = res.data.data;
                    } else {
                        this.$router.back();
                    }
                })
            }
        },
        mounted() {
            this.get_article();
            this.width = document.documentElement.clientWidth > 900;
        },
    }
</script>
<style scoped>
    .card-top {
        margin-top: 2%;
    }
</style>
<style>
    :hover[style="background-color: rgb(0, 0, 0);"] {
        background-color: white !important;
    }

    [style="background-color: rgb(0, 0, 0);"] {
        color: black !important;
    }

    img {
        max-width: 100%;
    }

    @media screen and (max-width: 900px) {
        .ivu-card-body {
            padding: 2px;
        }

        .ivu-layout-content {
            padding: 2% !important;
        }
    }
</style>
