<template>
    <div>
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
                    key:"Snum",
                },
                {
                    title:"用户名",
                    key:"username",
                },
                {
                    title:"用户组",
                    key:"group",
                    width:150
                },
                {
                    title:"手机号",
                    key:"phone",
                },
                {
                        title: '操作',
                        key: 'action',
                        width: 250,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'primary',

                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            let info = params.row;
                                            if(info.group === "学生"){
                                                info.group = 1
                                            }else{
                                                 info.group = 0
                                            }
                                            this.$router.push({name:'modify_student',query:{info:info}})
                                        }
                                    }
                                }, '修改信息'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                    
                                    },
                                    on: {
                                        click: () => {
                                            let that = this;
                                            let info = {
                                                token:this.$Cookies.get('token'),
                                                snum:params.row.Snum
                                            }
                                            this.$api.account.admin_delete_student(info).then((res)=>{
                                                if(res.data.code === 1){
                                                    this.$api.account.get_all_student().then((res)=>{
                                                        if(res.data.code === 1){
                                                            that.students = res.data.data
                                                        }
                                                    })
                                                }else if(res.data.code === -2){
                                                    that.modal = true;
                                                    that.alert_info="无法删除自己";
                                                }else{
                                                    that.modal = true;
                                                    that.alert_info="删除失败";
                                                }
                                            })

                                        }
                                    }
                                }, '删除学生')
                            ]);
                        }
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
                            this.$api.account.get_all_student().then((res)=>{
                                if(res.data.code === 1){
                                    that.students = res.data.data
                                }
                            })
                        }else if(res.data.code === -2){
                            that.alert_info = "已存在该学生";
                            that.modal = true;
                        }
                    })
                }
            })
        },
        get_user(){
                this.$api.account.get_info().then(res => {
                    if (res.data.code === 1) {
                       this.username = res.data.data.username
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
