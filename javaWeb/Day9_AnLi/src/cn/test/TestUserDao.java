package cn.test;


import cn.dao.UserDao;
import cn.domain.User;
import org.junit.Test;

public class TestUserDao {
    @Test
    public void testLogin(){
        User user = new User();
        user.setUsername("super");
        user.setPassword("123");

        UserDao userDao = new UserDao();
        User user1 = userDao.login(user);
        System.out.println(user1);
    }
}
