package cn.dao;

import cn.domain.User;
import com.alibaba.druid.util.JdbcUtils;
import itcast.util.JDBCUtils;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;

// 操作数据库中的user类
public class UserDao {
  // 声明jdbc共用
  private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

  // 登陆方法
    public User login(User loginUser){
        String sql = "select * from user where username=? and password = ? ";
        User user = template.queryForObject(sql,
                new BeanPropertyRowMapper<User>(User.class),
                loginUser.getUsername(), loginUser.getPassword());
        return user;
    }

}
