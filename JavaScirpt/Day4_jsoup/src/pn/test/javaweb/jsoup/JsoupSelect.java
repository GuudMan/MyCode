package pn.test.javaweb.jsoup;


import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.io.PrintStream;

// Jsoup选择器
public class JsoupSelect {
    // 方法1 ： 传统的方法；一步一步获取
    public static void main(String[] args) throws IOException {
        // 获取资源路径
        String path = JsoupSelect.class.getClassLoader().getResource("student.xml").getPath();
        // 获取document
        Document document = Jsoup.parse(new File(path), "utf-8");
        // 获取student标签
        Elements student = document.getElementsByTag("student");
        // 获取student中的第一个
        Element element = student.get(0);
        // 获取name标签
        Elements name = element.getElementsByTag("name");
        System.out.println(name);
        //获取文本内容
        String text = name.text();
        System.out.println(text);
    }

    // 方法2； 快速获取
    @Test
    public void jsoupSelect() throws IOException {
        // 获取资源路径
        String path = JsoupSelect.class.getClassLoader().getResource("student.xml").getPath();
        // 获取document
        Document document = Jsoup.parse(new File(path), "utf-8");
        // 查询name标签
        Elements elements = document.select("name");
        System.out.println("------------");
        // 查询id值为itcast的元素
        Elements elements1 = document.select("#itcast");
        System.out.println(elements1);
        System.out.println("------------");
        System.out.println(elements1.text());
        System.out.println("------------");
        //获取student标签并且number属性值为0001的age子标签
        Elements elements2 = document.select("student[numbe=\"fd0001\"]");
        System.out.println(elements2);
        // 获取子标签
        System.out.println("------------");
        Elements elements3 = document.select("student[numbe=\"fd0001\"] > age");
        System.out.println(elements3);

    }
}
