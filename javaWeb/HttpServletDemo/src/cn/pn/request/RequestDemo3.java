package cn.pn.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/*
** java1.8
** _*_coding:utf-8 _*_
**  @Time        :2021年3月21日11:26:08
** @Author      :彭能
**  @Email       :2663017379@qq.com
**  @Name        :
**  @Software    :IntelliJ IDEA 2019.3.3 x64
**  @Description :演示获取请求头
*/

@WebServlet("/RequestDemo3")
public class RequestDemo3 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 演示获取请求头
        String agent = request.getHeader("user-agent");
        if(agent.contains("Chrome")){
            //判读浏览器类型
            System.out.println("谷歌浏览器");
        }else if(agent.contains("Firefox")){
            // 火狐浏览器
            System.out.println("火狐浏览器");
        }
    }

}

