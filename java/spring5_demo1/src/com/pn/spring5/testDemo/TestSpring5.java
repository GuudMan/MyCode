package com.pn.spring5.testDemo;

import com.pn.spring5.Book;
import com.pn.spring5.Order;
import com.pn.spring5.User;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestSpring5 {

    @Test
    public void testAdd(){
      //1 加载spring配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean1.xml");

      //2 获取配置创建的对象 参数为配置文件中的id
        User user = context.getBean("user", User.class);
        System.out.println(user);
        user.add();
    }

    @Test
    public void testBook1(){
        // 加载配置文件
        ApplicationContext context = new ClassPathXmlApplicationContext("bean1.xml");

        // 获取配置文件中的对象
        Book book = context.getBean("book",Book.class);
        book.testDemo();
    }

    @Test
    public void testOrder(){
        // 加载配置文件
        ApplicationContext context = new ClassPathXmlApplicationContext("bean1.xml");

        // 获取配置文件中的对象
        Order order = context.getBean("order", Order.class);
        order.testContruct();
    }

}
