<template>
    <Card style="margin-top: 2%" :padding="0">
        <p slot="title">评论区</p>
        <div>
            <CommentCard v-for="item in comments" :content="item" v-on:get_comment="get_comment"
                         :article_id="article_id"></CommentCard>
            <p style="text-align: center;color: grey;margin: 1%" v-if="comments.length===0">(╯‵□′)╯︵┻━┻没人评论啊</p>
        </div>
        <Row style="border-top: 1px solid #e8eaec;padding: 1%;margin-top: 1%">
            <Col :xs="20" :md="22">
                <Input v-model="content" :placeholder="placeholder" clearable
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
    import CommentCard from "./CommentCard";


    export default {
        name: "CommentList",
        components: {CommentCard},
        props: ['article_id'],
        data() {
            return {
                comments: [],
                content: '',
                father: '',
                placeholder: '(～o￣3￣)～来刷月活啊，指标要完成的啊'
            }
        },
        watch: {
            "article_id": 'get_comment'
        },
        methods: {
            get_comment() {
                this.$api.comment.get_comment(this.article_id).then(res => {
                    if (res.data.code === 1) {
                        this.comments = res.data.data;
                    }
                })
            },
            add_comment() {
                if (this.content !== '') {
                    let data = {
                        token: this.$Cookies.get('token'),
                        article_id: this.article_id,
                        content: this.content,
                        father: this.father
                    };
                    this.$api.comment.add_comment(data).then(res => {
                        if (res.data.code === 1) {
                            this.clear_comment();
                            this.get_comment();
                        }
                    })
                }
            },
            clear_comment() {
                this.content = '';
                this.father = '';
                this.placeholder = '(～o￣3￣)～来刷月活啊，指标要完成的啊';
            }
        },
        mounted() {
            this.get_comment()
        }
    }
</script>

<style scoped>
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
