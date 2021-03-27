import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;


/**
 * 重定向
 */

@WebServlet("/ResponseServlet2")
public class ResponseServlet2 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        // 获取流之前设置流的字符集编码ISO-8859-1设置为GBK,但是有时候不知道浏览器的默认字符集
        //response.setCharacterEncoding("gbk"); // 有了下面的，就不需要这一句

        // 告诉浏览器：服务器发送的消息体数据的编码，建议浏览器使用该编码解码 Context-Type
        response.setHeader("content-type", "text/html;charset=utf-8");

        // 更为简单的形式设置编码
        response.setContentType("text/html;charset=utf-8");

        // 获取字符输出流
        PrintWriter writer = response.getWriter();

        // 输出数据
        writer.write("<h1>你好 response</h1>");

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }
}
