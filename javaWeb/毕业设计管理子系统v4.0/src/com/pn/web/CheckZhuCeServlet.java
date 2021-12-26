package com.pn.web;

import com.pn.pojo.Student;
import com.pn.pojo.Teacher;
import com.pn.service.LoginService;
import com.pn.service.LoginServiceImpl;
import lombok.SneakyThrows;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "CheckZhuCeServlet", value = "/CheckZhuCeServlet")
public class CheckZhuCeServlet extends HttpServlet {
	private final LoginService loginService = new LoginServiceImpl();

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
	}

	@SneakyThrows
	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 获取前端参数
        String name = request.getParameter("name");
        String password = request.getParameter("password");
        String id = request.getParameter("id");
        String entity = request.getParameter("entity");

        if(entity.equals("学生")){
	        Student student = new Student();
	        student.setName(name);
	        student.setPassword(password);
	        student.setStudentId(id);
	        // 若没有查到，则为空
	        Student student1 = loginService.selectAllStudent(student);
	        if(student1 == null){
		        int i = loginService.addStudent(student);
		        if (i == 1) {
			        response.getWriter().write("success");
		        } else {
			        response.getWriter().write("fail");
		        }
	        }else {
	        	response.getWriter().write("fail");
	        }

        }else if(entity.equals("教师")){
	        Teacher teacher = new Teacher();
	        teacher.setTname(name);
	        teacher.setPassword(password);
	        teacher.setTeacherId(id);
	        Teacher teacher1 = loginService.selectAllTeacher(teacher);
	        if(teacher1 == null){
	        	int i = loginService.addTeacher(teacher);
		        if (i == 1) {
			        response.getWriter().write("success");
		        } else {
			        response.getWriter().write("fail");
		        }

	        }else {
	        	response.getWriter().write("fail");
	        }

        }else {
            response.getWriter().write("fail");
        }

	}
}
