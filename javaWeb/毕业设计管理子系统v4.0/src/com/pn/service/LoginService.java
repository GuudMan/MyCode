package com.pn.service;

import com.pn.pojo.Admin;
import com.pn.pojo.Student;
import com.pn.pojo.Teacher;

import java.sql.SQLException;

public interface LoginService {
	 Admin selectAllAdmin(Admin admin);
	 Admin selectAllAdmin(String name, String password);
	 Student selectAllStudent(Student student);
	 Teacher selectAllTeacher(Teacher teacher);

	 int addStudent(Student student) throws SQLException;

	 int addTeacher(Teacher teacher) throws SQLException;
}
