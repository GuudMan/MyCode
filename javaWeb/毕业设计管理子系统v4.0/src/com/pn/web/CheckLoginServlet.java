package com.pn.web;

import com.pn.dao.UserDao;
import com.pn.pojo.Admin;
import com.pn.pojo.Student;
import com.pn.pojo.Teacher;
import com.pn.service.LoginService;
import com.pn.service.LoginServiceImpl;
import org.springframework.beans.BeanUtils;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.util.Map;

@WebServlet("/CheckLoginServlet")
public class CheckLoginServlet extends HttpServlet {
	private static final long serialVersionUID=1L;
	private final LoginService loginService = new LoginServiceImpl();

	public CheckLoginServlet(){
		super();
	}

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//1.设置编码
		request.setCharacterEncoding("utf-8");

		// 获取请求参数
		String name = request.getParameter("name");
		String password = request.getParameter("password");
		String entity = request.getParameter("entity");

		if(entity.equals("管理员")){
			// 获取前端的数据得到的管理员
			Admin loginAdmin  = new Admin();
			loginAdmin.setName(name);
			loginAdmin.setPassword(password);
			//	通过数据库查询到的管理员
			//LoginService loginService = new LoginServiceImpl();
			Admin admin = loginService.selectAllAdmin(loginAdmin);
			//	 判断admin
			if(admin == null){
				response.getWriter().write("fail");
			}else {
				HttpSession session = request.getSession();
				session.setAttribute("admin", admin);
				response.getWriter().write("success");
			}
		}else if(entity.equals("学生")){
			Student studentLogin = new Student();
			studentLogin.setName(name);
			studentLogin.setPassword(password);
			Student student = loginService.selectAllStudent(studentLogin);
			//	 判断admin
			if(student == null){
				response.getWriter().write("fail");
			}else {
				HttpSession session = request.getSession();
				session.setAttribute("student", student);
				response.getWriter().write("success");
			}

		} else if(entity.equals("教师")){
			Teacher teacherLogin = new Teacher();
			teacherLogin.setTname(name);
			teacherLogin.setPassword(password);
			Teacher teacher = loginService.selectAllTeacher(teacherLogin);
			//	 判断admin
			if(teacher == null){
				response.getWriter().write("fail");
			}else {
				HttpSession session = request.getSession();
				session.setAttribute("teacher", teacher);
				response.getWriter().write("success");
			}
		} else{
			response.getWriter().write("fail");
		}

	}
}
