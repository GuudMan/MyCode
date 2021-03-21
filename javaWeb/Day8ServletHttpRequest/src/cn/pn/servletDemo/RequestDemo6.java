package cn.pn.servletDemo;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.BufferedReader;
import java.io.IOException;

@WebServlet("/RequestDemo6")
public class RequestDemo6 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        // 获取参数前设置流的字符集编码
        request.setCharacterEncoding("utf-8");

        // GET  获取请求消息体
        String username = request.getParameter("username");
//        System.out.println("post");
        System.out.println(username);
        // 获取参数名称的数组
        String[] hobbies = request.getParameterValues("hobby");
        for(String i :hobbies){
            System.out.println(i);
        }
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // post  获取请求消息体
        this.doPost(request, response);
    }
}
