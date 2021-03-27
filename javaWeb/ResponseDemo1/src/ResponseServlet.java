import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;


/**
 * 重定向
 */

@WebServlet("/ResponseServlet")
public class ResponseServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("demo1被访问了。。。");
        // 访问这个资源会自动跳转到另外的资源
        // 1. 设置状态码为302
        //response.setStatus(302); //用下面的方法
        // // 2. 设置响应头location
        // response.setHeader("location", "/ResponseServlet1"); // 用下面的方法

        // 动态获取虚拟目录
        String contextPath = request.getContextPath();

        // 有一种简单的重定向方法
        response.sendRedirect(contextPath+"/ResponseServlet");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }
}
