<template>
    <Card style="margin-top: 2%">
        <p slot="title">
            修改文章
        </p>
        <div slot="extra">
            <span style="margin-right: 10px">自动保存</span>
            <i-switch v-model="auto_save" size="large">
                <span slot="open">开</span>
                <span slot="close">关</span>
            </i-switch>
        </div>
        <Form label-position="top">
            <FormItem label="标题">
                <Input v-model="title" @blur="save_article"></Input>
            </FormItem>
            <FormItem label="标签">
                <Cascader :data="tag_tree" v-model="tag_list" change-on-select @blur="save_article"></Cascader>
            </FormItem>
            <FormItem label="正文">
                <div style="height: 70vh">
                    <quill-editor
                            v-model="content"
                            :options="options"
                            style="height: 90%;"
                            @blur="save_article"
                    >
                    </quill-editor>
                </div>
            </FormItem>
            <FormItem>
                <Button type="primary" @click="add_article">提交</Button>
                <Button style="margin-left: 8px" type="success" @click="save_article_cache">保存</Button>
                <Button style="margin-left: 8px" type="warning" @click="load_cloud()">加载云端存档</Button>
                <Button style="margin-left: 8px" @click="cancel_edit">取消</Button>
            </FormItem>
        </Form>
    </Card>

</template>

<script>
    import hljs from 'highlight.js'
    import 'highlight.js/styles/monokai-sublime.css'
    import * as Quill from 'quill'  //引入编辑器
    import ImageResize from 'quill-image-resize-module'
    import {ImageExtend, QuillWatch} from 'quill-image-extend-module'
