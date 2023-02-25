<template>
    <el-container style="height: 500px; border: 1px solid #eee">
        <el-container>
            <el-header style="text-align: right; font-size: 12px">
                <el-dropdown>
                    <i class="el-icon-setting" style="margin-right: 15px"></i>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item>查看</el-dropdown-item>
                        <el-dropdown-item>新增</el-dropdown-item>
                        <el-dropdown-item>删除</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
                <span>王小虎</span>
            </el-header>

            <el-main>
                <!--<el-table :data="tableData">-->
                <!--  <el-table-column prop="date" label="日期" width="140">-->
                <!--  </el-table-column>-->
                <!--  <el-table-column prop="name" label="姓名" width="120">-->
                <!--  </el-table-column>-->
                <!--  <el-table-column prop="address" label="地址">-->
                <!--  </el-table-column>-->
                <!--</el-table>-->
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>

</template>

<script>
    export default {
        name: "index"
    }
</script>

<style scoped>

</style>