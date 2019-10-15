<template>
    <div style="width: 100%" class="bg">
        <Row>
            <Col :sx="0" :md="16" style="padding-left: 5%;padding-right: 5%;padding-top: 10%">
                <div style="height: 80px">
                    <img src="">
                    <span style="font-size: xx-large;border-left: rgba(0,0,0,0.3) 1px solid">中国计量大学软件外包实验室资料库</span>
                </div>
                <List border style="background: #fff">
                    <h1 slot="header">实验室资料库公告</h1>
                    <ListItem>
                        <ListItemMeta title="请老用户登录后进行人脸识别升级操作" description="2019-10-15"></ListItemMeta>
                    </ListItem>
                    <div slot="footer">
                        <p style="text-align: right;color: rgba(0,0,0,0.3)">version:1.01a copyright@hanerx2019</p>
                    </div>
                </List>
            </Col>
            <Col :sx="24" :md="8" class="login_panel">
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
                            <Button type="text">忘记密码</Button>
                        </Col>
                        <Col :span="8" :offset="8" style="text-align: right">
                            <Button type="text">注册</Button>
                        </Col>
                    </Row>
                </Card>
                <Card v-if="show_camera" style="z-index: -2">
                    <div style="text-align: center">
                        <Icon type="md-contact" size="100"/>
                        <h4>登录</h4>
                        <Divider></Divider>
                    </div>
                    <FaceCheck :vector="face_vector"></FaceCheck>
                </Card>
            </Col>
        </Row>
    </div>
</template>

<script>
    import FaceCheck from "../component/FaceCheck";

    export default {
        name: "login",
        components: {FaceCheck},
        data() {
            return {
                show_camera: false,
                face_vector: [],
                username: '',
                password: ''
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
                    }
                })
            }
        },
        mounted() {

        }
    };
</script>
<style scoped>
    .login_panel {
        padding-left: 5%;
        padding-right: 5%;
        padding-top: 10%
    }

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
</style>
