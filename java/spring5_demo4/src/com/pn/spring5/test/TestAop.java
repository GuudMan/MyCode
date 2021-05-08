package com.pn.spring5.test;

import com.pn.spring5.aopXML.Book;
import com.pn.spring5.aopano.User;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestAop {

    @Test
    public void testAopAno(){
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean2.xml");
        User user = context.getBean("user", User.class);
        user.add();
    }

    @Test
    public void testAOPxml(){
        ApplicationContext context =
                new ClassPathXmlApplicationContext("bean2.xml");
        Book book = context.getBean("book", Book.class);
        book.buy();
    }

}
