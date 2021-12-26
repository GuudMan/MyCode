<%@ page import="com.pn.pojo.Teacher" %><%--
  Created by IntelliJ IDEA.
  User: pn
  Date: 2021/12/26
  Time: 9:30
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>

  <script src="layui/layui.js"></script>
  <script src="./js/jquery-3.5.1.min.js"></script>
  <title>教师打分</title>
  <link rel="stylesheet" href="layui/css/layui.css" media="all">

  <%
    Teacher teacher = (Teacher) session.getAttribute("teacher");
    String teacherId = teacher.getTeacherId();

  %>
</head>
<body>
<table id="demo" lay-filter="test"></table>

<script>
  layui.use('table', function () {
    var table = layui.table;

    //第一个实例
    table.render({
      elem: '#demo'
      , height: 'full-10'
      , url: 'SelectStudentByTeacherId?teacherId='+<%=teacherId%>
      , method: 'post'
      , page: true //开启分页
      , cols: [[ //表头
        {field: 'studentId', title: '学号', width: 80, sort: true}
        , {field: 'name', title: '用户名', width: 120}
        , {field: 'sex', title: '性别', width: 80, sort: true}
        , {field: 'age', title: '年龄', width: 80}
        , {field: 'titelId', title: '选题', width: 180}
        , {field: 'teacherId', title: '教师编号', width: 100, sort: true}
        , {field: 'grade', title: '分数', width: 100, sort: true}
        , {field: 'clazz', title: '班级', width: 100, sort: true}
        , {field: 'right', title: '操作', width: 160, toolbar: '#barDemo'}
      ]]
    });
    // 监听行事件

    //监听行工具事件
    table.on('tool(test)', function (obj) {
      var data = obj.data;
      //console.log(obj)
      if (obj.event === 'score') {
        // 实现编辑的功能
        layer.open({  // 打开弹出层
          type: 2 // 2表示自定义弹出 1表示layui弹出层
          , title: '编辑学生信息'
          , content: 'ScoreStudent.html'
          , maxmin: true
          , area: ['500px', '600px']
          , btn: ['确定', '取消']
          , yes: function (index, layero) {
            // 得到回调的数值
            var studentId = $(layero).find('iframe')[0].contentWindow.studentId.value;
            var name = $(layero).find('iframe')[0].contentWindow.document.getElementById('name').value;
            var sex = $(layero).find('iframe')[0].contentWindow.document.getElementById('sex').value;
            var age = $(layero).find('iframe')[0].contentWindow.document.getElementById('age').value;
            var titleId = $(layero).find('iframe')[0].contentWindow.document.getElementById('titleId').value;
            var teacherId = $(layero).find('iframe')[0].contentWindow.document.getElementById('teacherId').value;
            var grade = $(layero).find('iframe')[0].contentWindow.document.getElementById('grade').value;
            var clazz = $(layero).find('iframe')[0].contentWindow.document.getElementById('clazz').value;

            // 同步数据表格中的数据
            obj.update({
              'studentId': studentId,
              'name': name,
              'sex': sex,
              'age': age,
              'titleId': titleId,
              'teacherId': teacherId,
              'grade': grade,
              'clazz': clazz

            })
            $.ajax({
              url: 'EditStudent?studentId=' + studentId + "&name=" + name + "&sex=" + sex + "&age=" + age + "&titleId=" + titleId + "&teacherId=" + teacherId + "&grade=" + grade + "&clazz=" + clazz,
              type: 'post',
              contentType: 'application/json;charset=utf-8',
              dataType: 'text',
              data: {
                'studentId': studentId,
                'name': name,
                'sex': sex,
                'age': age,
                'titleId': titleId,
                'teacherId': teacherId,
                'grade':grade,
                'clazz':clazz
              }
              , success: function (res) {
                layer.msg("编辑成功")
              },
              error: function (res) {
                layer.msg("编辑失败")
              }
            });
            layer.close(index); // 关闭弹出层
          }
          , success: function (layero, index) {
            var div = layero.find('iframe').contents().find("#useradminstudent");
            //  得到回调的数值
            var body = layer.getChildFrame('body', index);
            var iframeWindow = Window['layui-layer-iframe' + index];
            body.find('#studentId').val(data.studentId);// 将每个格中填充初始数据
            body.find('#name').val(data.name);
            body.find('#sex').val(data.sex);
            body.find('#age').val(data.age);
            body.find('#titleId').val(data.titleId);
            body.find('#teacherId').val(data.teacherId);
            body.find('#grade').val(data.grade);
            body.find('#clazz').val(data.clazz);
          }
        });
      }
    });


  });
</script>

<script type="text/html" id="barDemo">
  <a class="layui-btn layui-btn-xs" lay-event="score">打分</a>
</script>
</body>
</html>
