<template>
    <div style="margin-top: 2%">
        <Card>
            <p slot="title">数据管理器</p>
            <Row>
                <Col :span="width?'8':'24'">
                    <i-menu theme="light" width="100%" @on-select="focus" @on-open-change="open_change" accordion
                            style="z-index:1">
                        <ChildMenuItemM :tag="tag"></ChildMenuItemM>
                    </i-menu>
                    <Button v-if="!width" @click="drawer=true" type="primary"
                            style="margin-top: 10px">{{!change?'修改选中':'新建根标签'}}
                    </Button>
                    <Button v-if="!width" @click="clear" :disabled="change"
                            style="margin-top: 10px;margin-left: 8px">取消
                    </Button>
                </Col>
                <Col span="16" v-if="width">
                    <Form style="margin-left: 10px">
                        <FormItem label="ID">
                            <Input v-model="id" disabled></Input>
                        </FormItem>
                        <FormItem label="名称">
                            <Input v-model="name"></Input>
                        </FormItem>
                        <FormItem>
                            <Button type="primary" @click="add_tag">新建</Button>
                            <Button style="margin-left: 8px" type="warning" @click="change_tag"
                                    :disabled="change">修改
                            </Button>
                            <Button style="margin-left: 8px" type="error" @click="delete_tag" :disabled="change">清除
                            </Button>
                            <Button style="margin-left: 8px" @click="clear" :disabled="change">清空</Button>
                            <Button style="margin-left: 8px" type="success"
                                    @click="$router.push({name:'add_article',query:{id:id}})" :disabled="change">添加文章
                            </Button>
                        </FormItem>
                    </Form>
                </Col>
                <Drawer title="修改标签选项" placement="right" :closable="true" v-model="drawer" v-if="!width"
                        :width="drawer_width">
                    <Form style="margin-left: 10px;margin-right: 10px">
                        <FormItem label="ID">
                            <Input v-model="id" disabled></Input>
                        </FormItem>
                        <FormItem label="名称">
                            <Input v-model="name"></Input>
                        </FormItem>
                        <FormItem>
                            <Button type="primary" @click="add_tag">新建</Button>
                            <Button style="margin-left: 8px" type="warning" @click="change_tag"
                                    :disabled="change">修改
                            </Button>
                            <Button style="margin-left: 8px" type="error" @click="delete_tag" :disabled="change">清除
                            </Button>
                        </FormItem>
                        <FormItem>
                            <Button @click="clear" :disabled="change">清空</Button>
                            <Button style="margin-left: 8px" type="success"
                                    @click="$router.push({name:'add_article',query:{id:id}})" :disabled="change">添加文章
                            </Button>
                        </FormItem>
                    </Form>
                </Drawer>
            </Row>
        </Card>
    </div>
</template>

<script>
    import ChildMenuItemM from "../component/ChildMenuItemM";

    export default {
        name: "tag_tree",
        components: {ChildMenuItemM},
        data() {
            return {
                tag: [],
                id: null,
                name: '',
                change: true,
                width: true,
                drawer: false,
                drawer_width: 300
            }
        },
        methods: {
            get_tag_tree() {
                this.$api.tag.get_tag_tree().then((res) => {
                    if (res.data.code === 1) {
                        this.tag = res.data.data;
                        this.$store.commit('update_tag', res.data.data);
                    }
                });
            },
            focus(id) {
                let tag = id.split('!@');
                this.id = tag[0];
                this.name = tag[1];
                this.change = false;
            },
            open_change(id) {
                if (id.length > 0) {
                    let tag = id[id.length - 1].split('!@');
                    this.id = tag[0];
                    this.name = tag[1];
                    this.change = false;
                }
            },
            add_tag() {
                let data = {
                    father: this.id,
                    name: this.name,
                    token: this.$Cookies.get('token')
                };
                this.$api.tag.add_tag(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag_tree();
                        this.id = null;
                        this.name = null;
                        this.change = true;
                        this.drawer = false;
                    }
                })
            },
            change_tag() {
                let data = {
                    tag_id: this.id,
                    name: this.name,
                    token: this.$Cookies.get('token')
                };
                this.$api.tag.change_tag(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag_tree();
                        this.id = null;
                        this.name = null;
                        this.change = true;
                        this.drawer = false;
                    }
                })
            },
            clear() {
                this.id = null;
                this.name = null;
                this.change = true;
                this.drawer = false;
            },
            delete_tag() {
                let data = {
                    tag_id: this.id,
                    token: this.$Cookies.get('token')
                };
                this.$api.tag.delete_tag(data).then(res => {
                    if (res.data.code === 1) {
                        this.get_tag_tree();
                        this.id = null;
                        this.name = null;
                        this.change = true;
                        this.drawer = false;
                    }
                })
            }
        },
        mounted() {
            this.get_tag_tree();
            this.width = document.documentElement.clientWidth > 1000;
            this.drawer_width = document.documentElement.clientWidth * 0.85;
        }
    }
</script>

<style scoped>

</style>
