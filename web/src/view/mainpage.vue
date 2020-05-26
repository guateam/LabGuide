<template>
    <div>
        <layout :style="{minHeight: '100vh'}" style="overflow: scroll">
            <sider collapsible :collapsed-width="0" v-model="isCollapsed" breakpoint="md" width="300" v-if="width">
                <div style="overflow-y: scroll;height: 95%;position: absolute;width: 100%" class="no-srollbar">
                    <h1 style="z-index: 999;color:white;text-align: center;margin-top: 20px;margin-bottom: 20px"
                        @click="$router.push({name:'default'})">
                        实验室指导资料库</h1>
                    <ChildMenu :tag="$store.state.tag" :theme="'dark'">

                    </ChildMenu>
                </div>
            </sider>
            <Drawer placement="left" :closable="false" v-model="$store.state.drawer" v-if="!width">
                <h1 style="text-align: center" slot="header" @click="$router.push({name:'default'})">实验室指导资料库</h1>
                <ChildMenu :tag="$store.state.tag" :theme="'light'">

                </ChildMenu>
            </Drawer>
            <layout>
                <i-header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                    <Icon @click.native="show_drawer" style="margin-left: 1%" type="md-menu" size="24"
                          v-if="!width"></Icon>
                    <dropdown trigger="click" style="float:right;margin-left:15px" class="user-panel">
                        <i-button v-text="username" type="primary" size="large" href="javascript:void(0)">

                            <icon type="ios-arrow-down"></icon>
                        </i-button>

                        <!--                            <dropdown-item name="logout">登出</dropdown-item>-->
                        <!--                            <dropdown-item name="tag_tree" @click="$router.push({name:'tag_tree'})"-->
                        <!--                                           v-if="$Cookies.get('group')==0">管理标签树-->
                        <!--                            </dropdown-item>-->
                        <!--                            <dropdown-item v-if="$Cookies.get('group')==0" name="add_student">添加学生-->
                        <!--                            </dropdown-item>-->
                        <user-panel slot="list" :username="username" :head="head" :desc="desc">

                        </user-panel>

                    </dropdown>
                </i-header>
                <i-content :style="{padding: '0 16px 16px'}">
                    <div>
                        <router-view></router-view>
                    </div>
                </i-content>
            </layout>
        </layout>
    </div>
</template>
<script>
    import ChildMenu from "../component/ChildMenu";
    import UserPanel from "../component/UserPanel";
    import baseUrl from '../api/base'

    export default {
        name: "mainpage",
        components: {UserPanel, ChildMenu},
        data() {
            return {
                tag: [],
                choosen_id: "",
                article_list: [],
                isCollapsed: false,
                is_choose: false,
                username: "未知用户",
                width: true,
                head: baseUrl.host + '/api/static/default.jpg',
                desc: '这个人懒得要死，什么都没留下'
            }
        },
        methods: {
            // changeMenu(name) {
            //     if (name === "logout") {
            //         this.$Cookies.remove('token');
            //         this.$router.push({name: 'login'});
            //     } else if (name === 'tag_tree') {
            //         this.$router.push({name: 'tag_tree'})
            //     } else if (name === 'add_student') {
            //         this.$router.push({name: 'add_student'})
            //     }
            // },
            get_right_list() {
                this.$api.right.get_right_list().then(res => {
                    if (res.data.code === 1) {
                        this.$store.commit('set_right_list', res.data.data);
                    }
                })
            },
            show_drawer() {
                this.$store.commit('open_drawer', !this.$store.state.drawer);
            },
            get_tag_tree() {
                this.$api.tag.get_tag_tree().then(res => {
                    if (res.data.code === 1) {
                        this.$store.commit('update_tag', res.data.data);
                    }
                })
            },
            get_user() {
                this.$api.user.get_info().then(res => {
                    if (res.data.code === 1) {
                        this.username = res.data.data.username;
                        this.head = res.data.data.head;
                        this.desc = res.data.data.desc;
                    }
                })
            }
        },
        mounted() {
            this.get_right_list();
            this.get_tag_tree();
            this.get_user();
            this.width = document.documentElement.clientWidth > 1000;
        }
    }
</script>
<style scoped>

</style>
<style>
    .ivu-layout-sider-zero-width-trigger {
        top: 11px !important;
    }

    .ivu-layout-header {
        padding-left: 5% !important;
    }

    .ivu-drawer-body {
        padding-left: 0 !important;
        padding-right: 0 !important;
    }

    .no-srollbar::-webkit-scrollbar {
        display: none
    }

    @media screen and (min-width: 900px) {
        .user-panel > .ivu-select-dropdown {
            width: 20% !important;
            left: 78% !important;
        }
    }

    @media screen and (max-width: 900px) {
        .user-panel > .ivu-select-dropdown {
            width: 70% !important;
            left: 20% !important;
        }
    }
</style>
