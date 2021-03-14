package pn.test.javaweb.jsoup;


import com.sun.scenario.effect.impl.sw.sse.SSEBlend_SRC_OUTPeer;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.junit.Test;
import sun.awt.geom.AreaOp;


import java.io.File;
import java.io.IOException;
import java.io.PrintStream;
import java.net.MalformedURLException;
import java.net.URL;

/*jsoup入门*/
public class JsoupDemo1 {
    public static void main(String[] args) throws IOException {
        // 获取domcument对象，根据xml文档获取
        //获取student.xml的路径.通过类加载器，获取资源
        String path = JsoupDemo1.class.getClassLoader().getResource(
                "student.xml").getPath();
        System.out.println(path);
        // 解析xml文档，加载文件进内存，获取dom树---->Domcument
        Document document = Jsoup.parse(new File(path), "utf-8");
//        System.out.print(document);
        // 获取元素对象Element
        Elements elements = document.getElementsByTag("name");//Elements继承了ArrayList集合来看

        System.out.println(elements.size());
        // 获取第一个name的element对象
        Element element1 = elements.get(0);
        //获取数据
        String text = element1.text();
        System.out.print(text);

    }


    // 方法2
    @Test
    public void jsoupTest() throws IOException {
        // 获取domcument对象，根据xml文档获取
        //获取student.xml的路径.通过类加载器，获取资源
        String path = JsoupDemo1.class.getClassLoader().getResource(
                "student.xml").getPath();
        System.out.println(path);
        // 解析xml文档，加载文件进内存，获取dom树---->Domcument
        Document document = Jsoup.parse(new File(path), "utf-8");
        String str = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n" +
                "\n" +
                "<students>\n" +
                "\t<student number=\"0001\">\n" +
                "\t\t<name id=\"itcast\">java</name>\n" +
                "\t\t<age>18</age>\n" +
                "\t\t<sex>male</sex>\n" +
                "\t</student>\n" +
                "\t<student number=\"0002\">\n" +
                "\t\t<name>jack</name>\n" +
                "\t\t<age>18</age>\n" +
                "\t\t<sex>female</sex>\n" +
                "\t</student>\n" +
                "\n" +
                "</students>";
        Document document1 = Jsoup.parse(str);
        System.out.print(document1);

    }

    // 方法三：解析网络资源
    @Test
    public void JsoupURL() throws IOException {
        // 获取资源路径
        String path = JsoupDemo1.class.getClassLoader().getResource("student.xml").getPath();

        // 解析资源
            // 获取url(url:统一资源定位符)
        URL url = new URL("https://www.jianshu.com/p/0ec77136ec48");
        Document parse = Jsoup.parse(url, 12000);
        System.out.print(parse);
    }

    @Test
    // Domcument对象
    public void JsoupDocument() throws IOException {
        // 获取资源路径
        String path = JsoupDemo1.class.getClassLoader().getResource("student.xml").getPath();
        // 获取document
        Document document = Jsoup.parse(new File(path), "utf-8");
        // 获取元素对象
            //获取所有student对象
        Elements elements = document.getElementsByTag("student");
        System.out.println(elements);

        System.out.println("-----------");

        // 获取属性名为id的属性对象
        Element itcast = document.getElementById("itcast");
        System.out.println(itcast);
        System.out.println("----------gf---------");
        // 获取number属性值为001的对象
        Elements attributeValue = document.getElementsByAttributeValue("number", "0001");
        System.out.println(attributeValue);

    }

}
