<template>
    <el-form style="width: 60%" :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
        <el-form-item label="编号" prop="id">
            <el-input v-model="ruleForm.id" readonly></el-input>
        </el-form-item>

        <el-form-item label="姓名" prop="name">
            <el-input v-model="ruleForm.name"></el-input>
        </el-form-item>

        <el-form-item label="年龄" prop="age">
            <el-input v-model="ruleForm.age"></el-input>
        </el-form-item>

        <el-form-item label="性别" prop="gender">
            <el-select v-model="ruleForm.gender" placeholder="请选择性别">
                <el-option label="男" value="男"></el-option>
                <el-option label="女" value="女"></el-option>
            </el-select>
        </el-form-item>

        <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">修改</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
    export default {
        data() {
            return {
                ruleForm: {
                    id: '',
                    name: '',
                    age: '',
                    gender: ''
                },
                rules: {
                    name: [
                        { required: true, message: '请输入学生姓名', trigger: 'blur' },
                        { min: 1, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
                    ],
                    age: [
                        { required: true, message: '请输入年龄', trigger: 'blur' }
                    ],
                    gender: [
                        { required: true, message: '请选择性别', trigger: 'change' }
                    ]

                }
            };
        },
        methods: {
            submitForm(formName) {
                const _this = this
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        axios.put('http://localhost:8181/student/update', this.ruleForm).then(function (resp) {
                            if(resp.data=='success'){
                                // alert('添加成功')
                                // _this.$message("添加成功")

                                _this.$alert('《 '+_this.ruleForm.name+'》修改成功', '消息', {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        _this.$router.push('/StudentManager')
                                    }
                                })

                                //
                            }
                        })
                    } else {
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        },
    created() {
        const _this = this
        axios.get('http://localhost:8181/student/findById/' + this.$route.query.id).then(function(resp) {
            _this.ruleForm=resp.data
        })
        }
    }
</script>