<template>
    <Card style="margin-top: 20px">
        <p slot="title">添加学生</p>
        <i-form ref="add_form" :model="info" :rules="rule" style="margin-left:20px">
              <form-item label="学号" prop="snum">
                <i-input size="large" v-model="info.snum" placeholder="输入学生学号"/>
              </form-item>
              <form-item >
                <i-button size="large" type="primary" style="width:120px" @click="add_student">添加</i-button>
              </form-item>
        </i-form>
        <i-table :columns="column" :data="students" :height="700"></i-table>
        <modal
            title="提示"
            v-model="modal"
        >
        <p v-text="alert_info"></p>
        </modal>
    </Card>
</template>
<script>
export default {
    name:"add_student",
    data(){
        return{
            info:{
                snum:"",
            },
            rule:{
                snum:[
                    {required: true, message: "学号不能为空", trigger:"blur"},
                    {type: 'string', min:10 ,message: "学号长度过短", trigger:"blur"},
                ]
            },
            column:[
                {
                    title:"学号",
                    key:"Snum"
                },
                {
                    title:"用户名",
                    key:"username",
                },
                {
                    title:"用户组",
                    key:"group",
                },
                {
                    title:"手机号",
                    key:"phone",
                }
            ],
            students:[
                {
                    Snum:"",
                    username:"",
                    group:"",
                    phone:"",
                }
            ],
            alert_info:"",
            modal:false,
        }
    },
    methods:{
        add_student(){
            let that = this;
            this.$refs["add_form"].validate((valid)=>{
                if(valid){
                    let data = {
                        token:that.$Cookies.get("token"),
                        snum:that.info.snum
                    }
                    this.$api.account.add_student(data).then((res)=>{
                        if(res.data.code === 1){
                            that.students.push({
                                Snum:data.Snum,
                                username:"",
                                group:"",
                                phone:"",
                            })
                        }else if(res.data.code === -2){
                            that.alert_info = "已存在该学生";
                            that.modal = true;
                        }
                    })
                }
            })

        }
    },
    mounted(){
        let that = this;
        this.$api.account.get_all_student().then((res)=>{
            if(res.data.code === 1){
                that.students = res.data.data
            }
        })
    }
}
</script>
