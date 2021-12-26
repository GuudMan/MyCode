package com.pn.web;

import com.alibaba.fastjson.JSONObject;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Collection;

@WebServlet("/UploadServlet")
public class UploadServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //指定request请求时的字符编码格式
        request.setCharacterEncoding("UTF-8");
        //设置response响应的字符编码格式
        response.setCharacterEncoding("UTF-8");
        //设置响应内容类型为 text/html(文本/超文本标记语言);文本编码为UTF-8
        response.setContentType("text/html'charset=UTF-8");

        JSONObject json = new JSONObject();
        // 存储路径
        String src = "\\毕业设计管理子系统v4.0\\web\\upload";
        String src2 = "web/upload";
        String savePath = "D:\\1Temp\\project\\javaWeb\\毕业设计管理子系统v4.0\\web\\upload";
        // 获取上传文件集合
        Collection<Part> parts = request.getParts();
        // 上传单个文件
        if (parts.size() == 1) {
            Part part = request.getPart("file");// 通过表单file控件的名字直接获取part对象
            String header = part.getHeader("content-disposition");
            // 获取文件名
            //String fileName = getFileName(header);

            String fileName = header.substring(header.lastIndexOf("=") + 2, header.length() - 1);

            // 把文件写到指定的路径
            part.write(savePath + File.separator + fileName);
            json.put("msg", "上传成功");
            json.put("code", 0);
            json.put("src", src + fileName);
            json.put("src2", src2 + fileName);
        } else {// 一次上传多个文件
            for (Part part : parts) {
                String header = part.getHeader("content-disposition");
                // 获取文件名
                //String fileName = getFileName(header);

                String fileName = header.substring(header.lastIndexOf("=") + 2, header.length() - 1);

                // 把文件写到指定的路径
                part.write(savePath + File.separator + fileName);
                json.put("msg", "上传成功");
                json.put("code", 0);
                json.put("src", src + fileName);
                json.put("src2", src2 + fileName);
            }
        }
        PrintWriter out = response.getWriter();
        out.println(json);
        out.flush();
        out.close();


    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
