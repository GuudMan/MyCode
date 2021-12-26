package com.pn.web;

import com.pn.dao.StudentEditDao;
import com.pn.dao.TeacherEditDao;
import com.pn.pojo.StudentInfo;
import com.pn.pojo.TeacherInfo;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "EditStudent", value = "/EditStudent")
public class EditStudent extends HttpServlet {
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
        String age = request.getParameter("age");
        String titleId = request.getParameter("titleId");
        String teacherId = request.getParameter("teacherId");
		String grade = request.getParameter("grade");
		String clazz = request.getParameter("clazz");

        int tage1 = Integer.parseInt(age);
        int titleId1 = Integer.parseInt(titleId);

		StudentInfo studentInfo = new StudentInfo();
		studentInfo.setStudentId(studentId);
		studentInfo.setName(name);
		studentInfo.setSex(sex);
		studentInfo.setAge(tage1);
		studentInfo.setTitleId(titleId1);
		studentInfo.setTeacherId(teacherId);
		studentInfo.setGrade(grade);
		studentInfo.setClazz(clazz);

		StudentEditDao studentEditDao = new StudentEditDao();
		try {
			int i = studentEditDao.editStudent(studentInfo);

		} catch (SQLException e) {
			e.printStackTrace();
		}


		//     'teacherId': teacherId,
        // 'name': name,
        // 'sex': sex,
        // 'age': age,
        // 'titleId': titleId,
        // 'teacherId': teacherId,
        // 'qQ': qQ,
        // 'prefessional': prefessional
	}
}
