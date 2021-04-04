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

import org.junit.Test;
import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

// jedis快速入门
public class JedisTest {
    @Test
    public void test1(){
        // 1. 获取连接,指定ip和端口
        Jedis jedis = new Jedis("localhost",6379);
        // 2. 操作
        jedis.set("username","zhangsan");
        // 3. 释放资源
        jedis.close();
    }

    @Test
    public void test7(){
        // 创建jedis连接池对象
        JedisPool jedisPool = new JedisPool();
        // 获取连接
        Jedis jedis = jedisPool.getResource();
        // 使用
        jedis.set("myname","hahah");
        // 关闭，归还到连接池中
        jedis.close();
    }
}
