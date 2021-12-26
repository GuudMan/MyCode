package com.pn.dao;

import com.pn.pojo.StudentInfo;
import com.pn.pojo.TeacherInfo;
import com.pn.utils.JDBCUtils;

import java.sql.PreparedStatement;
import java.sql.SQLException;

public class StudentEditDao {
	public int editStudent(StudentInfo studentInfo) throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "update studentinfo set name=?,sex=?,age=?,titleId=?,teacherId=? ,grade=? ,clazz=? where studentId=?";
		PreparedStatement ps = jdbcUtils.getPreparedStatement(sql);

		ps.setString(1, studentInfo.getName());
		ps.setString(2, studentInfo.getSex());
		ps.setInt(3, studentInfo.getAge());
		ps.setInt(4, studentInfo.getTitleId());
		ps.setString(5, studentInfo.getTeacherId());
		ps.setString(6, studentInfo.getGrade());
		ps.setString(7, studentInfo.getClazz());
		ps.setString(8, studentInfo.getStudentId());

		int result = ps.executeUpdate();
		if(result == 1){
			jdbcUtils.commit();
			return 0;
		}else {
			jdbcUtils.connectRollBACK();
			return 1;
		}
	}
}
