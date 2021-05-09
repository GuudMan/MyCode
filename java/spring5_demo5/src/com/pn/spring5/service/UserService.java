package com.pn.spring5.service;

import com.pn.spring5.dao.UserDao;
import com.pn.spring5.entity.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {
    // 注入dao
    @Autowired
    private UserDao userDao;

    // 添加方法
    public void addUser(User user){
        userDao.add(user);
    }

    // 修改方法
    public void update(User user){
        userDao.update(user);
    }

    // 删除方法
    public void delete(int id){
        userDao.delete(id);
    }

    // 查询表中的记录数
    public int findCount(){

        return userDao.selectCount();
    }

    // 查询对象
    public User findOb(String id){
        return userDao.selectOb(id);
    }

    // 返回所有对象
    public List<User> findAllOb(){
        return userDao.selectAllOb();
    }

    // 批量添加
    public void batchAdd(List<Object[]> batchArg){
        userDao.batchAddUser(batchArg);
    }

    // 批量修改
    public void batchUpdate(List<Object[]> batchArg){
        userDao.batchUpdateUser(batchArg);
    }

    // 批量删除
    public void batchDelete(List<Object[]> batchArg){
        userDao.batchDeleteUser(batchArg);
    }

}
