<template>
    <Card style="margin-top: 2%" padding="0">
        <p slot="title">评论区</p>
        <div>
            <CommentCard></CommentCard>
        </div>
        <div style="border-top: 1px solid #e8eaec;padding: 1%;margin-top: 1%">
            <div style="width: 90%;display: inline">
                <Input style="width: 90%"></Input>
            </div>
            <div style="width: 20%;display: inline;margin-left: 1%">
                <Button>发送</Button>
            </div>
        </div>
    </Card>
</template>

<script>
    import CommentCard from "./CommentCard";


    export default {
        name: "CommentList",
        components: {CommentCard}
    }
</script>

<style scoped>

</style>
