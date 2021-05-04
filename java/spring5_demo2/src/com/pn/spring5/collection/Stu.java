package com.pn.spring5.collection;

import org.junit.Test;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class Stu {
    // 数组类型的属性
    private String[] course;
    // list集合类型的属性
    private List<String> list;
    // map集合类型的属性
    private Map<String,String> map;
    //  课程
    private List<Course> courseList;

    public void setCourseList(List<Course> courseList) {
        this.courseList = courseList;
    }

    public void setCourse(String[] course) {
        this.course = course;
    }

    public void setList(List<String> list) {
        this.list = list;
    }

    public void setMap(Map<String, String> map) {
        this.map = map;
    }

    @Override
    public String toString() {
        return "Stu{" +
                "course=" + Arrays.toString(course) +
                ", list=" + list +
                ", map=" + map +
                ", courseList=" + courseList +
                '}';
    }

    public void test(){
        System.out.println(Arrays.toString(course));
        System.out.println(list);
        System.out.println(map);
        System.out.println(courseList);
    }
}

