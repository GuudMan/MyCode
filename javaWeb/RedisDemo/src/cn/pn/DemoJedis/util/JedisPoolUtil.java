package cn.pn.DemoJedis.util;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;
import redis.clients.jedis.JedisPoolConfig;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class JedisPoolUtil {

    private static JedisPool jedisPool;

    // 定义一个静态代码块，读取配置文件
    static{
        // 读取配置文件，使用类加载器
        InputStream is = JedisPoolUtil.class.getClassLoader().getResourceAsStream("jedis.properties");

        // 创建properties对象
        Properties pro = new Properties();
        // 关联文件
        try {
            pro.load(is);
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 获取数据，设置到JedisPoolConfig中,需要件string转为int
        JedisPoolConfig conf = new JedisPoolConfig();
        conf.setMaxTotal(Integer.parseInt(pro.getProperty("maxTotal")));
        conf.setMaxIdle(Integer.parseInt(pro.getProperty("maxIdle")));

        // 初始化JedisPool连接池对象
        jedisPool = new JedisPool(conf,pro.getProperty("host"),Integer.parseInt(pro.getProperty("port")));

    }

    // 获取连接方法
    public static Jedis getJedis(){
        return jedisPool.getResource();
    }
}
