<template>
    <div style="margin-top: 20px">
        <Row>
            <Col :sx="24" :md="24">
                <Card style="margin-left: 2%">
                    <Menu mode="horizontal" :active-name="1" @on-select="change_menu">
                        <MenuItem :name="1">
                            <Icon type="ios-paper"/>
                            用户管理
                        </MenuItem>
                        <MenuItem :name="2">
                            <Icon type="ios-people"/>
                            权限管理
                        </MenuItem>
                    </Menu>
                    <div v-if="activate===1">
                        <div style="margin: 1%">
                            <Row >
                                <Col style="" :span="8"><h3>用户管理</h3></Col>
                                <Col style="text-align: right" :span="8" :offset="8"><Button type="success">添加学生</Button></Col>
                            </Row>
                            <Divider></Divider>
                        </div>
                        <List>
                            <ListItem>
                                <ListItemMeta
                                        avatar="https://dev-file.iviewui.com/userinfoPDvn9gKWYihR24SpgC319vXY8qniCqj4/avatar"
                                        title="用户X" description="学号：1700000000"/>
                                <template slot="action">
                                    <li>
                                        <a href="">编辑</a>
                                    </li>
                                    <li>
                                        <a href="">清除</a>
                                    </li>
                                </template>
                            </ListItem>
                        </List>
                    </div>
                    <div v-if="activate===2"></div>
                </Card>
            </Col>
        </Row>
    </div>
</template>

<script>
    export default {
        name: "student_control_center",
        data() {
            return {
                activate: 1,
            }
        },
        methods: {
            change_menu(name) {
                this.activate = name;
            }
        }
    }
</script>

<style scoped>
    >>>.ivu-menu{
        z-index: 1;
    }
</style>
