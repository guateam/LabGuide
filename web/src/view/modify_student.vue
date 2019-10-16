<template>
    <div>
        <Card style="margin-top: 2%">
        <p slot="title">修改学生信息</p>
        <i-form ref="modify_form" :model="info" :rules="rule" style="margin-left:20px">
              <form-item label="用户名" prop="username">
                <i-input  size="large" v-model="info.username" placeholder="输入新的用户名"/>
              </form-item>
              <form-item label="手机号" prop="phone">
                <i-input  size="large" v-model="info.phone" placeholder="输入新的手机号"/>
              </form-item>
              <form-item label="用户组" prop="group">
                <i-select v-model="info.group">
                    <i-option v-for="item in group_list" :value="item.value" :label="item.label">
                    </i-option>
                </i-select>
              </form-item>
              <form-item >
                <i-button size="large" type="primary" style="width:120px" @click="modify_student">确认修改</i-button>
              </form-item>
        </i-form>
    </Card>
    <modal
        title="提示"
        v-model="modal"
    >
        <p v-text="alert_info"></p>
    </modal>
    </div>
</template>
<script>
export default {
    name:"modify_student",
    data(){
        return{
            info:{
                username:"",
                phone:"",
                group:"",
            },
            rule:{
                username:[
                    {required:true,message:"用户名不能为空",trigger:"blur"}
                ],
                phone:[
                    {type:"string",min:11,max:11,message:"手机号长度不正确",trigger:"blur"}
                ],
            },
            group_list:[
                {value:0,label:"管理员"},
                {value:1,label:"学生"},
            ],
            modal:false,
            alert_info:"",

        }
    },
    methods:{
        modify_student(){
            let that = this;
            this.$refs["modify_form"].validate((valid)=>{
                if(valid){
                    let pack = {
                        token:that.$Cookies.get("token"),
                        snum:that.info.Snum,
                        username:that.info.username,
                        phone:that.info.phone,
                        group:that.info.group,
                    }
                    that.$api.user.admin_modify_info(pack).then((res)=>{
                        if(res.data.code === 1){
                            that.$router.back()
                        }else if(res.data.code === 0){
                            that.alert_info = "您不是管理员，无法修改";
                            that.modal = true;
                        }else if(res.data.code === -1){
                            that.alert_info = "用户名重复";
                            that.modal = true;
                        }else if(res.data.code === -2){
                            that.alert_info = "修改失败，请重试";
                            that.modal = true;
                        }
                    })
                }
            })
        }
    },
    mounted(){
        this.info = this.$route.query.info
    }
}
</script>