import VideoResize from 'quill-video-resize-module';


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
    Quill.register('modules/VideoResize', VideoResize);
    const maxRows = 10;
    const maxCols = 5;
    const tableOptions = [];
    for (let r = 1; r <= maxRows; r++) {
        for (let c = 1; c <= maxCols; c++) {
            tableOptions.push('newtable_' + r + '_' + c);
        }
    }

    export default {
        name: "change_article",
        data() {
            return {
                content: '',
                cloud: '',
                title: '',
                query: '',
                tag: '',
                auto_save: true,
                request: undefined,
                db: undefined,
                tag_tree: [],
                tag_list: [],
                options: {
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
                        table: true,
                        markdownShortcuts: {},
                        ImageExtend: {
                            loading: true,  // 可选参数 是否显示上传进度和提示语
                            name: 'picture',  // 图片参数名
                            size: 3,  // 可选参数 图片大小，单位为M，1M = 1024kb
                            action: 'https://www.wiseweblab.com/api/upload/upload_picture',  // 服务器地址, 如果action为空，则采用base64插入图片
                            // response 为一个函数用来获取服务器返回的具体图片地址
                            // 例如服务器返回{code: 200; data:{ url: 'baidu.com'}}
                            // 则 return res.data.url
                            response: (res) => {
                                return res.data;
                            },
                        },
                        VideoResize: {
                            modules: ['Resize', 'DisplaySize', 'Toolbar']
                        },
                        imageResize: {
                            modules: ['Resize', 'DisplaySize', 'Toolbar']
                        },
                        toolbar: {
                            container: [['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                                [{'header': [1, 2, 3, 4, false]}, {'list': 'ordered'}, {'list': 'bullet'}],
                                [{'indent': '-1'}, {'indent': '+1'}, {'align': []}],
                                ['blockquote', 'code-block', 'link', 'image','video', 'formula'],
                                [{'color': []}, {'background': []}], [{table: tableOptions}, {table: 'append-row'}, {table: 'append-col'}], ['clean']],
                            handlers: {
                                'image': function () {  // 劫持原来的图片点击按钮事件
                                    QuillWatch.emit(this.quill.id)
                                }
                            }
                        }
                    },
                    placeholder: '请在此输入内容'
                },


            }
        },
        methods: {
            add_article() {
                let that = this;
                let data = {
                    title: that.title,
                    content: that.content,
                    tag: this.tag_list[this.tag_list.length - 1],
                    token: that.$Cookies.get('token'),
                    article_id: this.query.id
                };
                this.$api.article.change_article(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag_tree();
                        this.delete_article_cache();
                        this.$router.back()
                    } else {

                    }
                })
            },
            get_tag_tree() {
                this.$api.tag.get_tag_tree().then(res => {
                    if (res.data.code === 1) {
                        let data = res.data.data;
                        this.tag_tree = this.set_tag_tree(data);
                        this.$store.commit('update_tag', data);
                    }
                })
            },
            set_tag_tree(tag) {
                let tree = [];
                tag.forEach(item => {
                    if (item['type'] === 0) {
                        tree.push({
                            value: item['ID'],
                            label: item['name'],
                            children: this.set_tag_tree(item['children'])
                        })
                    }
                });
                return tree;
            },
            get_tag_list(id) {
                this.$api.tag.get_tag_list(id).then(res => {
                    if (res.data.code === 1) {
                        this.tag_list = res.data.data;
                    }
                })
            },
            cancel_edit() {
                this.delete_article_cache();
                this.$router.back();
            },
            save_article() {
                if (this.auto_save) {
                    this.$Notice.info({
                        title: '正在自动保存···'
                    });
                    this.save_article_cache();
                }
            },
            load_article_cache() {
                let request = this.db.transaction('change_article', 'readwrite').objectStore('change_article').get(this.$route.query.id);
                let that = this;
                request.onerror = function (event) {
                    that.$Notice.warning({
                        title: '读取缓存失败',
                    })
                };
                request.onsuccess = function (event) {
                    if (request.result) {
                        that.content = request.result.content;
                        that.title = request.result.title;
                        that.tag = request.result.tag;
                        that.get_tag_list(request.result.tag);
                        that.$Notice.info({
                            title: '已读取缓存',
                        })
                    } else {
                        console.log('未获得数据记录');
                    }
                };
            },
            save_article_cache() {
                let request = this.db.transaction('change_article', 'readwrite')
                    .objectStore('change_article')
                    .add({
                        id: this.$route.query.id,
                        content: this.content,
                        title: this.title,
                        tag: this.tag_list[this.tag_list.length - 1]
                    });
                let request1 = this.db.transaction('change_article', 'readwrite')
                    .objectStore('change_article')
                    .put({
                        id: this.$route.query.id,
                        content: this.content,
                        title: this.title,
                        tag: this.tag_list[this.tag_list.length - 1]
                    });
                let that = this;
                request.onsuccess = function (event) {
                    that.$Notice.warning({
                        title: '本地保存失败,请重试(第一次保存可能出现失败情况)',
                    })
                };

                request.onerror = function (event) {
                    that.$Notice.success({
                        title: '本地保存成功',
                    })
                }
            },
            delete_article_cache() {
                let request = this.db.transaction(['change_article'], 'readwrite')
                    .objectStore('change_article')
                    .delete(this.$route.query.id);
                let that = this;
                request.onsuccess = function (event) {
                    that.$Notice.info({
                        title: '本地缓存已释放'
                    })
                };
                request.onerror = function (event) {
                    that.$Notice.warning({
                        title: '本地缓存释放失败'
                    })
                }
            },
            load_cloud() {
                this.query = this.$route.query;
                this.$api.article.get_article(this.$route.query.id).then((res) => {
                    if (res.data.code === 1) {
                        this.content = res.data.data.content;
                        this.title = res.data.data.title;
                        this.tag = res.data.data.tag;
                        this.get_tag_list(this.tag);
                        this.get_tag_tree();
                    }
                })
            }
        },
        mounted() {
            this.query = this.$route.query;
            this.$api.article.get_article(this.$route.query.id).then((res) => {
                if (res.data.code === 1) {
                    this.content = res.data.data.content;
                    this.title = res.data.data.title;
                    this.tag = res.data.data.tag;
                    this.get_tag_list(this.tag);
                    this.get_tag_tree();
                    this.request = window.indexedDB.open('article_cache');
                    this.request.onerror = function (event) {
                        this.$Notice.warning({
                            title: '本地数据库打开失败',
                            desc: '本地数据库打开失败，文章将不会自动缓存！'
                        })
                    };
                    let that = this;
                    this.request.onsuccess = function (event) {
                        that.db = event.target.result;
                        that.load_article_cache();
                    };
                    this.request.onupgradeneeded = function (event) {
                        that.db = event.target.result;
                        let objectStore;
                        if (!that.db.objectStoreNames.contains('article')) {
                            objectStore = that.db.createObjectStore('article', {keyPath: 'id', autoIncrement: true});
                            objectStore.createIndex('content', 'content', {unique: true});
                            objectStore.createIndex('title', 'title', {unique: true});
                        }
                        if (!that.db.objectStoreNames.contains('change_article')) {
                            objectStore = that.db.createObjectStore('change_article', {
                                keyPath: 'id',
                                autoIncrement: true
                            });
                            objectStore.createIndex('content', 'content', {unique: true});
                            objectStore.createIndex('title', 'title', {unique: true});
                            objectStore.createIndex('tag', 'tag', {unique: true});
                        }
                    }
                } else {
                    this.$router.push({name: 'login'});
                }
            })
        }
    }
</script>

<style scoped>
    >>>.quill-editor iframe {
        pointer-events: none;
    }
</style>
<style>
    :hover[style="background-color: rgb(0, 0, 0);"] {
        background-color: white !important;
    }

    [style="background-color: rgb(0, 0, 0);"] {
        color: black !important;
    }

    @media screen and (max-width: 900px) {
        .ql-toolbar {
            overflow-y: scroll;
            max-height: 10%;
        }
    }

    .ivu-notice-icon {
        display: none;
    }
    .quill-editor iframe{
        max-width: 100%;
    }
</style>
