package com.pn.spring5.bean;

// 员工类
public class Emp {
    private String eName;
    private String gender;
    // 部门： 一个员工要属于一个部门
    private Dept dept;

    @Override
    public String toString() {
        return "Emp{" +
                "eName='" + eName + '\'' +
                ", gender='" + gender + '\'' +
                ", dept=" + dept +
                '}';
    }

    public void setDept(Dept dept) {
        this.dept = dept;
    }

    public void seteName(String eName) {
        this.eName = eName;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void add(){
        System.out.println(eName + "::" + gender +"::" + dept);
    }
}
