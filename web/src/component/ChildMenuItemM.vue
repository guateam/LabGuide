<template>
    <div>
        <submenu v-for='tg in tag' v-if="tg.children.length!==0" :name="tg.ID+'!@'+tg.name+'!@'+tg.father">
            <template slot="title">{{tg.name}}</template>
            <ChildMenuItem :tag="tg.children"></ChildMenuItem>
        </submenu>
        <menu-item v-for="tg in tag" :name="tg.ID+'!@'+tg.name+'!@'+tg.father" v-if="tg.children.length===0 && tg.type===0">
            <span>{{tg.name}}</span>
        </menu-item>
    </div>
</template>

<script>
    import ChildMenu from "./ChildMenu";

    export default {
        name: "ChildMenuItem",
        props: ['tag'],
        methods: {}
    }
</script>

<style scoped>

</style>
