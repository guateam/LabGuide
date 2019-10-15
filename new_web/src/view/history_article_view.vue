<template>
    <div>
        <Card class="card-top">
            <div slot="title"><h3 style="margin-bottom: 5px">{{content.date}}</h3> <span style="margin-top: 5px">修改人：{{content.username}}</span>
            </div>
            <div>
                <!--<div v-html="content.content" style="margin-left: 5px;margin-right: 5px"></div>-->
                <div>
                    <div id="toolbar" hidden></div>
                    <quill-editor
                            v-model="content.content"
                            :options="options"
                            disabled
                    ></quill-editor>
                </div>

            </div>
        </Card>
    </div>
</template>

<script>
    import hljs from 'highlight.js'
    import 'highlight.js/styles/monokai-sublime.css'
    import * as Quill from 'quill' //引入编辑器
    import ImageResize from 'quill-image-resize-module'
    import {ImageExtend} from 'quill-image-extend-module'
    import CommentList from "../component/CommentList";

    const katex = require('katex');
    window.katex = katex;

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
        name: "history_article_view",
        data() {
            return {
                content: {
                    date: '加载中',
                    content: '',
                },
                options: {
                    readOnly: true,
                    modules: {
                        formula: true,
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
                        toolbar: '#toolbar',

                    },
                    placeholder: '加载中···'
                }
            }
        },
        watch: {
            "$route": "get_history_article"
        },
        methods: {
            get_history_article() {
                this.content = '';
                let id = this.$route.query.id;
                this.$api.article.get_history_article(id).then((res) => {
                    if (res.data.code === 1) {
                        this.content = res.data.data;
                    } else {
                        this.$router.back();
                    }
                })
            },
        },
        mounted() {
            this.get_history_article();
        }
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
            padding: 1%;
        }

        .ivu-layout-content {
            padding: 2% !important;
        }
    }
</style>
