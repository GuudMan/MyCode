package com.pn.spring5.service;

import com.pn.spring5.dao.UserDao;

public class UserService {


    private UserDao userDao;

    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void add(){
        System.out.println("add-------");
        userDao.update();
        // 原始方法：创建UserDao的对象
        // UserDao userDao = new UserDaoImpl();
        // userDao.update();
    }
}
