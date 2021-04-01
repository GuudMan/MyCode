package cn.pn.sertlvtDemo.test;

import cn.pn.sertlvtDemo.Domain.Person;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.util.Date;

public class JackjsonTest {

    @Test
    // java-json
    public void test1() throws IOException {
        // 创建person对象
        Person p = new Person();
        p.setName("张三");
        p.setAge(23);
        p.setGender("男");
        p.setBirthday(new Date());

        // 创建json
        ObjectMapper mapper = new ObjectMapper();
        String value = mapper.writeValueAsString(p);
        System.out.println(value);
        // 输出：{"name":"张三","age":23,"gender":"男","birthday":1617203858373}
        // 转换
        //  加上该注解后，  @JsonFormat(pattern = "YYYY-MM-DD hh:mm:ss") // 表示格式化该属性，推荐这种方式
        // 输出{"name":"张三","age":23,"gender":"男","birthday":"2021-03-90 03:20:18"}
        /*
        转换方法
            writeValue(参数1，obj)
                File:将obj对象转换为json字符串，并保存到指定的文件中
                Writer:将object对象转化为json字符串，并将json数据填充到字符输出流中
                OutputStream：将object对象转化为json字符串，并将json数据填充到字节输出流中
            writeValueAsString(obj)： 将obj转为json字符串
         */
        // String json = mapper.writeValueAsString(p);
        // System.out.println(json);
        //
        // // 将数据写到D盘下的文件中
        // mapper.writeValue(new File("D:\\1Temp\\1.txt"), p);
    }

}
