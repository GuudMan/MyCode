package com.pn.web;

import com.pn.dao.UserDao;
import com.pn.pojo.Student;
import com.pn.pojo.Title;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "AddTitle", value = "/AddTitle")
public class AddTitle extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	    doPost(request, response);
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //指定request请求时的字符编码格式
        request.setCharacterEncoding("UTF-8");
        //设置response响应的字符编码格式
        response.setCharacterEncoding("UTF-8");
        //设置响应内容类型为 text/html(文本/超文本标记语言);文本编码为UTF-8
        response.setContentType("text/html'charset=UTF-8");

        String teacherId = request.getParameter("teacherId");
        String name = request.getParameter("name");
        String type = request.getParameter("type");

        Title title = new Title();
        title.setTeacherId(teacherId);
        title.setName(name);
        title.setType(type);

		UserDao userDao = new UserDao();
		try {
			int i = userDao.addTitle(title);
			if (i == 1) {
				response.getWriter().write("success");
			} else {
				response.getWriter().write("fail");
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}


	}
}
