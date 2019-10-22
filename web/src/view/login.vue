<template>
    <div style="width: 100%" class="bg">
        <Row>
            <Col :sx="0" :md="16" class="notice_panel">
                <div style="height: 80px">
                    <img src="">
                    <span style="font-size: xx-large;border-left: rgba(0,0,0,0.3) 1px solid">中国计量大学软件外包实验室资料库</span>
                </div>
                <List border style="background: #fff">
                    <h1 slot="header">实验室资料库公告</h1>
                    <ListItem v-for="item in notice">
                        <ListItemMeta :title="item.content"
                                      :description="item.time"></ListItemMeta>
                    </ListItem>
                    <div slot="footer">
                        <p style="text-align: right;color: rgba(0,0,0,0.3)">version:{{version}} copyright@hanerx2019</p>
                    </div>
                </List>
            </Col>
            <Col :sx="24" :md="8" class="login_panel">
                <div v-if="!register">
                    <Card v-if="!show_camera">
                        <div style="text-align: center">
                            <Icon type="md-contact" size="100"/>
                            <h4>登录</h4>
                            <Divider></Divider>
                        </div>
                        <Form>
                            <FormItem label="用户名">
                                <Input v-model="username" type="text" placeholder="请输入用户名或者学号"></Input>
                            </FormItem>
                            <FormItem label="密码">
                                <Input v-model="password" type="password" password placeholder="请输入密码"></Input>
                            </FormItem>
                            <FormItem>
                                <Button long type="success" @click="get_face_vector">登录</Button>
                            </FormItem>
                        </Form>
                        <Row>
                            <Col :span="8" style="text-align:left">
                                <Button type="text" @click="show_forget">忘记密码</Button>
                            </Col>
                            <Col :span="8" :offset="8" style="text-align: right">
                                <Button type="text" @click="register=true">注册</Button>
                            </Col>
                        </Row>
                    </Card>
                    <Card v-if="show_camera" style="z-index: -2">
                        <div style="text-align: center">
                            <Icon type="md-contact" size="100"/>
                            <h4>登录</h4>
                            <Divider></Divider>
                        </div>
                        <FaceCheck :vector="face_vector" :username="username" :password="password"></FaceCheck>
                    </Card>
                </div>
                <div v-if="register">
                    <Card>
                        <div>
                            <Steps :current="register_step">
                                <Step title="检查学号" icon="ios-person"></Step>
                                <Step title="填写信息" icon="ios-create"></Step>
                                <Step title="注册人脸" icon="ios-camera"></Step>
                            </Steps>
                            <Divider></Divider>
                        </div>
                        <Form v-if="register_step===0">
                            <FormItem label="学号">
                                <Input v-model="register_form.s_num" type="text" placeholder="请输入学号"></Input>
                            </FormItem>
                            <FormItem>
                                <Button long type="success" @click="register_next_step">下一步</Button>
                            </FormItem>
                        </Form>
                        <Form v-if="register_step===1">
                            <FormItem label="用户名">
                                <Input v-model="register_form.username" type="text" placeholder="请输入用户名或者学号"></Input>
                            </FormItem>
                            <FormItem label="密码">
                                <Input v-model="register_form.password" type="password" password
                                       placeholder="请输入密码"></Input>
                            </FormItem>
                            <FormItem label="确认密码">
                                <Input v-model="confirm_password" type="password" password placeholder="请输入密码"></Input>
                            </FormItem>
                            <FormItem>
                                <Button long type="success" @click="register_next_step">下一步</Button>
                            </FormItem>
                        </Form>
                        <div v-if="register_step===2">
                            <FaceRegister :username="register_form.username" :password="register_form.password"
                                          :Snum="register_form.s_num" @success="register_next_step"></FaceRegister>
                        </div>
                        <Row>
                            <Col :span="8" :offset="16" style="text-align: right">
                                <Button type="text" @click="clean_register">登录</Button>
                            </Col>
                        </Row>
                    </Card>
                </div>
            </Col>
        </Row>
        <Modal v-model="show_old_api" width="360" :closable="false" :mask-closable="false" footer-hide>
            <p slot="header" style="color:#f60;text-align:center">
                <Icon type="ios-information-circle"></Icon>
                <span>旧API对接</span>
            </p>
            <div style="text-align:center" v-if="!face_change">
                <p>嗨，这里是旧api对接对话框！看样子你是第一次登录新的资料库，请在感觉pose摆好后点击下面的确认按钮</p>
                <Button type="success" size="large" long @click="face_change=true">录入人脸</Button>
            </div>
            <div v-if="face_change">
                <APIUpdate @success="show_old_api=false" :username="username" :password="password"></APIUpdate>
            </div>
        </Modal>
    </div>
