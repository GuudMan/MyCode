package com.pn.service;

import com.pn.pojo.Admin;
import com.pn.pojo.Student;
import com.pn.dao.UserDao;
import com.pn.pojo.Teacher;

import java.sql.SQLException;

public class LoginServiceImpl implements LoginService {

	UserDao userDao  = new UserDao();


	@Override
	public Admin selectAllAdmin(Admin admin) {
		return userDao.selectAllAdmin(admin);
	}

	@Override
	public Admin selectAllAdmin(String name, String password) {
		return userDao.selectAllAdmin(name, password);
	}

	@Override
	public Student selectAllStudent(Student student) {
		return userDao.selectAllStudent(student);
	}

	@Override
	public Teacher selectAllTeacher(Teacher teacher) {
		return userDao.selectAllTeacher(teacher);
	}

	@Override
	public int addStudent(Student student) throws SQLException {
		return userDao.addStudent(student);
	}

	@Override
	public int addTeacher(Teacher teacher) throws SQLException {
		return userDao.addTeacher(teacher);
	}
}
