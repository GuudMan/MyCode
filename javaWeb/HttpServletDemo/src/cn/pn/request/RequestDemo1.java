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
**  @Time        :
** @Author      :彭能
**  @Email       :2663017379@qq.com
**  @Name        :
**  @Software    :IntelliJ IDEA 2019.3.3 x64
**  @Description :request对象获取请求行数据
 */

@WebServlet("/RequestDemo1")
public class RequestDemo1 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        /*
        	1. 获取请求方法GET
               	1. String getMethod()
          	2. 获取虚拟路径 day6 :flags:重点
               	1. String getContextPath()
         	3. 获取Servlet路径：/demo1
             	1. String getSevletPath()
         	4. 获取get方式的请求参数： name=zhangsan
             	1. String getQueryString()
         	5. 获取请求URI：/day6/demo1 :arrow_forward:重点
             	1. String getRequestURI()
             	2. String getRequsetURL(): http://localhost:8080/day6/demo1
         	6. 获取协议版本
             	1. String getProtocol()
         	7. 获取客户机的ip地址
             	1. String getRemoteAddr()
         */
        // 获取请求方式
        String requestMethod = request.getMethod();
        System.out.println(requestMethod);

        // 获取虚拟目录
        String requestContextPath = request.getContextPath();
        System.out.println(requestContextPath);

        // 获取请求参数
        String queryString = request.getQueryString();
        System.out.println(queryString);

        // 获取请求URI
        String requestURI = request.getRequestURI();
        System.out.println(requestURI);

        // 获取版本协议
        String protocol = request.getProtocol();
        System.out.println(protocol);

        // 获取ip地址
        String remoteAddr = request.getRemoteAddr();
        System.out.println(remoteAddr);
    }
}
