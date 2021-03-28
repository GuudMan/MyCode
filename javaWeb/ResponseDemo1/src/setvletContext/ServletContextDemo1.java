package setvletContext;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/ServletContextDemo1")
public class ServletContextDemo1 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        /*
        1. 通过request对象获取
             1. request.getSerletContext()
        2. 通过HTTPServlet获取
            1. this.getServletContext()
         */

//        通过request对象获取
        ServletContext context = request.getServletContext();
//        2. 通过HTTPServlet获取
        ServletContext context1 = this.getServletContext();
        System.out.println(context);
        System.out.println(context1);
        System.out.println(context == context1);// 输出true


    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }
}
