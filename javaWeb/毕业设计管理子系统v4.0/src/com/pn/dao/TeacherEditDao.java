package com.pn.dao;

import com.pn.pojo.TeacherInfo;
import com.pn.utils.JDBCUtils;

import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TeacherEditDao {
	public int editTeacher(TeacherInfo teacher) throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "update teacherinfo set tname=?,tsex=?,tage=?,tdept=?,tel=?,qQ=?,prefessional=? where teacherId=?";
		PreparedStatement ps = jdbcUtils.getPreparedStatement(sql);

		ps.setString(1, teacher.getTname());
		ps.setString(2, teacher.getTsex());
		ps.setInt(3, teacher.getTage());
		ps.setString(4, teacher.getTdept());
		ps.setString(5, teacher.getTel());
		ps.setString(6, teacher.getQq());
		ps.setString(7, teacher.getPrefessional());
		ps.setString(8, teacher.getTeacherId());

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
