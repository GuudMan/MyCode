package com.pn.spring5.TestBean;

import com.pn.spring5.autowire.Emp;
import com.pn.spring5.bean.Order;
import com.pn.spring5.collection.Book;
import com.pn.spring5.collection.Stu;
import com.pn.spring5.factoryBean.MyBean;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestBean {
    @Test
    public void testCollection(){
        // 加载配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean1.xml");
        // 注入属性
        Stu stu = context.getBean("stu", Stu.class);
        stu.test();
    }

    @Test
    public void testCollection2(){
        // 加载配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean2.xml");
        // 注入属性
        Book book1 = context.getBean("book", Book.class);
        Book book2 = context.getBean("book", Book.class);
        System.out.println(book1);
        System.out.println(book2);
    }

    @Test
    public void testCollection3(){
        // 加载配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean3.xml");
        // 注入属性
        MyBean myBean = context.getBean("myBean", MyBean.class);
        System.out.println(myBean);
    }

    @Test
    public void testCollection4(){
        // 加载配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean4.xml");
        // 注入属性
        Order order = context.getBean("order", Order.class);
        System.out.println("第四步：获取创建实例的对象");
        System.out.println(order);
        ((ClassPathXmlApplicationContext) context).close();
    }

    @Test
    public void testCollection5(){
        // 加载配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean5.xml");
        // 注入属性
        Emp emp = context.getBean("emp", Emp.class);
        System.out.println(emp);
    }
}
