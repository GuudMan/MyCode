package cn.dao;

import cn.domain.User;
import cn.util.JDBCUtils;
import org.springframework.dao.DataAccessException;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.SqlOutParameter;

//// 操作数据库中的user类
//public class UserDao {
//  // 声明jdbc共用
//  private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());
//
//  // 登陆方法
//    public User login(User loginUser){
//        try {
//            String sql = "select * from user where username=? and PASSWORD = ? ";
//            User user = template.queryForObject(sql,
//                    new BeanPropertyRowMapper<User>(User.class),
//                    loginUser.getUsername(), loginUser.getPassword());
//            return user;
//        } catch (DataAccessException e) {
//            e.printStackTrace();
//            return null;
//        }
//    }
//
//}

public class UserDao {

    //声明JDBCTemplate对象共用
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());

    /**
     * 登录方法
     * @param loginUser 只有用户名和密码
     * @return user包含用户全部数据,没有查询到，返回null
     */
    public User login(User loginUser){
        System.out.println("login");
        try {
            //1.编写sql
            String sql = "select * from user where username = ? and password = ?";
            //2.调用query方法
            User user = template.queryForObject(sql,
                    new BeanPropertyRowMapper<User>(User.class),
                    loginUser.getUsername(), loginUser.getPassword());


            return user;
        } catch (DataAccessException e) {
            e.printStackTrace();//记录日志
            return null;
        }
    }
}