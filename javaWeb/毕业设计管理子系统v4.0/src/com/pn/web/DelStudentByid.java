package com.pn.web;

import com.pn.dao.UserDao;
import com.pn.pojo.StudentInfo;
import com.pn.pojo.TeacherInfo;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "DelStudentByid", value = "/DelStudentByid")
public class DelStudentByid extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String studentId = request.getParameter("id");

        StudentInfo studentInfo = new StudentInfo();
        studentInfo.setStudentId(studentId);

        UserDao userDao = new UserDao();
        try {
            int i = userDao.delStudentByid(studentInfo);
            if(i == 0){
                response.getWriter().write("success");
            }else {
                response.getWriter().write("fail");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
	}

	@Override
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
	}
}
