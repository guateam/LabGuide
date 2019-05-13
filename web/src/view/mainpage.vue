<template>
    <div>
        <layout :style="{minHeight: '100vh'}" style="overflow: scroll">
            <sider collapsible :collapsed-width="78" v-model="isCollapsed" width="300">
                <h1 style="z-index: 999;color:white;text-align: center;margin-top: 20px;margin-bottom: 20px">
                    实验室指导资料库</h1>
                <ChildMenu :tag="tag">

                </ChildMenu>
            </sider>
            <layout>
                <i-header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                    <dropdown trigger="click" @on-click="changeMenu" style="float:right;margin-left:15px">
                        <i-button v-text="username" type="primary" size="large" href="javascript:void(0)">

                            <icon type="ios-arrow-down"></icon>
                        </i-button>
                        <dropdown-menu slot="list">
                            <dropdown-item name="logout">登出</dropdown-item>
                            <dropdown-item name="tag_tree" @click="$router.push({name:'tag_tree'})"
                                           v-if="$store.state.userInfo.group.value===0">管理标签树
                            </dropdown-item>
                            <dropdown-item v-if="usergroup==0" name="add_student">添加学生</dropdown-item>
                        </dropdown-menu>
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

    export default {
        name: "mainpage",
        components: {ChildMenu},
        data() {
            return {
                tag: [],
                choosen_id: "",
                article_list: [],
                isCollapsed: false,
                is_choose: false,
                username: "菜单",
            }
        },
        methods: {
            changeMenu(name) {
                if (name === "logout") {
                    this.$Cookies.remove('token');
                    this.$router.push({name: 'login'});
                }
            }
        },
        mounted() {
            let that = this;
            this.$api.tag.get_tag_tree().then((res) => {
                if (res.data.code === 1) {
                    that.tag = res.data.data;
                    that.username = that.$store.state.userInfo.username;
                    if (that.username === "") that.username = "菜单"
                } else
                    that.$router.push({name: 'login'});
            });
            this.$router.push({name:'default'})
        }
    }
</script>
