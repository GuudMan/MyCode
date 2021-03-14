package pn.test.javaweb.jsoup;

import cn.wanghaomiao.xpath.exception.XpathSyntaxErrorException;
import cn.wanghaomiao.xpath.model.JXDocument;
import cn.wanghaomiao.xpath.model.JXNode;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class XMLXPath {

    @Test
    public void XMLXPath() throws IOException, XpathSyntaxErrorException {
        // 获取资源路径
        String path = JsoupSelect.class.getClassLoader().getResource("student.xml").getPath();
        // 获取document
        Document document = Jsoup.parse(new File(path), "utf-8");
       // 创建JXDocument对象
        JXDocument jxDocument = new JXDocument(document);

        // 结合xpath的语法 查询所有的student标签  //
        List<JXNode> jxNodes = jxDocument.selN("//student");
        for(JXNode jnode:jxNodes){
            System.out.println(jnode);
        }
        System.out.println("-------");
        // 结合xpath的语法 查询所有的student标签的子标签  /
        List<JXNode> jxNodes2 = jxDocument.selN("//student/name");
        for(JXNode jnode:jxNodes2){
            System.out.println(jnode);
        }


        System.out.println("-------");
        // 结合xpath的语法 查询所有的student下带有id属性的标签 [@]
        List<JXNode> jxNodes3 = jxDocument.selN("//student/name[@id]");
        for(JXNode jnode:jxNodes3){
            System.out.println(jnode);
        }


        System.out.println("-------");
        // 结合xpath的语法 查询所有的student下带有id属性的标签 [@],并且id属性为指定值
        List<JXNode> jxNodes4 = jxDocument.selN("//student/name[@id='itcast']");
        for(JXNode jnode:jxNodes4){
            System.out.println(jnode);
        }
    }
}
