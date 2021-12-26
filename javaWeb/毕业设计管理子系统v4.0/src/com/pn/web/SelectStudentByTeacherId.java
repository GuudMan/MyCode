package com.pn.web;

import com.alibaba.fastjson.JSONObject;
import com.pn.dao.UserDao;
import com.pn.pojo.StudentInfo;
import com.pn.pojo.Vo;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

@WebServlet(name = "SelectStudentByTeacherId", value = "/SelectStudentByTeacherId")
public class SelectStudentByTeacherId extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	    doPost(request,response);
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

		String pageStr = request.getParameter("page");
		String limitStr = request.getParameter("limit");

        //StudentInfo studentInfo = new StudentInfo();
        //studentInfo.setTeacherId(teacherId);

        UserDao userDao = new UserDao();
		try {
			List<Object> teacherList = userDao.selectStudentByTeacherId(pageStr, limitStr, teacherId);

			Vo vo = new Vo();
			vo.setCode(0);
			vo.setMsg("success");
			vo.setCount(userDao.countTeacher());
			vo.setData(teacherList);
			response.getWriter().write(JSONObject.toJSON(vo).toString());
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}
}
