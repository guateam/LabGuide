<template>
    <div style="margin-top: 20px">
        <Row>
            <Col :sx="24" :md="24">
                <Card style="margin-left: 2%">
                    <Menu mode="horizontal" :active-name="1" @on-select="change_menu">
                        <MenuItem :name="1">
                            <Icon type="ios-paper"/>
                            用户管理
                        </MenuItem>
                        <MenuItem :name="2">
                            <Icon type="ios-people"/>
                            权限管理
                        </MenuItem>
                    </Menu>
                    <div v-if="activate===1">
                        <div style="margin: 1%">
                            <Row>
                                <Col style="" :span="8"><h3>用户管理</h3></Col>
                                <Col style="text-align: right" :span="8" :offset="8">
                                    <Button type="success" @click="add_confirm">添加学生</Button>
                                </Col>
                            </Row>
                            <Divider></Divider>
                        </div>
                        <List>
                            <ListItem v-for="item in users">
                                <ListItemMeta
                                        :avatar="item.head?item.head:default_head"
                                        :title="item.username" :description="'学号：'+item.s_num"/>
                                <template slot="action">
                                    <li>
                                        <Button type="primary" ghost>编辑</Button>
                                    </li>
                                    <li>
                                        <Button type="error" ghost @click="delete_confirm(item.id)">清除</Button>
                                    </li>
                                </template>
                            </ListItem>
                        </List>
                    </div>
                    <div v-if="activate===2"></div>
                </Card>
            </Col>
        </Row>
        <Modal v-model="delete_modal.show" width="360" :on-cancel="delete_cancel">
            <p slot="header" style="color:#f60;text-align:center">
                <Icon type="ios-information-circle"></Icon>
                <span>清除确认</span>
            </p>
            <div style="text-align:center">
                <p>清除该账户后将不能还原</p>
                <p>是否继续?</p>
            </div>
            <div slot="footer">
                <Button type="error" size="large" long :loading="delete_modal.loading" @click="delete_user">清除</Button>
            </div>
        </Modal>
        <Modal
                v-model="add_modal.show"
                title="添加用户"
                footer-hide
        >
            <Form>
                <FormItem label="学号" :error="add_modal.check?'账号已存在':''">
                    <label>
                        <Input v-model="add_modal.s_num"></Input>
                    </label>
                </FormItem>
                <FormItem label="用户组">
                    <label>
                        <Select v-model="add_modal.group">
                            <Option v-for="item in right_group" :value="item.group_id">{{item.desc}}</Option>
                        </Select>
                    </label>
                </FormItem>
                <FormItem style="text-align: right">
                    <Button  @click="add_cancel">取消</Button>
                    <Button type="primary" @click="add_user" style="margin-left: 1%">添加</Button>
                </FormItem>
            </Form>
        </Modal>
    </div>
</template>

<script>
    import baseUrl from "../api/base";

    export default {
        name: "student_control_center",
        data() {
            return {
                activate: 1,
                users: [],
                default_head: baseUrl.host + '/static/default.jpg',
                delete_modal: {
                    show: false,
                    loading: false,
                    user_id: 0
                },
                add_modal: {
                    show: false,
                    s_num: '',
                    group: -1,
                    check: false
                },
                right_group: []
            }
        },
        methods: {
            change_menu(name) {
                this.activate = name;
            },
            get_users() {
                this.$api.user.get_users().then(res => {
                    if (res.data.code === 1) {
                        this.users = res.data.data;
                    }
                })
            },
            delete_confirm(user_id) {
                this.delete_modal.show = true;
                this.delete_modal.user_id = user_id;
            },
            delete_user() {
                this.delete_modal.loading = true;
                this.$api.user.delete_user(this.delete_modal.user_id).then(res => {
                    if (res.data.code === 1) {
                        this.delete_cancel();
                        this.get_users();
                    }
                })
            },
            delete_cancel() {
                this.delete_modal = {
                    show: false,
                    loading: false,
                    user_id: 0
                };
            },
            add_confirm() {
                this.add_modal.show = true;
            },
            get_right_group() {
                this.$api.right.get_right_groups().then(res => {
                    if (res.data.code === 1) {
                        this.right_group = res.data.data;
                    }
                })
            },
            add_cancel() {
                this.add_modal = {
                    show: false,
                    s_num: '',
                    group: -1,
                    check: false
                }
            },
            add_user() {
                this.add_modal.check = false;
                let data = {
                    token: this.$Cookies.get('token'),
                    s_num: this.add_modal.s_num,
                    group: this.add_modal.group
                };
                this.$api.user.add_user(data).then(res => {
                    if (res.data.code === 1) {
                        this.add_cancel();
                        this.get_users();
                    } else if (res.data.code === -9) {
                        this.add_modal.check = true;
                    }
                })
            }
        },
        mounted() {
            this.get_users();
            this.get_right_group();
        }
    }
</script>

<style scoped>
    >>> .ivu-menu {
        z-index: 1;
    }
</style>
