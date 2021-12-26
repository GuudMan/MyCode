package com.pn.dao;

import com.alibaba.fastjson.JSONObject;
import com.pn.pojo.Student;
import com.pn.pojo.Title;
import com.pn.pojo.Vo;
import com.pn.utils.JDBCUtils;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class TitleDao {
	public int selectTitleById(Title title) throws SQLException {
		JDBCUtils jdbcUtils  = new JDBCUtils();
		String sql = "select titleId from titleinfo where titleId=?";
		PreparedStatement statement = jdbcUtils.getPreparedStatement(sql);
		statement.setInt(1, title.getTitleId());
		ResultSet resultSet = statement.executeQuery();
		if (resultSet != null){
			return 0;
		}else return 1;
	}

	public List<Object> selectAllTitle(String page, String limit) throws SQLException {
		int page1 = Integer.parseInt(page);
		int limit1 = Integer.parseInt(limit);

		JDBCUtils jdbcUtils = new JDBCUtils();

		String sql = "select * from titleinfo limit ?,?";

		PreparedStatement statement = jdbcUtils.getPreparedStatement(sql);

		statement.setInt(1, (page1 - 1)*limit1);

		statement.setInt(2, limit1);

		ResultSet rs = statement.executeQuery();

		List<Object> list = new ArrayList<>();

		while (rs.next()){
			Title title = new Title();

			title.setTitleId(rs.getInt("titleId"));
			title.setType(rs.getString("type"));
			title.setName(rs.getString("name"));
			title.setTeacherId(rs.getString("teacherId"));
			list.add(title);
		}
		return list;

	}

	public int countTitle() throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "select count(*) as numTitle from titleinfo";
		Statement statement = jdbcUtils.getStatement();
		ResultSet rs = statement.executeQuery(sql);
		while (rs.next()){
			return rs.getInt("numTitle");
		}
		return 0;
	}

	public List<Object> selectTitle(String select) throws SQLException {
		JDBCUtils jdbcUtils = new JDBCUtils();
		String sql = "select * from titleinfo where name like '%"+ select + "%'";
		PreparedStatement statement = jdbcUtils.getPreparedStatement(sql);
		ResultSet resultSet = statement.executeQuery();

		List<Object> listTitle = new ArrayList<>();
		Title title;
		while(resultSet.next()){
			title = new Title();
			title.setTitleId(resultSet.getInt("titleId"));
			title.setType(resultSet.getString("type"));
			title.setName(resultSet.getString("name"));
			title.setTeacherId(resultSet.getString("teacherId"));
			listTitle.add(title);
		}
		return listTitle;
	}
}
