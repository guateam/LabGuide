<template>
    <div style="margin-top: 1%">
        <Row>
            <Col :xs="24" :md="12">
                <Card style="margin-right: 0.5%">
                    <p slot="title">总览</p>
                    <div>
                        <p>
                            在线人数：0
                        </p>
                        <p>今日访客：0
                        </p>
                        <p>
                            新增文章：0
                        </p>
                        <p>
                            新增修改：0
                        </p>
                    </div>
                </Card>
            </Col>
            <Col :xs="24" :md="12">
                <Card style="margin-left: 0.5%">
                    <p slot="title">活动</p>
                </Card>
            </Col>
        </Row>
    </div>
</template>

<script>
    export default {
        name: "admin_view"
    }
</script>

<style scoped>

</style>
