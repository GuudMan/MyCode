package cn.web;

import cn.domain.User;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/SuccessServlet")
public class SuccessServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
       //获取req中共享的user对象
        User user = (User) request.getAttribute("user");

        if (user != null){
            //给页面写一句话
            // 设置页面编码
            response.setContentType("text/html,charset = utf-8");
            //输出到页面上
            response.getWriter().write("success，" + user + "welcome");
        }

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }
}
