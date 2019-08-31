<template>
    <div style="width: 100%">
        <Row style="border-bottom: rgba(0,0,0,0.1) 1px solid">
            <Col :xs="8" :md="6">
                <div :style="{width: '100%',height: 0,paddingBottom: '100%',overflow: 'hidden',background:'url('+head+')',backgroundSize:'cover'}">
                </div>
            </Col>
            <Col :xs="16" :md="18">
                <div style="padding-left: 5%;padding-top: 10%;line-height:1.5">
                    <h2 style="margin-bottom: 5px;line-height: 1.5">{{username}}</h2>
                    <span>{{desc}}</span>
                </div>
            </Col>
        </Row>
        <Row style="border-bottom: rgba(0,0,0,0.1) 1px solid">
            <Col :md="12" v-for="item in menu">
                <CustomCell @click.native="click_cell(item.route)" :title="item.title"></CustomCell>
            </Col>
        </Row>
        <Row style="line-height: 3">
            <Col :xs="0" :md="20"><p style="margin-left: 5%">copyright@ 2019 by hanerx</p></Col>
            <Col :xs="24" :md="4">
                <Button type="text" @click="logout">登出</Button>
            </Col>
        </Row>
    </div>
</template>

<script>
    import CustomCell from "./CustomCell";

    export default {
        name: "UserPanel",
        components: {CustomCell},
        props: ['username', 'head','desc'],
        data() {
            return {
                menu: [
                    {
                        title: '个人中心',
                        route: {
                            name: 'user_view'
                        }
                    },
                    {
                        title: '后台管理',
                        route: {
                            name: 'admin_view'
                        }
                    },
                    {
                        title: '标签树管理',
                        route: {
                            name: 'tag_tree'
                        }
                    },
                    {
                        title: '用户管理',
                        route: {
                            name: 'add_student'
                        }
                    }
                ]
            }
        },
        methods: {
            click_cell(route) {
                this.$router.push(route)
            },
            logout() {
                this.$Cookies.remove('token');
                this.$router.push({name: 'login'});
            }
        },
        mounted() {
            if (this.$Cookies.get('group') != 0) {
                this.menu = [
                    {
                        title: '个人中心',
                        route: {
                            name: 'user_view'
                        }
                    },
                ]
            }
        }
    }
</script>

<style scoped>

</style>
