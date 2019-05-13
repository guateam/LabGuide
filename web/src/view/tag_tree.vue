<template>
    <div style="margin-top: 20px">
        <Card>
            <p slot="title">数据管理器</p>
            <Row>
                <Col span="8">
                    <i-menu theme="light" width="100%" @on-select="focus" @on-open-change="open_change" accordion>
                        <ChildMenuItemM :tag="tag"></ChildMenuItemM>
                    </i-menu>
                </Col>
                <Col span="16">
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
                change: true
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
                    }
                })
            },
            clear() {
                this.id = null;
                this.name = null;
                this.change = true;
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
                    }
                })
            }
        },
        mounted() {
            this.get_tag_tree()
        }
    }
</script>

<style scoped>

</style>
