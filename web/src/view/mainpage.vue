<template>
    <div>
        <layout :style="{minHeight: '100vh'}" style="overflow: scroll">
            <sider collapsible :collapsed-width="78" v-model="isCollapsed" width="300">
                <i-menu theme="dark" width="100%" :class="menuitemClasses" @on-select="focus">
                    <submenu v-for="tg in tag" :name="tg.name">
                        <template slot="title">
                            {{tg.name}}
                        </template>
                        <menu-item v-for="child in tg.children" :name="child.name">
                            <span>{{child.name}}</span>
                        </menu-item>
                    </submenu>
                </i-menu>
            </sider>
            <layout>
                <i-header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}"></i-header>
                <i-content :style="{padding: '0 16px 16px'}">
                    <breadcrumb :style="{margin: '16px 0'}">
                        <breadcrumb-item v-text="choosen"></breadcrumb-item>
                    </breadcrumb>

                    <div>
                      
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
            choosen:"",
            isCollapsed: false,
        }
    },
    methods:{
        menuitemClasses: function () {
            return [
                'menu-item',
                this.isCollapsed ? 'collapsed-menu' : ''
            ]
        },
        focus(name){
            this.choosen = name;
            
        }
    },
    mounted(){
        let that = this;
        this.$api.tag.get_tag_tree().then((res)=>{
            if(res.data.code === 1)
                that.tag = res.data.data
            else
                that.$router.push({name:'login'})
        })
    }
}
</script>