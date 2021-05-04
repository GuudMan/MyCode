package com.pn.spring5.bean;

public class Order {

    private String oName;

    public Order() {
        // 无参构造
        System.out.println("第一步:执行无参数构造bean实例");
    }

    public void setoName(String oName) {
        this.oName = oName;
        System.out.println("第二步： 调用set方法，设置属性值");
    }

    // 创建执行的初始化方法
    public void initMethod(){
        System.out.println("第三步：执行初始化方法");
    }

    // 销毁方法
    public void destoryMethod(){
        System.out.println("第五步：销毁的方法");
    }
}