</template>

<script>
    import FaceCheck from "../component/FaceCheck";
    import FaceRegister from "../component/FaceRegister";
    import APIUpdate from "../component/APIUpdate";

    export default {
        name: "login",
        components: {FaceCheck, FaceRegister, APIUpdate},
        data() {
            return {
                show_camera: false,
                face_vector: [],
                username: '',
                password: '',
                register: false,
                register_form: {
                    s_num: '',
                    username: '',
                    password: '',
                    face_vector: ''
                },
                register_step: 0,
                confirm_password: '',
                notice: [],
                show_old_api: false,
                face_change: false,
                version: '1.01b'
            };
        },
        methods: {
            get_face_vector() {
                let data = {
                    username: this.username,
                    password: this.password
                };
                this.$api.user.get_face_vector(data).then(res => {
                    if (res.data.code === 1) {

                        this.face_vector = res.data.data.face_vector;
                        this.show_camera = true;
                    } else if (res.data.code === 3) {
                        this.show_old_api = true;
                    } else {
                        this.$Message['error']({
                            background: true,
                            content: '用户名或密码错误'
                        });
                    }
                })
            },
            check_s_num() {
                this.$api.user.check_s_num(this.register_form.s_num).then(res => {
                    if (res.data.code === 1) {
                        this.register_step++;
                    }
                })
            },
            clean_register() {
                this.register = false;
                this.register_form = {
                    s_num: '',
                    username: '',
                    password: '',
                    face_vector: ''
                };
                this.confirm_password = '';
                this.register_step = 0;
            },
            register_next_step() {
                switch (this.register_step) {
                    case 0:
                        this.check_s_num();
                        break;
                    case 1:
                        if (this.register_form.password === this.confirm_password) {
                            this.register_step++;
                        } else {
                            this.$Message['error']({
                                background: true,
                                content: '两次密码不相同'
                            });
                        }
                        break;
                    case 2:
                        this.register_step++;
                        this.clean_register();
                        break;
                }
            },
            get_notice() {
                this.$api.notice.get_notice().then(res => {
                    if (res.data.code === 1) {
                        this.notice = res.data.data;
                    }
                })
            },
            show_forget() {
                this.$Message['warning']({
                    background: true,
                    content: '忘记密码功能尚未实装，请有需要的同学联系管理员'
                });
            }
        },
        mounted() {
            this.get_notice()
        }
    };
</script>
<style scoped>

    .bg {
        background-image: url("../../public/img/bg.jpg");
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -10;
        zoom: 1;
        background-color: #fff;
        background-repeat: no-repeat;
        background-size: cover;
        -webkit-background-size: cover;
        -o-background-size: cover;
        background-position: center 0;
        overflow: scroll;
    }

    @media screen and (min-width: 768px) {
        .notice_panel {
            padding-left: 5%;
            padding-right: 5%;
            padding-top: 10%
        }

        .login_panel {
            padding-left: 3%;
            padding-right: 3%;
            padding-top: 10%
        }
    }

    @media screen and (max-width: 768px) {
        .notice_panel {
            display: none;
        }

        .login_panel {
            padding-left: 7%;
            padding-right: 7%;
            padding-top: 10%
        }
    }
</style>
