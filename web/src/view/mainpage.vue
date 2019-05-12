<template>
    <div>
        <layout :style="{minHeight: '100vh'}" style="overflow: scroll">
            <sider collapsible :collapsed-width="78" v-model="isCollapsed" width="300">
                <i-menu theme="dark" width="100%" :class="menuitemClasses" @on-select="focus">
                    <submenu v-for="tg in tag" :name="tg.ID">
                        <template slot="title">
                            {{tg.name}}
                        </template>
                        <menu-item v-for="child in tg.children" :name="child.ID">
                            <span>{{child.name}}</span>
                        </menu-item>
                    </submenu>
                </i-menu>
            </sider>
            <layout>
                <i-header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
                    <dropdown trigger="click" @on-click="changeMenu" style="float:right;margin-left:15px">
                        <i-button type="primary" size="large" href="javascript:void(0)">
                            
                            <icon type="ios-arrow-down"></icon>
                        </i-button>
                        <dropdown-menu slot="list">
                            <dropdown-item name="logout">登出</dropdown-item>
                        </dropdown-menu>
                    </dropdown>
                    <i-button type="success" @click.native="add_article()" :disabled="!is_choose" size="large" style="float:right;margin-top:15px" >
                        为本标签添加文章
                    </i-button>
                </i-header>
                <i-content :style="{padding: '0 16px 16px'}">
                    <div>
                      <card @click.native="enter_article(item.ID)" v-for="item in article_list" style="width:50%;margin-top:12px;margin-right:5px;">
                       <p slot="title">{{item.title}}</p>
                       发布时间:<p v-text="item.time"></p>
                      </card>
                    </div>
                </i-content>
            </layout>
        </layout>
    </div>
</template>
<script>
export default {
    name:"mainpage",
    data(){
        return {
            tag:[],
            choosen_id:"",
            article_list:[],
            isCollapsed: false,
            is_choose:false,
            username:"",
        }
    },
    methods:{
        menuitemClasses: function () {
            return [
                'menu-item',
                this.isCollapsed ? 'collapsed-menu' : ''
            ]
        },
        focus(id){
            let that = this;
            this.is_choose = true;
            this.choosen_id = id;
            this.$api.tag.get_articles(id).then((res)=>{
                if(res.data.code == 1){
                    that.article_list = res.data.data;
                }else{
                    that.$router.push({name:'login'});
                }
            })
        },
        enter_article(id){
            this.$router.push({name:'article',query:{article_id:id}});
        },
        changeMenu(name){
            if(name === "logout"){
                this.$Cookies.remove('token');
                this.$router.push({name:'login'});
            }
        },
        add_article(){
            let id = this.choosen_id;
            this.$router.push({name:'add_article',query:{tag_id:id}})
        }
    },
    mounted(){
        let that = this;
        this.$api.tag.get_tag_tree().then((res)=>{
            if(res.data.code === 1){
                that.tag = res.data.data;
                that.username = that.$store.state.userInfo.username;
            }
            else
                that.$router.push({name:'login'});
        })
    }
}
</script>