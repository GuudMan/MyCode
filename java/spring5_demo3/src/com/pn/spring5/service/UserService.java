package com.pn.spring5.service;

import com.pn.spring5.dao.UserDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;


// 注解中value属性值可以默认不写，默认值是类名称，首字母小写 UserService--->userService
// @Component(value = "userService") // <bean id="userService" class=""/>
@Service
public class UserService {

    @Value(value = "abc")
    private String name;

    // 注入dao类型的属性,
    // 不需要添加set方法
    // 添加注入属性注解
    @Autowired
    private UserDao userDao;

    public void add(){
        System.out.println("service add..." + name);
        userDao.add();
    }
}
