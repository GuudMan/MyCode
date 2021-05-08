package com.pn.spring5.aopano;


import org.springframework.stereotype.Component;

// 被增强的方法
@Component
public class User {
    public void add(){
        System.out.println("add.....");
    }
}
