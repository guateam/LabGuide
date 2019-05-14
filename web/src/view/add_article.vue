<template>
    <Card style="margin-top: 20px">
        <p slot="title">
            添加文章
        </p>
        <Form :label-width="100">
            <FormItem label="标题">
                <Input v-model="title"></Input>
            </FormItem>
            <FormItem label="正文">
                <div style="height: 70vh">
                    <quill-editor
                            v-model="content"
                            :options="options"
                            style="height: 90%;"
                    >
                    </quill-editor>
                </div>
            </FormItem>
            <FormItem>
                <Button type="primary" @click="add_article">提交</Button>
                <Button style="margin-left: 8px" @click="$router.back()">取消</Button>
            </FormItem>
        </Form>
    </Card>

</template>

<script>
    import * as Quill from 'quill'  //引入编辑器
    import ImageResize from 'quill-image-resize-module'
    import {ImageExtend, QuillWatch} from 'quill-image-extend-module'

    Quill.register('modules/imageResize', ImageResize);
    Quill.register('modules/ImageExtend', ImageExtend);

    export default {
        name: "add_article",
        data() {
            return {
                content: '',
                title: '',
                query:'',
                options: {
                    modules: {
                        ImageExtend: {
                            loading: true,  // 可选参数 是否显示上传进度和提示语
                            name: 'picture',  // 图片参数名
                            size: 3,  // 可选参数 图片大小，单位为M，1M = 1024kb
                            action: 'http://localhost:5000/api/upload/upload_picture',  // 服务器地址, 如果action为空，则采用base64插入图片
                            // response 为一个函数用来获取服务器返回的具体图片地址
                            // 例如服务器返回{code: 200; data:{ url: 'baidu.com'}}
                            // 则 return res.data.url
                            response: (res) => {
                                return res.data;
                            },
                        },
                        imageResize: {
                            modules: ['Resize', 'DisplaySize', 'Toolbar']
                        },
                        toolbar: {
                            container: [['bold', 'italic', 'underline', 'strike'],        // toggled buttons
                                [{'header': [1, 2, 3, 4, false]}, {'list': 'ordered'}, {'list': 'bullet'}],
                                [{'indent': '-1'}, {'indent': '+1'}],
                                ['blockquote', 'code-block', 'link', 'image', 'formula'],
                                [{'color': []}, {'background': []}]],
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
            add_article(){
                let that=this;
                let data = {
                    title: that.title,
                    content: that.content,
                    tag: that.query.id,
                    token: that.$Cookies.get('token')
                };
                this.$api.article.add_article(data).then(res => {
                    if (res.data.code === 1) {
                        this.$router.go(-1);
                    }else{

                    }
                })
            }
        },
        mounted() {
            this.query = this.$route.query;
        }
    }
</script>

<style scoped>

</style>
<style>
    :hover[style="background-color: rgb(0, 0, 0);"] {
        background-color: white !important;
    }

    [style="background-color: rgb(0, 0, 0);"] {
        color: black !important;
    }
</style>
