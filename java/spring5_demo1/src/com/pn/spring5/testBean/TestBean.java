package com.pn.spring5.testBean;

import com.pn.spring5.bean.Emp;
import com.pn.spring5.service.UserService;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestBean {
    @Test
    public void testBean(){
        // 加载配置文件
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean2.xml");

        // 获取配置创建的对象
        UserService userSerice = context.getBean("userService",UserService.class);
        userSerice.add();
    }
@Test
    public void testBean1(){
    // 加载配置文件
    ApplicationContext context =
            new ClassPathXmlApplicationContext("bean4.xml");

    // 获取配置创建的对象
    Emp emp = context.getBean("emp",Emp.class);
    emp.add();
}
}
