package com.pn.web;

import com.pn.dao.TitleDao;
import com.pn.dao.UserDao;
import com.pn.pojo.TeacherInfo;
import com.pn.pojo.Title;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet(name = "DelTeacherByid", value = "/DelTeacherByid")
public class SelectTitleById extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String titleId = request.getParameter("id");

		Title title = new Title();
		title.setTeacherId(titleId);

        TitleDao titleDao = new TitleDao();
		try {
			int i = titleDao.selectTitleById(title);
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
