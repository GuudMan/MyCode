package com.pn.spring5.collection;

import java.sql.SQLOutput;
import java.util.List;

public class Book {
    private List<String> list;

    // @Override
    // public String toString() {
    //     return "Book{" +
    //             "list=" + list +
    //             '}';
    // }

    public void setList(List<String> list) {
        this.list = list;
    }
    public void add(){
        System.out.println(list);
    }
}
