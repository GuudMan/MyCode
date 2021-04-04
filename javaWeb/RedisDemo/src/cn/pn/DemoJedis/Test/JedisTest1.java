package cn.pn.DemoJedis.Test;
/*
** java1.8
** _*_coding:utf-8 _*_
**  @Time        :2021年4月3日10:56:31
** @Author      :彭能
**  @Email       :2663017379@qq.com
**  @Name        :
**  @Software    :IntelliJ IDEA 2019.3.3 x64
**  @Description :jedis快速入门
 */

import cn.pn.DemoJedis.util.JedisPoolUtil;
import org.junit.Test;
import redis.clients.jedis.Jedis;

// 测试jedis连接池工具类
public class JedisTest1 {
    @Test
    public void test1() {

        // 通过连接池工具类来获取
        Jedis jedis = JedisPoolUtil.getJedis();

        // 使用
        jedis.set("pn", "hello");

        // 关闭，归还到连接池中
        jedis.close();

    }
}
