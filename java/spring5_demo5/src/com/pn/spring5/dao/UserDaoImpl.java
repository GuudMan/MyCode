package com.pn.spring5.dao;

import com.pn.spring5.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.Arrays;
import java.util.List;

@Repository
public class UserDaoImpl implements UserDao {

    // 注入jdbcTemplate
    @Autowired
    private JdbcTemplate jdbcTemplate;

    // 添加方法
    @Override
    public void add(User user) {
        String sql = "insert into user values(?,?,?)";

        int i = jdbcTemplate.update(sql, user.getUserId(), user.getUserName(), user.getUstatus());
        System.out.println(i);
    }

    @Override
    public void update(User user) {
        String sql = "update user set username=?,ustatus=? where userId=?";
        int update = jdbcTemplate.update(sql, user.getUserName(), user.getUstatus(), user.getUserId());
        System.out.println(update);
    }

    @Override
    public void delete(int id) {
        String sql = "delete from user where userId=?";
        int update = jdbcTemplate.update(sql, id);
        System.out.println(update);

    }

    @Override
    public int selectCount() {
        String sql = "select count(*) from user";
        Integer integer = jdbcTemplate.queryForObject(sql, Integer.class);
        return integer;
    }

    @Override
    public User selectOb(String id) {
        String sql = "select * from user where userId=?";
        User user = jdbcTemplate.queryForObject(sql,new BeanPropertyRowMapper<>(User.class),id);

        return user;
    }

    @Override
    public List<User> selectAllOb() {

        String sql = "select * from user";
        List<User> query = jdbcTemplate.query(sql, new BeanPropertyRowMapper<>(User.class));
        return query;
    }

    // 批量添加
    @Override
    public void batchAddUser(List<Object[]> batchArg) {
        String sql = "insert into user values(?,?,?)";

        int[] ints = jdbcTemplate.batchUpdate(sql,batchArg);
        System.out.println(Arrays.toString(ints));
    }

    // 批量修改
    @Override
    public void batchUpdateUser(List<Object[]> batchArg) {
        String sql = "update user set username=?,ustatus=? where userId=?";
        int[] ints = jdbcTemplate.batchUpdate(sql,batchArg);
        System.out.println(Arrays.toString(ints));
    }

    // 批量删除
    @Override
    public void batchDeleteUser(List<Object[]> batchArg) {
        String sql = "delete from user where userId=?";
        int[] ints = jdbcTemplate.batchUpdate(sql, batchArg);
        System.out.println(Arrays.toString(ints));
    }


}
