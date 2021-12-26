package com.pn.web;

import com.pn.dao.TeacherEditDao;
import com.pn.pojo.Teacher;
import com.pn.pojo.TeacherInfo;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "EditTeacher", value = "/EditTeacher")
public class EditTeacher extends HttpServlet {
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
        String tname = request.getParameter("tname");
        String tsex = request.getParameter("tsex");
        String tage = request.getParameter("tage");
        String tdept = request.getParameter("tdept");
        String tel = request.getParameter("tel");
        String qQ = request.getParameter("qQ");
        String prefessional = request.getParameter("prefessional");

        int tage1 = Integer.parseInt(tage);

		TeacherInfo teacher = new TeacherInfo();
		teacher.setTeacherId(teacherId);
		teacher.setTname(tname);
		teacher.setTsex(tsex);
		teacher.setTage(tage1);
		teacher.setTdept(tdept);
		teacher.setTel(tel);
		teacher.setQq(qQ);
		teacher.setPrefessional(prefessional);

		TeacherEditDao teacherEditDao = new TeacherEditDao();
		try {
			int i = teacherEditDao.editTeacher(teacher);

			if(i == 1){
				response.getWriter().write("success");
			}else {
				response.getWriter().write("fail");
			}

		} catch (SQLException e) {
			e.printStackTrace();
			response.getWriter().write("fail");
		}


		//     'teacherId': teacherId,
        // 'tname': tname,
        // 'tsex': tsex,
        // 'tage': tage,
        // 'tdept': tdept,
        // 'tel': tel,
        // 'qQ': qQ,
        // 'prefessional': prefessional
	}
}
