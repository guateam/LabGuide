<template>
    <i-menu theme="dark" width="100%" @on-select="focus" @on-open-change="change" accordion>
        <ChildMenuItem :tag="tag"></ChildMenuItem>
    </i-menu>
</template>

<script>
    import ChildMenuItem from "./ChildMenuItem";

    export default {
        name: "ChildMenu",
        components: {ChildMenuItem},
        props: ['tag'],
        methods: {
            focus(id) {
                let tag = id.split('-');
                if (tag[1] === '0') {
                    this.$router.push({name: 'article_list', query: {id: tag[0]}})
                } else if (tag[1] === '1') {
                    this.$router.push({name: 'article_view', query: {id: tag[0]}})
                }
            },
            change(id) {
                console.info(id);
                if (id.length > 0) {
                    let tag = id[id.length - 1].split('-');
                    if (tag[1] === '0') {
                        this.$router.push({name: 'article_list', query: {id: tag[0]}})
                    } else if (tag[1] === '1') {
                        this.$router.push({name: 'article_view', query: {id: tag[0]}})
                    }
                }
            }
        }
    }
</script>

<style scoped>

</style>
