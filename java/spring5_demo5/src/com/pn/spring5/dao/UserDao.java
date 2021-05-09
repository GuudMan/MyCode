package com.pn.spring5.dao;

import com.pn.spring5.entity.User;

import java.util.List;

public interface UserDao {
    void add(User user);

    void update(User user);

    void delete(int id);

    int selectCount();

    User selectOb(String id);

    List<User> selectAllOb();

    //批量添加
    void batchAddUser(List<Object[]> batchArg);

    void batchUpdateUser(List<Object[]> batchArg);

    void batchDeleteUser(List<Object[]> batchArg);
}
