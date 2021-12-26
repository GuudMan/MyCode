<%--
  Created by IntelliJ IDEA.
  User: pn
  Date: 2021/12/4
  Time: 20:05
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <title>毕业设计管理子系统主界面</title>
    <link rel="stylesheet" href="../../layui/css/layui.css">

</head>
<body>
<div class="layui-layout layui-layout-admin">
    <div class="layui-header">
        <div class="layui-logo">毕业设计管理系统V4.0</div>
        <!-- 头部区域（可配合layui 已有的水平导航） -->
        <ul class="layui-nav layui-layout-left">
            <li class="layui-nav-item"><a href="">nav 1</a></li>
            <li class="layui-nav-item"><a href="">nav 2</a></li>
            <li class="layui-nav-item"><a href="">nav 3</a></li>
            <li class="layui-nav-item">
                <a href="javascript:;">nav groups</a>
                <dl class="layui-nav-child">
                    <dd><a href="">menu 11</a></dd>
                    <dd><a href="">menu 22</a></dd>
                    <dd><a href="">menu 33</a></dd>
                </dl>
            </li>
        </ul>
        <ul class="layui-nav layui-layout-right">
            <li class="layui-nav-item">
                <%--<a href="javascript:;">--%>
                <%--    <img src="//tva1.sinaimg.cn/crop.0.0.118.118.180/5db11ff4gw1e77d3nqrv8j203b03cweg.jpg" class="layui-nav-img">--%>
                <%--    tester--%>
                <%--</a>--%>
                <dl class="layui-nav-child">
                    <dd><a href="">set 1</a></dd>
                    <dd><a href="">set 2</a></dd>
                </dl>
            </li>
            <li class="layui-nav-item"><a href="">Sign out</a></li>
        </ul>
    </div>

    <div class="layui-side layui-bg-black">
        <div class="layui-side-scroll">
            <!-- 左侧导航区域（可配合layui已有的垂直导航） -->
            <ul class="layui-nav layui-nav-tree" lay-filter="test">
                <li class="layui-nav-item layui-nav-itemed">
                    <a class="" href="javascript:;">主要功能</a>
                    <dl class="layui-nav-child">
                        <dd><a href="allstudent.html">学生列表</a></dd>
                        <dd><a href="allteacher.html">教师列表</a></dd>
                        <dd><a href="addStudent.html">添加学生</a></dd>
                        <dd><a href="addTeacher.html">添加教师</a></dd>
                    </dl>
                </li>
                <li class="layui-nav-item">
                    <a href="javascript:;">menu group 2</a>
                    <dl class="layui-nav-child">
                        <dd><a href="javascript:;">list 2-1</a></dd>
                        <dd><a href="javascript:;">list 2-2</a></dd>
                        <dd><a href="">超链接</a></dd>
                    </dl>
                </li>

            </ul>
        </div>
    </div>

    <div class="layui-body">
        <!-- 内容主体区域 -->
        <%--<div style="padding: 15px;">内容主体区域</div>--%>
        <iframe src="" id="main" height="100%" width="100%">
        </iframe>
    </div>

    <div class="layui-footer">
        <!-- 底部固定区域 -->
        底部固定区域
    </div>
</div>

<script src="../../layui/layui.js"></script>
<script>
    //JavaScript代码区域
    layui.use('element', function () {
        var element = layui.element;
        var $ = layui.jquery;
        $(document).ready(function () {
            // dd>a 就是查找dd下的a标签，dd就是主要功能，a就是各种列表
            $("dd > a").click(function (e) {
                e.preventDefault();
                $('#main').attr("src", $(this).attr("href"));
            });
        });

    });
</script>
</body>
</html>
