package com.pn.spring5.test;

import com.pn.spring5.entity.User;
import com.pn.spring5.service.UserService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.awt.print.Book;
import java.util.ArrayList;
import java.util.List;

public class Test {

    @org.junit.Test
    public void testJDBCTemplate(){
        ApplicationContext context = new
                ClassPathXmlApplicationContext("bean1.xml");
        UserService userService = context.getBean("userService", UserService.class);
        // 添加
        // User user = new User();
        // user.setUserId(1);
        // user.setUserName("java");
        // user.setUstatus("a");
        // userService.addUser(user);

        // 修改
        // User user = new User();
        // user.setUserId(1);
        // user.setUserName("sqlmy");
        // user.setUstatus("b");
        // userService.update(user);


        // 修改
        // int id = 1;
        // userService.delete(id);

        // 查询 单参数
        // int count = userService.findCount();
        // System.out.println(count);

        // // 查询 ，返回对象
        // User user = userService.findOb("1");
        // System.out.println(user);

        // // 查询 ，返回集合对象
        // List<User> list = userService.findAllOb();
        // for (User user : list) {
        //     System.out.println(user);
        // }


       //  // 批量添加
       //  List<Object[]> batchArgs = new ArrayList<>();
       //  Object[] o1 = {"30","sdfs","sdfs"};
       //  Object[] o2 = {"40","df","ert"};
       //  Object[] o3 = {"52","wre","ytrt"};
       //  batchArgs.add(o1);
       //  batchArgs.add(o2);
       //  batchArgs.add(o3);
       //  // 调用批量添加方法
       // userService.batchAdd(batchArgs);


        //  // 批量修改，注意顺序
        //  List<Object[]> batchArgs = new ArrayList<>();
        //  Object[] o1 = {"java","python","30"};
        //  Object[] o2 = {"c++","c","40"};
        //  Object[] o3 = {"scala","Rubby","50"};
        //  batchArgs.add(o1);
        //  batchArgs.add(o2);
        //  batchArgs.add(o3);
        //  // 调用批量添加方法
        // userService.batchUpdate(batchArgs);

        // 批量删除
        List<Object[]> batchArgs = new ArrayList<>();
        Object[] o1 = {"30"};
        Object[] o2 = {"40"};
        Object[] o3 = {"52"};
        batchArgs.add(o1);
        batchArgs.add(o2);
        batchArgs.add(o3);
        // 调用批量添加方法
        userService.batchDelete(batchArgs);

    }



}
