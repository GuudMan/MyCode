package com.pn.web;

import com.alibaba.fastjson.JSONObject;
import com.pn.dao.UserDao;
import com.pn.pojo.Vo;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

@WebServlet(name = "SelectAllStudent", value = "/SelectAllStudent")
public class SelectAllStudent extends HttpServlet {
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

		String pageStr = request.getParameter("page");
		String limitStr = request.getParameter("limit");

		UserDao userDao = new UserDao();
		try {
			List<Object> teacherList = userDao.selectAllStudent(pageStr, limitStr);
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
