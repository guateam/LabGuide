<template>
    <div class="ivu-cell">
        <div class="ivu-cell-link">
            <div class="ivu-cell-item">
                <div class="ivu-cell-icon"></div>
                <div class="ivu-cell-main">
                    <div class="ivu-cell-title">{{title}}</div>
                    <div class="ivu-cell-label"></div>
                </div>
                <div class="ivu-cell-footer"><span class="ivu-cell-extra"></span></div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CustomCell",
        props:['title']
    }
</script>

<style scoped>

</style>
