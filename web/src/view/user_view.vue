<template>
    <div style="margin-top: 1%">
        <Row>
            <Col :md="6" style="padding: 0.5%">
                <Card>
                    <p slot="title">头像</p>
                    <div :style="{width: '100%',height: 0,paddingBottom: '100%',overflow: 'hidden',background:'url('+user.head+')',backgroundSize:'cover'}">
                    </div>
                    <Button slot="extra" icon="md-create" shape="circle" type="text" @click="head_editable=true">
                    </Button>
                </Card>
            </Col>
            <Col :md="18" style="padding: 0.5%">
                <Card>
                    <p slot="title">个人简介</p>
                    <div>
                        <Form :label-width="80" label-position="left">
                            <FormItem label="用户名">
                                <Input :readonly="!user_editable" type="text" v-model="user.username"></Input>
                            </FormItem>
                            <FormItem label="手机号">
                                <Input :readonly="!user_editable" type="tel" v-model="user.phone"></Input>
                            </FormItem>
                            <FormItem label="简介">
                                <Input :readonly="!user_editable" type="tel" v-model="user.desc"></Input>
                            </FormItem>
                            <FormItem label="学号">
                                <p>{{user.number}}</p>
                            </FormItem>
                            <FormItem label="用户组">
                                <p>{{user_group[user.user_group]}}</p>
                            </FormItem>
                            <FormItem :style="{display:user_editable?'':'none'}">
                                <Button type="primary" @click="change_user">提交</Button>
                                <Button style="margin-left: 8px">取消</Button>
                            </FormItem>
                        </Form>
                    </div>
                    <Button slot="extra" icon="md-create" shape="circle" type="text"
                            @click="user_editable=!user_editable">
                    </Button>
                </Card>
            </Col>
            <Col :md="6" style="padding: 0.5%">
                <Card title="安全中心" icon="md-construct">
                    <CellGroup>
                        <Cell title="修改密码"/>
                        <Cell title="修改人脸"/>
                    </CellGroup>
                </Card>
            </Col>
            <Col :md="12" style="padding: 0.5%">
                <Card title="我的文章">
                    <CellGroup>
                        <Cell v-for="item in articles" :title="item.title"
                              :to="{name:'article_view',query:{id:item.id}}"/>
                    </CellGroup>
                </Card>
            </Col>
        </Row>
        <Modal
                v-model="head_editable"
                title="修改头像"
                @on-ok="change_head"
                @on-cancel="head_editable=false" :mask-closable="false" :closable="false">
            <div>
                <Form :label-width="80" label-position="left">
                    <FormItem label="上传头像">
                        <Upload
                                type="drag"
                                action="https://www.wiseweblab.com/api/api/upload/upload_picture" name="picture"
                                :multiple="false"
                                :show-upload-list="false"
                                :on-success="upload_success"
                        >
                            <div style="padding: 20px 0">
                                <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                                <p>点击上传头像</p>
                            </div>
                        </Upload>
                    </FormItem>
                    <FormItem label="头像预览">
                        <div style="width: 70%">
                            <div :style="{width: '100%',height: 0,paddingBottom: '100%',overflow: 'hidden',background:'url('+temp_head+')',backgroundSize:'cover'}">
                        </div>
                        </div>
                    </FormItem>
                </Form>
            </div>
        </Modal>
    </div>
</template>

<script>
    export default {
        name: "user_view",
        data() {
            return {
                user_editable: false,
                head_editable: false,
                temp_head: '',
                user_group: ['管理员', '普通用户'],
                user: {
                    user_group: 0,
                    number: '17h00000000',
                    username: '啦啦啦啦',
                    phone: '1588808792',
                    head: '/img/vue.png',
                    desc: '这个人很懒啥都没写'
                },
                articles: [
                    {
                        title: '文章一',
                        id: 76
                    },
                    {
                        title: '文章二',
                        id: 0
                    }
                ]
            }
        },
        methods: {
            change_head() {

            },
            change_user() {

            },
            upload_success(response, file, fileList) {
                if (response.code === 1) {
                    this.temp_head = response.data;
                }
            }
        },
        mounted() {

        }
    }
</script>

<style scoped>

</style>
