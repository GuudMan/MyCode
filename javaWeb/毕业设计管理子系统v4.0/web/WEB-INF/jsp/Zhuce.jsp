<%--
  Created by IntelliJ IDEA.
  User: pn
  Date: 2021/11/21
  Time: 12:24
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>登陆界面</title>
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <script src="../../js/jquery-3.5.1.min.js"></script>
    <link rel="stylesheet" href="../../layui/css/layui.css" media="all">
    <link rel="stylesheet" href="../../style/admin.css" media="all">
    <link rel="stylesheet" href="../../style/login.css" media="all">
    <script src="../../js/jquery-3.5.1.min.js"></script>
    <script src="../../layui/layui.js"></script>
</head>
<body>
<div class="layadmin-user-login layadmin-user-display-show" id="LAY-user-login" style="display: none;">
    <div class="layadmin-user-login-main">
        <div class="layui-form-item logo-title">
            <h1>注册新用户页面</h1>
        </div>
        <div class="layui-form-item">
            <label class="layui-icon layui-icon-username" for="LAY-user-login-username"></label>
            <input type="text" name="name" id="name" lay-verify="required" placeholder="请输入用户名" class="layui-input">
        </div>
        <div class="layui-form-item">
            <label class="layui-icon layui-icon-password" for="LAY-user-login-password"></label>
            <input type="password" name="password" id="password" lay-verify="required" placeholder="请输入密码" class="layui-input">
        </div>
        <div class="layui-form-item">
            <label class="layui-icon layui-icon-password" for="LAY-user-login-password"></label>
            <input type="password" name="password_verfy" id="password_verfy" lay-verify="required" placeholder="请确认密码" class="layui-input">
        </div>

        <form action="" class="layui-form">
            <div class="layui-input-iterm">
                <label class="layui-form-label">您的角色</label>
                <input type="radio" name="entity" value="学生" title="学生" checked="">
                <input type="radio" name="entity" value="教师" title="教师">
            </div>
        </form>

        <div class="layui-form-item">
            <label class="layui-icon layui-icon-username" for="LAY-user-login-nickname"></label>
            <input type="text" name="nickname" id="nickname" lay-verify="required" placeholder="请输入学号或工号" class="layui-input">
        </div>

        <div class="layui-form-item">
            <input type="checkbox" name="agreement" lay-skin="primary" title="同意用户协议" checked>同意用户协议
        </div>

        <div class="layui-form-item">
            <button class="layui-btn layui-btn-fluid" lay-submit lay-filter="LAY-user-login-submit" id="zhuce"
                    onclick="zhuce()">注 册
            </button>
        </div>


        <div class="layui-trans layui-form-item layadmin-user-login-other">
            <label>社交账号登入</label>
            <a href="javascript:;"><i class="layui-icon layui-icon-login-qq"></i></a>
            <a href="javascript:;"><i class="layui-icon layui-icon-login-wechat"></i></a>
            <a href="javascript:;"><i class="layui-icon layui-icon-login-weibo"></i></a>
            <a href="LoginServlet" class="layadmin-user-jump-change layadmin-link">已有账号登陆</a>

        </div>
    </div>
</div>

<script src="../../js/jquery-3.5.1.min.js"></script>
<script type="text/javascript">
    function zhuce() {
        var name = $("#name").val();// 获取用户名
        var password = $("#password").val();// 获取密码 password-verfy
        var password_verfy = $("#password_verfy").val();// 获取密码 password-verfy
        var entity = $('input[name="entity"]:checked').val();
        var id =  $("#nickname").val();
        if( password != password_verfy){
            layer.msg("两次密码不一致， 请重新确认密码", {icon: 5})
        }else{
            $.ajax({
                type: 'post',
                url: 'CheckZhuCeServlet',
                data: {
                    'name': name,
                    'password': password,
                    'id': id,
                    'entity': entity
                },
                dataType: 'text',
                success: function (res){
                    if (res == "success"){
                        layer.msg("注册成功",{icon:6});
                        window.location.href = "/LoginServlet";
                    }else {
                        layer.msg('注册失败', {icon: 5});
                    }
                }
            })
        }

    }
</script>

<script>
    // 解决表单无法显示的问题
    layui.use('form', function(){
        var form = layui.form; //只有执行了这一步，部分表单元素才会自动修饰成功
        //……
        //但是，如果你的HTML是动态生成的，自动渲染就会失效
        //因此你需要在相应的地方，执行下述方法来手动渲染，跟这类似的还有 element.init();
        form.render();
    });
</script>

</body>
</html>
