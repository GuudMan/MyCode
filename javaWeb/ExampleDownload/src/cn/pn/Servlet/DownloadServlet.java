package cn.pn.Servlet;

import cn.pn.utils.DownLoadUtils;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.FileInputStream;
import java.io.IOException;

@WebServlet("/DownloadServlet")
public class DownloadServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        // 获取请求参数
        String filename = request.getParameter("filename");

        // 使用字节输出流将文件加载至内存
        //找到文件服务器真实路径
        ServletContext context = this.getServletContext();
        String path = context.getRealPath("/img/" + filename);
        // 使用字节流关联
        FileInputStream inputStream = new FileInputStream(path);
        // 设置response的响应头

        // 设置响应头content-type
        String mimeType = context.getMimeType(filename);// 获取文件的mime文件类型

        response.setHeader("content-type",mimeType);
        // 设置响应打开方式content-disposition

        // 解决中文名的问题
        // 获取user-agent请求头
        String header = request.getHeader("user-agent");
        // 使用工具类方法编码文件名即可
        filename = DownLoadUtils.getFileName(header, filename);

        response.setHeader("content-disposition","attachment;filename=" + filename);
        // 输入流的数据写入到输出流
        ServletOutputStream outputStream = response.getOutputStream();
        byte[] bytes = new byte[1024*8];
        int len = 0;
        while (inputStream.read() != -1){
            outputStream.write(bytes,0,len);
        }
        // 字节流不用刷新
        //输出流不用关闭，只需关闭输入流
        inputStream.close();
        // 完毕
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }
}
