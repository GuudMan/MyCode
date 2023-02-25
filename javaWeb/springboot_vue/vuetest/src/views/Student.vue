<template>
    <div>
        <table>
            <tr>
                <th>编号</th>
                <th>姓名</th>
                <th>年龄</th>
                <th>性别</th>
            </tr>

            <tr v-for="item in students">
                <td>{{item.id}}</td>
                <td>{{item.name}}</td>
                <td>{{item.age}}</td>
                <td>{{item.gender}}</td>
            </tr>

        </table>
    </div>
</template>

<script>
    export default {
        name: "Student",
        data(){
            return {
                msg: "hello Vue",
                students:[
                    {
                        id: 1,
                        name: '大学英语',
                        age: 452,
                        gender: '男'
                    },
                    {
                        id: 2,
                        name: '大学英语',
                        age: 452,
                        gender: '男'
                    },
                    {
                        id: 3,
                        name: '大学英语',
                        age: 452,
                        gender: '男'
                    }
                ]
            }
        },
        created() {
        //    这是初始化的操作
            const _this = this
            axios.get('http://localhost:8181/student/findAll').then(function (resp) {
               _this.students = resp.data
            })
        }
    }
</script>

<style scoped>

</style>