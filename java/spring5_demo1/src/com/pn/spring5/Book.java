package com.pn.spring5;

public class Book {
    private String bName;
    private String bAuthor;

    // 生成set方法

    public void setbName(String bName) {
        this.bName = bName;
    }

    public void setbAuthor(String bAuthor) {
        this.bAuthor = bAuthor;
    }

    public void testDemo(){
        System.out.println(bName +"::"+ bAuthor);
    }
}
