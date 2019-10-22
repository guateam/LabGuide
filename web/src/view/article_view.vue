<template>
    <div>
        <Card class="card-top">
            <div slot="title"><h3 style="margin-bottom: 5px">{{content.title}}</h3> <span style="margin-top: 5px">更新日期：{{content.time}} 作者：{{content.author}} <span
                    v-if="content.changer!=''">修改人：{{content.changer}}</span><Button
                    @click="$router.push({name:'history_list',query:{id:$route.query.id}})"
                    type="text">历史记录</Button></span>
            </div>
            <div slot="extra" v-if="width">
                <Button v-if="rights.add_tag" type="info" size="large"
                        @click="show_tag=true">设置标签
                </Button>
                <Button v-if="rights.change_article" type="warning" size="large" style="margin-left: 8px"
                        @click="$router.push({name:'change_article',query:{id:$route.query.id}})">修改文章
                </Button>
                <Button v-if="rights.delete_article" type="error" size="large" style="margin-left: 8px"
                        @click="show_delete=true">清除文章
                </Button>
            </div>
            <div>
                <div style="margin: 5px;text-align:center" v-if="!width">
                    <Button v-if="rights.add_tag" type="info"
                            @click="show_tag=true">设置标签
                    </Button>
                    <Button v-if="rights.change_article" type="warning" style="margin-left: 8px"
                            @click="$router.push({name:'change_article',query:{id:$route.query.id}})">修改文章
                    </Button>
                    <Button v-if="rights.delete_article" type="error" style="margin-left: 8px"
                            @click="show_delete=true">清除文章
                    </Button>
                </div>
                <!--<div v-html="content.content" style="margin-left: 5px;margin-right: 5px"></div>-->
                <div>
                    <Alert show-icon :type="tag.tag_type" v-for="tag in tags">
                        {{tag.name}}
                        <Icon :type="tag.icon" slot="icon"></Icon>
                        <template slot="desc">{{tag.description}}
                            <Button v-if="rights.change_tag" type="warning" size="small"
                                    @click="show_change(tag)">修改标签
                            </Button>
                            <Button v-if="rights.delete_tag" type="error" size="small" style="margin-left: 5px"
                                    @click="show_delete_tag(tag.id)">清除标签
                            </Button>
                        </template>
                    </Alert>
                </div>
                <div>
                    <div id="toolbar" hidden></div>
                    <quill-editor
                            v-model="content.content"
                            :options="options"
                            disabled
                    ></quill-editor>
                </div>

            </div>
            <Modal
                    v-model="show_delete"
                    title="是否清除"
                    @on-ok="delete_article"
                    @on-cancel="show_delete=false">
                <p>你确定要清除这篇文章吗</p>
            </Modal>
            <Modal
                    v-model="show_delete_tag_state"
                    title="是否清除"
                    @on-ok="delete_tag"
                    @on-cancel="show_delete_tag_state=false">
                <p>你确定要清除这个标签吗</p>
            </Modal>
            <Modal
                    v-model="show_tag"
                    title="添加标签"
                    @on-ok="add_tag"
                    @on-cancel="show_tag=false">
                <Form style="margin-left: 10px">
                    <FormItem label="名称">
                        <Input v-model="tag_name"></Input>
                    </FormItem>
                    <FormItem label="描述">
                        <Input v-model="tag_desc"></Input>
                    </FormItem>
                    <FormItem label="类型">
                        <Select v-model="tag_type">
                            <Option value="info">通知</Option>
                            <Option value="success">成功</Option>
                            <Option value="warning">警告</Option>
                            <Option value="error">错误</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="图标">
                        <Input v-model="tag_icon"></Input>
                        <a href="https://www.iviewui.com/components/icon" target="view_window">图标查询</a>
                    </FormItem>
                    <FormItem label="预览">
                        <Alert show-icon :type="tag_type">
                            {{tag_name}}
                            <Icon :type="tag_icon" slot="icon"></Icon>
                            <template slot="desc">{{tag_desc}}
                            </template>
                        </Alert>
                    </FormItem>
                </Form>

            </Modal>
            <Modal
                    v-model="show_change_tag"
                    title="修改标签"
                    @on-ok="change_tag"
                    @on-cancel="show_change_tag=false">
                <Form style="margin-left: 10px">
                    <FormItem label="标签id">
                        <Input v-model="tag_info.id" disabled></Input>
                    </FormItem>
                    <FormItem label="名称">
                        <Input v-model="tag_info.name"></Input>
                    </FormItem>
                    <FormItem label="描述">
                        <Input v-model="tag_info.description"></Input>
                    </FormItem>
                    <FormItem label="类型">
                        <Select v-model="tag_info.tag_type">
                            <Option value="info">通知</Option>
                            <Option value="success">成功</Option>
                            <Option value="warning">警告</Option>
                            <Option value="error">错误</Option>
                        </Select>
                    </FormItem>
                    <FormItem label="图标">
                        <Input v-model="tag_info.icon"></Input>
                        <a href="https://www.iviewui.com/components/icon" target="view_window">图标查询</a>
                    </FormItem>
                    <FormItem label="预览">
                        <Alert show-icon :type="tag_info.tag_type">
                            {{tag_info.name}}
                            <Icon :type="tag_info.icon" slot="icon"></Icon>
                            <template slot="desc">{{tag_info.description}}
                            </template>
                        </Alert>
                    </FormItem>
                </Form>

            </Modal>
        </Card>
        <CommentList :article_id="$route.query.id"></CommentList>
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
        name: "article_view",
        components: {CommentList},
        data() {
            return {
                tags: [
                    {name: '加载中', description: 'loading···', tag_type: 'info', icon: 'md-infinite', id: 0}
                ],
                delete_tag_id: 0,
                tag_name: '',
                tag_desc: '',
                tag_type: 'info',
                tag_icon: '',
                tag_info: {
                    id: 0,
                    description: '',
                    name: '',
                    tag_type: 'info',
                    icon: ''
                },
                show_change_tag: false,
                show_delete_tag_state: false,
                show_tag: false,
                show_delete: false,
                width: true,
                content: {
                    title: '加载中',
                    content: '<p></p>',
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
                },
                rights: {
                    add_tag: false,
                    change_tag: false,
                    delete_tag: false,
                    change_article: false,
                    delete_article: false
                }
            }
        },
        watch: {
            "$route": "get_article"
        },
        methods: {
            show_delete_tag(id) {
                this.show_delete_tag_state = true;
                this.delete_tag_id = id;
            },
            show_change(tag) {
                this.tag_info = tag;
                this.show_change_tag = true;
            },
            delete_tag() {
                let data = {
                    tag_id: this.delete_tag_id,
                    token: this.$Cookies.get('token')
                };
                this.$api.article.delete_article_tag(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag();
                    }
                })
            },
            change_tag() {
                let data = {
                    article_id: this.$route.query.id,
                    name: this.tag_info.name,
                    token: this.$Cookies.get('token'),
                    description: this.tag_info.description,
                    icon: this.tag_info.icon,
                    tag_type: this.tag_info.tag_type,
                    tag_id: this.tag_info.id
                };
                this.$api.article.change_article_tag(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag();
                        this.tag_info = {
                            id: 0,
                            description: '',
                            name: '',
                            tag_type: 'info',
                            icon: ''
                        };
                        this.show_change_tag = false;
                    }
                })
            },
            add_tag() {
                let data = {
                    article_id: this.$route.query.id,
                    name: this.tag_name,
                    token: this.$Cookies.get('token'),
                    description: this.tag_desc,
                    icon: this.tag_icon,
                    tag_type: this.tag_type
                };
                this.$api.article.add_article_tag(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag();
                        this.tag_type = 'info';
                        this.tag_name = '';
                        this.tag_icon = '';
                        this.tag_desc = '';
                        this.show_tag = '';
                        this.show_tag = false;
                    }
                })
            },
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
                this.content = '';
                let id = this.$route.query.id;
                this.$api.article.get_article(id).then((res) => {
                    if (res.data.code === 1) {
                        this.content = res.data.data;
                        this.get_tag();
                    } else {
                        this.$router.replace({name: 'not_found'})
                    }
                })
            },
            get_tag() {
                this.$api.article.get_article_tag(this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.tags = res.data.data;
                    }
                })
            },
            get_rights() {
                this.$api.right.get_right(11, this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.rights.add_tag = true
                    }
                });
                this.$api.right.get_right(13, this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.rights.change_tag = true
                    }
                });
                this.$api.right.get_right(15, this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.rights.delete_tag = true
                    }
                });
                this.$api.right.get_right(9, this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.rights.change_article = true
                    }
                });
                this.$api.right.get_right(7, this.$route.query.id).then(res => {
                    if (res.data.code === 1) {
                        this.rights.delete_article = true
                    }
                });
            }
        },
        mounted() {
            this.get_article();
            this.width = document.documentElement.clientWidth > 900;
            this.get_rights();
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
            padding: 1%;
        }

        .ivu-layout-content {
            padding: 2% !important;
        }
    }
</style>
