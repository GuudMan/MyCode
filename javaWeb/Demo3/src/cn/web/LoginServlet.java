package cn.web;

import cn.dao.UserDao;
import cn.domain.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

//
//@WebServlet("/LoginServlet")
//public class LoginServlet extends HttpServlet {
//    @Override
//    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//
//        //设置编码
//        req.setCharacterEncoding("utf-8");
//        //获取请求参数
//        String username = req.getParameter("username");
//        String password = req.getParameter("password");
//        // 封装user对象
//        User loginUser = new User();
//        loginUser.setUsername(username);
//        loginUser.setPassword(password);
//
//        // 调用UserDao的login方法
//        UserDao userDao = new UserDao();
//        User user = userDao.login(loginUser);// 真正获取的user
//
//        // 判断user
//        if(user == null){
//            System.out.println("登陆失败");
//            // 分发到登陆失败
//            req.getRequestDispatcher("/FailServlet").forward(req,resp);
//        }else {
//            System.out.println("登陆成功");
//            // 分发到登陆成功
//            //存储数据
//            req.setAttribute("user",user);
//            //转发
//            req.getRequestDispatcher("/SuccessServlet").forward(req,resp);
//        }
//
//    }
//
//    @Override
//    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//
//        this.doGet(req,resp);
//    }
//}


@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        System.out.println("开始");
        //1.设置编码
        req.setCharacterEncoding("utf-8");
        //2.获取请求参数
        String username = req.getParameter("username");
        String password = req.getParameter("password");
        //3.封装user对象
        User loginUser = new User();
        loginUser.setUsername(username);
        loginUser.setPassword(password);

        //4.调用UserDao的login方法
        UserDao dao = new UserDao();
        System.out.println("dao");
        User user = dao.login(loginUser);

        //5.判断user
        if(user == null){
            //登录失败
            req.getRequestDispatcher("/FailServlet").forward(req,resp);
        }else{
            //登录成功
            //存储数据
            req.setAttribute("user",user);
            //转发
            req.getRequestDispatcher("/SuccessServlet").forward(req,resp);
        }

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doGet(req,resp);
        System.out.println("no problem");
    }
}

