<template>
    <div>
        <el-table :data="tableData" border style="width: 100%">
            <el-table-column
                    fixed
                    prop="id"
                    label="编号"
                    width="150">
            </el-table-column>
            <el-table-column
                    prop="name"
                    label="姓名"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="age"
                    label="年龄"
                    width="120">
            </el-table-column>
            <el-table-column
                    prop="gender"
                    label="性别"
                    width="120">
            </el-table-column>
            <el-table-column
                    label="操作"
                    width="100">
                <template slot-scope="scope">
                    <el-button @click="edit(scope.row)" type="text" size="small">修改</el-button>
                    <el-button @click="deleteStudent(scope.row)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>

        <!--page-size="6" 设置每页的条数-->
        <el-pagination
                background
                layout="prev, pager, next"
                :total="50"
                @current-change="page">
        </el-pagination>

    </div>
</template>

<script>
    export default {
        methods: {
            edit(row) {
                this.$router.push({
                    path: '/StudentUpdate',
                    query:{
                        id:row.id
                    }
                })
            },
            deleteStudent(row) {
                const _this = this
                axios.delete('http://localhost:8181/student/deleteById/'+row.id).then(function (resp) {
                    _this.$alert('《 '+row.name+'》删除成功', '消息', {
                        confirmButtonText: '确定',
                        callback: action => {
                            // _this.$router.push('/StudentManager')
                            window.location.reload()
                        }
                    })
                })
            },
            page(currentPage){
                // alert(currentPage)
                const _this = this
                axios.get('http://localhost:8181/student/findAll/'+currentPage+'/6').then(function (resp) {
                    _this.tableData = resp.data.content
                    _this.total = resp.data.totalElements
                })
            }
        },

        created() {
            const _this = this
            axios.get('http://localhost:8181/student/findAll/1/6').then(function (resp) {
            _this.tableData = resp.data.content
            _this.total = resp.data.totalElements
            })
        },

        data() {
            return {
                total:null,
                tableData: null
            }
        }
    }
</script>