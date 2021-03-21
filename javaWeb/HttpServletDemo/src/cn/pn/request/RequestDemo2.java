package cn.pn.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Enumeration;

/*
** java1.8
** _*_coding:utf-8 _*_
**  @Time        :2021年3月21日11:26:08
** @Author      :彭能
**  @Email       :2663017379@qq.com
**  @Name        :
**  @Software    :IntelliJ IDEA 2019.3.3 x64
**  @Description :演示获取请求头
*
输出
host======localhost:8080
connection======keep-alive
cache-control======max-age=0
sec-ch-ua======"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
sec-ch-ua-mobile======?0
upgrade-insecure-requests======1
user-agent======Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
accept======text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/
//*;q=0.8,application/signed-exchange;v=b3;q=0.9
//        sec-fetch-site======none
//        sec-fetch-mode======navigate
//        sec-fetch-user======?1
//        sec-fetch-dest======document
//        accept-encoding======gzip, deflate, br
//        accept-language======zh-CN,zh;q=0.9
//        cookie======Idea-52c87822=5936fd73-e48d-48dd-b537-039d1a2a7b1f; JSESSIONID=DE2CC24DCFC29E0719983409CAD07293
//
//*/

@WebServlet("/RequestDemo2")
public class RequestDemo2 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 演示获取请求头
        //. 获取所有的请求头
        Enumeration<String> headerNames = request.getHeaderNames();
        while (headerNames.hasMoreElements()){
            String name = headerNames.nextElement();
            // 根据名称获取请求头的值
            String value = request.getHeader(name);
            System.out.println(name + "======" + value);
        }
    }

}

