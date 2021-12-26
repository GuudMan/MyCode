<%@ page import="com.pn.pojo.Teacher" %><%--
  Created by IntelliJ IDEA.
  User: pn
  Date: 2021/12/25
  Time: 21:31
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <script src="layui/layui.js"></script>
    <script src="./js/jquery-3.5.1.min.js"></script>
    <title>创建选题</title>
    <link rel="stylesheet" href="layui/css/layui.css" media="all">

    <%
        Teacher teacher = (Teacher) session.getAttribute("teacher");
        String teacherId = teacher.getTeacherId();

    %>

</head>
<body>
<label>工号：</label>
<input type="text" id="teacherId" value=<%=teacherId%> readonly="readonly">
<br>
<br>

<label>题目类型：</label>
<input type="text" id="type" value="">
<br>
<br>

<label>题目名称：</label>
<input type="text" id="name" value="">
<br>
<br>
<label>相关文档：</label>
<div class="layui-upload">
    <button type="button" class="layui-btn layui-btn-normal" id="testList">选择多文件</button>
    <div class="layui-upload-list">
        <table class="layui-table">
            <thead>
            <tr>
                <th>文件名</th>
                <th>大小</th>
                <th>状态</th>
                <th>操作</th>
            </tr>
            </thead>
            <tbody id="demoList"></tbody>
        </table>
    </div>
    <button type="button" class="layui-btn" id="testListAction">开始上传</button>
</div>

<br>
<br>

<input type="submit" id="submit" onclick="addTitle()">

<script type="text/javascript"        >
    layui.use('upload', function () {
        var $ = layui.jquery
            , upload = layui.upload;
        var demoListView = $('#demoList')
            , uploadListIns = upload.render({
            elem: '#testList'
            , url: 'UploadServlet' //改成您自己的上传接口
            , accept: 'file'
            , multiple: true
            , auto: false
            , bindAction: '#testListAction'
            , choose: function (obj) {
                var files = this.files = obj.pushFile(); //将每次选择的文件追加到文件队列
                //读取本地文件
                obj.preview(function (index, file, result) {
                    var tr = $(['<tr id="upload-' + index + '">'
                        , '<td>' + file.name + '</td>'
                        , '<td>' + (file.size / 1024).toFixed(1) + 'kb</td>'
                        , '<td>等待上传</td>'
                        , '<td>'
                        , '<button class="layui-btn layui-btn-xs demo-reload layui-hide">重传</button>'
                        , '<button class="layui-btn layui-btn-xs layui-btn-danger demo-delete">删除</button>'
                        , '</td>'
                        , '</tr>'].join(''));

                    //单个重传
                    tr.find('.demo-reload').on('click', function () {
                        obj.upload(index, file);
                    });

                    //删除
                    tr.find('.demo-delete').on('click', function () {
                        delete files[index]; //删除对应的文件
                        tr.remove();
                        uploadListIns.config.elem.next()[0].value = ''; //清空 input file 值，以免删除后出现同名文件不可选
                    });

                    demoListView.append(tr);
                });
            }
            , done: function (res, index, upload) {
                if (res.files.file) { //上传成功
                    var tr = demoListView.find('tr#upload-' + index)
                        , tds = tr.children();
                    tds.eq(2).html('<span style="color: #5FB878;">上传成功</span>');
                    tds.eq(3).html(''); //清空操作
                    return delete this.files[index]; //删除文件队列已经上传成功的文件
                }
                this.error(index, upload);
            }
            , error: function (index, upload) {
                var tr = demoListView.find('tr#upload-' + index)
                    , tds = tr.children();
                tds.eq(2).html('<span style="color: #FF5722;">上传失败</span>');
                tds.eq(3).find('.demo-reload').removeClass('layui-hide'); //显示重传
            }
        });

    });
</script>

<script type="text/javascript">
    function addTitle() {
        var teacherId = $('#teacherId').val();
        var name = $('#name').val();
        var type = $('#type').val();

        $.ajax({
            url: 'AddTitle',
            type:'post',
            data:{
                'teacherId':teacherId,
                'name': name,
                'type':type
            },
            success: function (res) {
                alert("添加成功")
            },
            error:function (res) {
                alert("添加失败")
            }
        });

    }
</script>

</body>
</html>
