<template>
    <Card style="margin: 1%">
        <div slot="title">
            <p style="height:auto !important"><img height="25px" width="25px"
                                                   :src="content.head?content.head:default_head" alt="头像">{{content.username}}
            </p>
        </div>
        <div slot="extra">{{content.time}}</div>
        <p style="margin-left: 2%" v-html="refine_string(content.content)"></p>
        <Card style="margin: 1%;padding-top: 0.5%;padding-bottom: 0.5%" dis-hover :padding="0"
              v-if="content.children.length>0">
            <p class="child" v-for="item in content.children"><b>{{item.username}}:</b><span
                    v-html="refine_string(item.content)"></span>
                <Button style="float: right" type="text"
                        @click="reply('回复 @'+content.username+' : ','回复 @'+content.username+' : ')">回复
                </Button>
            </p>
        </Card>
        <div style="position: relative;right: 1%;text-align: right">
            <Button type="text" @click="reply('','回复 @'+content.username+' : ')">回复</Button>
        </div>
        <Row style="border-top: 1px solid #e8eaec;padding: 1%;margin-top: 1%" v-if="show_reply">
            <Col :xs="20" :md="22">
                <Input v-model="comment" :placeholder="placeholder" clearable
                       :on-clear="clear_comment"></Input>
            </Col>
            <Col :xs="4" :md="2" style="text-align: center;">
                <Button class="send-long" @click="add_comment">发送</Button>
                <Button icon="ios-arrow-forward" class="send" @click="add_comment"></Button>
            </Col>
        </Row>
    </Card>
</template>

<script>
    import baseUrl from "../api/base";

    export default {
        name: "CommentCard",
        props: ['content', 'article_id'],
        data() {
            return {
                show_reply: false,
                comment: '',
                father: '',
                placeholder: '(～o￣3￣)～都点开回复了，回复一下呗',
                username: '',
                article: '',
                default_head: baseUrl.host + '/api/static/default.jpg'
            }
        },
        watch: {
            article_id(val) {
                this.article = val;
            }
        },
        methods: {
            reply(content, placeholder) {
                this.show_reply = true;
                this.username = content;
                this.placeholder = placeholder;
            },
            clear_comment() {
                this.show_reply = false;
                this.comment = '';
                this.placeholder = '(～o￣3￣)～都点开回复了，回复一下呗';
                this.username = '';
            },
            add_comment() {
                if (this.comment !== '') {
                    let data = {
                        token: this.$Cookies.get('token'),
                        article_id: this.article,
                        content: this.username + this.comment,
                        father: this.father
                    };
                    this.$api.comment.add_comment(data).then(res => {
                        if (res.data.code === 1) {
                            this.clear_comment();
                            this.$emit("get_comment")
                        }
                    })
                }
            },
            refine_string(string) {
                let re = /(http:\/\/|https:\/\/)((\w|=|\?|\.|\/|&|-)+)/gi;
                return string.replace(re, function (a) {
                    return '<a href="' + a + '" target="view_window">' + a + '</a>';
                });
            }
        },

        mounted() {
            this.father = this.content.ID;
        }
    }
</script>

<style scoped>
    .child {
        padding-left: 1%;
        padding-bottom: 0.2%;
        padding-top: 0.2%;
        border-bottom: 1px solid #e8eaec;
        overflow: hidden;
        text-align: start;
    }

    .head {
        background-size: cover !important;
    }

    @media screen and (max-width: 1000px) {
        .send-long {
            display: none;
        }

        .send {
            width: auto;
        }
    }

    @media screen and (min-width: 1000px) {
        .send-long {
            width: 100%;
            margin-left: 4%;
        }

        .send {
            display: none;
        }
    }
</style>
