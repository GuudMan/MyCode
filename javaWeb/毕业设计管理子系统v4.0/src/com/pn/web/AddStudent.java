package com.pn.web;

import com.pn.dao.UserDao;
import com.pn.pojo.Student;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "AddStudent", value = "/AddStudent")
public class AddStudent extends HttpServlet {
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

        String studentId = request.getParameter("studentId");
        String name = request.getParameter("name");
        String sex = request.getParameter("sex");
        String password = request.getParameter("password");

        Student student = new Student();
        student.setStudentId(studentId);
        student.setName(name);
        student.setSex(sex);
        student.setPassword(password);

		UserDao userDao = new UserDao();
		try {
			int i = userDao.addStudentAdmin(student);
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
