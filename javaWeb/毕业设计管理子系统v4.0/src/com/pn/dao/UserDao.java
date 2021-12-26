package com.pn.dao;

import com.pn.pojo.*;
import com.pn.utils.JDBCUtils;
import com.sun.org.apache.bcel.internal.generic.NEW;
import org.springframework.dao.DataAccessException;
import org.springframework.dao.EmptyResultDataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class UserDao {
	//声明JDBCTemplate对象共用
	private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

	public Admin selectAllAdmin(Admin adminLogin){

			try {
				//1.编写sql
				String sql = "select * from s_admin where name = ? and password = ?";
				//2.调用query方法
				Admin admin = template.queryForObject(sql,
						new BeanPropertyRowMapper<Admin>(Admin.class),
						adminLogin.getName(), adminLogin.getPassword());
				return admin;
			} catch (EmptyResultDataAccessException e) {
				e.printStackTrace();//记录日志
				return null;
			}
		}

	public Student selectAllStudent(Student studentLogin) {

		//1.编写sql
		String sql = "select * from s_student where name = ? and password = ?";
		try {
			//2.调用query方法
			Student student = template.queryForObject(sql,
					new BeanPropertyRowMapper<Student>(Student.class),
					studentLogin.getName(), studentLogin.getPassword());
			return student;
		} catch (Exception e) {
			//e.printStackTrace();//记录日志
			return null;
		}
	}

	public Teacher selectAllTeacher(Teacher teacherLogin) {

		//1.编写sql
		String sql = "select * from s_teacher where name = ? and password = ?";
		try {
			//2.调用query方法
			Teacher teacher = template.queryForObject(sql,
					new BeanPropertyRowMapper<Teacher>(Teacher.class),
					teacherLogin.getTname(), teacherLogin.getPassword());
			return teacher;
		} catch (EmptyResultDataAccessException e) {
			e.printStackTrace();//记录日志
			return null;
		}
	}

	public Admin selectAllAdmin(String name, String password){
		//1.编写sql
		String sql = "select * from s_admin where name = ? and password = ?";
		try {
			//2.调用query方法
			Admin admin = template.queryForObject(sql,
					new BeanPropertyRowMapper<Admin>(Admin.class),
					name, password);
			return admin;
		} catch (EmptyResultDataAccessException e) {
			e.printStackTrace();//记录日志
			return null;
		}
	}

	public int addStudent(Student student) throws SQLException {

		JDBCUtils jdbcUtils = new JDBCUtils();
		//1.编写sql
		String sql = "insert into s_student(name, password, studentId) values(?, ?, ?)";
		PreparedStatement preparedStatement = jdbcUtils.getPreparedStatement(sql);
		preparedStatement.setString(1, student.getName());
		preparedStatement.setString(2, student.getPassword());
		preparedStatement.setString(3, student.getStudentId());
		int rs1 = preparedStatement.executeUpdate();

		if(rs1 == 1){
			jdbcUtils.commit();
			String sql2 = "insert into studentInfo(name,studentId) values(?,?)";
			PreparedStatement ps2 = jdbcUtils.getPreparedStatement(sql2);
			ps2.setString(1, student.getName());
			ps2.setString(2, student.getStudentId());
			int rs2 = ps2.executeUpdate();
			if (rs2 == 1) {
				jdbcUtils.commit();
				return 1;
			} else {
				jdbcUtils.connectRollBACK();
				return 0;
			}
		}else {
			jdbcUtils.connectRollBACK(); // 回滚
			return 0;
		}

	}

	public int addTeacher(Teacher teacher) throws SQLException {

		JDBCUtils jdbcUtils = new JDBCUtils();
		//1.编写sql
		String sql = "insert into s_teacher(name, password, teacherId) values(?, ?, ?)";
		PreparedStatement preparedStatement = jdbcUtils.getPreparedStatement(sql);
		preparedStatement.setString(1, teacher.getTname());
		preparedStatement.setString(2, teacher.getPassword());
		preparedStatement.setString(3, teacher.getTeacherId());
		int rs1 = preparedStatement.executeUpdate();

		if(rs1 == 1){
			jdbcUtils.commit();
			String sql2 = "insert into teacherInfo(tname,teacherId) values(?,?)";
			PreparedStatement ps2 = jdbcUtils.getPreparedStatement(sql2);
			ps2.setString(1, teacher.getTname());
			ps2.setString(2, teacher.getTeacherId());
			int rs2 = ps2.executeUpdate();
			if (rs2 == 1) {
				jdbcUtils.commit();
				return 1;
			} else {
				jdbcUtils.connectRollBACK();
				return 0;
			}
		}else {
			jdbcUtils.connectRollBACK(); // 回滚
			return 0;
		}

	}

	public List<Object> selectAllTeacher(String page, String limit) throws SQLException {

		int page1 = Integer.parseInt(page);
		int limit1 = Integer.parseInt(limit);

		JDBCUtils jdbcUtils = new JDBCUtils();

		String sql = "select * from teacherInfo limit ?,?";

		PreparedStatement statement = jdbcUtils.getPreparedStatement(sql);

		statement.setInt(1, (page1 - 1)*limit1);

		statement.setInt(2, limit1);

		ResultSet rs = statement.executeQuery();

		List<Object> list = new ArrayList<>();

		while (rs.next()){
			Teacher teacher = new Teacher();

			teacher.setTeacherId(rs.getString("teacherId"));
			teacher.setTname(rs.getString("tname"));
			teacher.setTsex(rs.getString("tsex"));
			teacher.setTage(rs.getInt("tage"));
			teacher.setTdept(rs.getString("tdept"));
			teacher.setTel(rs.getString("tel"));
			teacher.setQQ(rs.getString("QQ"));
			teacher.setPrefessional(rs.getString("prefessional"));
			list.add(teacher);
		}
		return list;
	}


	public List<Object> selectAllStudent(String page, String limit) throws SQLException {

		int page1 = Integer.parseInt(page);
		int limit1 = Integer.parseInt(limit);

		JDBCUtils jdbcUtils = new JDBCUtils();

		String sql = "select * from studentInfo limit ?,?";

		PreparedStatement statement = jdbcUtils.getPreparedStatement(sql);

		statement.setInt(1, (page1 - 1)*limit1);

		statement.setInt(2, limit1);

		ResultSet rs = statement.executeQuery();

		List<Object> list = new ArrayList<>();

		while (rs.next()){
			Student student = new Student();

			student.setStudentId(rs.getString("studentId"));
			student.setName(rs.getString("name"));
			student.setSex(rs.getString("sex"));
			student.setAge(rs.getInt("age"));
			student.setTitleId(rs.getInt("titleId"));
			student.setTeacherId(rs.getString("teacherId"));
			list.add(student);
		}
		return list;
	}


	public int countTeacher() throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "select count(*) as numTeacher from teacherinfo";
		Statement statement = jdbcUtils.getStatement();
		ResultSet rs = statement.executeQuery(sql);
		while (rs.next()){
			return rs.getInt("numTeacher");
		}
		return 0;
	}

	public int delTeacherByid(TeacherInfo teacherInfo) throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "delete from teacherinfo where teacherId = ?";
		PreparedStatement pstmt = jdbcUtils.getPreparedStatement(sql);
		pstmt.setString(1, teacherInfo.getTeacherId());
		int result = pstmt.executeUpdate();
		if(result == 1){
			jdbcUtils.commit();
			return 0;
		}else {
			jdbcUtils.connectRollBACK();
			return 1;
		}
	}

	public int delStudentByid(StudentInfo studentInfo) throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "delete from studentinfo where studentId = ?";
		PreparedStatement pstmt = jdbcUtils.getPreparedStatement(sql);
		pstmt.setString(1, studentInfo.getStudentId());
		int result = pstmt.executeUpdate();
		if(result == 1){
			jdbcUtils.commit();
			return 0;
		}else {
			jdbcUtils.connectRollBACK();
			return 1;
		}
	}

	public int addStudentAdmin(Student student) throws SQLException {

		JDBCUtils jdbcUtils = new JDBCUtils();
		//1.编写sql
		String sql = "insert into s_student(name, password, studentId) values(?, ?,?)";
		PreparedStatement preparedStatement = jdbcUtils.getPreparedStatement(sql);
		preparedStatement.setString(1, student.getName());
		preparedStatement.setString(2, student.getPassword());
		preparedStatement.setString(3, student.getStudentId());
		int rs1 = preparedStatement.executeUpdate();

		if(rs1 == 1){
			jdbcUtils.commit();
			String sql2 = "insert into studentInfo(name,studentId) values(?,?)";
			PreparedStatement ps2 = jdbcUtils.getPreparedStatement(sql2);
			ps2.setString(1, student.getName());
			ps2.setString(2, student.getStudentId());
			int rs2 = ps2.executeUpdate();
			if (rs2 == 1) {
				jdbcUtils.commit();
				return 1;
			} else {
				jdbcUtils.connectRollBACK();
				return 0;
			}
		}else {
			jdbcUtils.connectRollBACK(); // 回滚
			return 0;
		}

	}

	public int addTeacherAdmin(Teacher teacher) throws SQLException {

		JDBCUtils jdbcUtils = new JDBCUtils();
		//1.编写sql
		String sql = "insert into s_teacher(name, password, teacherId) values(?, ?,?)";
		PreparedStatement preparedStatement = jdbcUtils.getPreparedStatement(sql);
		preparedStatement.setString(1, teacher.getTname());
		preparedStatement.setString(2, teacher.getPassword());
		preparedStatement.setString(3, teacher.getTeacherId());
		int rs1 = preparedStatement.executeUpdate();

		if(rs1 == 1){
			jdbcUtils.commit();
			String sql2 = "insert into teacherInfo(teacherId,tname,tsex) values(?,?,?)";
			PreparedStatement ps2 = jdbcUtils.getPreparedStatement(sql2);
			ps2.setString(1, teacher.getTeacherId());
			ps2.setString(2, teacher.getTname());
			ps2.setString(3, teacher.getTsex());
			int rs2 = ps2.executeUpdate();
			if (rs2 == 1) {
				jdbcUtils.commit();
				return 1;
			} else {
				jdbcUtils.connectRollBACK();
				return 0;
			}
		}else {
			jdbcUtils.connectRollBACK(); // 回滚
			return 0;
		}

	}

	public int addTitle(Title title) throws SQLException {

		JDBCUtils jdbcUtils = new JDBCUtils();
		//1.编写sql
		String sql = "insert into titleinfo(name, type, teacherId) values(?, ?,?)";
		PreparedStatement preparedStatement = jdbcUtils.getPreparedStatement(sql);
		preparedStatement.setString(1, title.getName());
		preparedStatement.setString(2, title.getType());
		preparedStatement.setString(3, title.getTeacherId());
		int rs1 = preparedStatement.executeUpdate();
		if(rs1 == 1){
			jdbcUtils.commit();
			return 1;
		}else {
			jdbcUtils.connectRollBACK(); // 回滚
			return 0;
		}

	}


	public List<Object> selectStudentByTeacherId(String pageStr, String limit, String teacherId) throws SQLException {

		int page1 = Integer.parseInt(pageStr);
		int limit1 = Integer.parseInt(limit);

		JDBCUtils jdbcUtils = new JDBCUtils();

		String sql = "select * from studentInfo where teacherId=? limit ?,?";

		PreparedStatement statement = jdbcUtils.getPreparedStatement(sql);
		statement.setString(1, teacherId);
		statement.setInt(2, (page1 - 1)*limit1);
		statement.setInt(3, limit1);

		ResultSet rs = statement.executeQuery();

		List<Object> list = new ArrayList<>();

		while (rs.next()){
			StudentInfo student = new StudentInfo();

			student.setStudentId(rs.getString("studentId"));
			student.setName(rs.getString("name"));
			student.setSex(rs.getString("sex"));
			student.setAge(rs.getInt("age"));
			student.setTitleId(rs.getInt("titleId"));
			student.setTeacherId(rs.getString("teacherId"));
			student.setGrade(rs.getString("grade"));
			student.setClazz(rs.getString("clazz"));

			list.add(student);
		}
		return list;
	}


}
