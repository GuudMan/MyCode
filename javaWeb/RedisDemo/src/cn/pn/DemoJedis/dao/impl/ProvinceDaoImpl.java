package cn.pn.DemoJedis.dao.impl;


import cn.pn.DemoJedis.Domain.Province;
import cn.pn.DemoJedis.dao.ProvinceDao;
import cn.pn.DemoJedis.util.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

import java.util.List;


public class ProvinceDaoImpl implements ProvinceDao {

    //1.声明成员变量 jdbctemplement
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

    @Override
    public List<Province> findAll() {
        //1.定义sql
        String sql = "select * from province ";
        //2.执行sql
        List<Province> list = template.query(sql, new BeanPropertyRowMapper<Province>(Province.class));
        return list;
    }
}
