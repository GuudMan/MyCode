package pn.test.javaweb.jsoup;


import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.io.PrintStream;

// 获取Element对象的功能
public class JsoupDemo4 {
    public static void main(String[] args) throws IOException {
        // 获取路径
        String path = JsoupDemo4.class.getClassLoader().getResource("student.xml").getPath();
        // 获取docum
        Document document = Jsoup.parse(new File(path), "utf-8");
        Elements name = document.getElementsByTag("name");
        System.out.println(name.size()); // 得到两个
        System.out.println("--------");
        // 获取子元素对象
            // 通过document获取name标签，可以同时获取所有的name标签
        Element element_student = document.getElementsByTag("student").get(0);
        Elements elementsName = element_student.getElementsByTag("name");
        System.out.println(elementsName.size());   // 得到一个
        System.out.println("--------");
        // 获取student的属性值
        String number = element_student.attr("numbe");
        System.out.println(number);


    }
}
