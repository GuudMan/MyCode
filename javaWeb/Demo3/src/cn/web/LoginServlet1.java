package cn.web;

import cn.dao.UserDao;
import cn.domain.User;
import org.apache.commons.beanutils.BeanUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.util.Map;

/**
 * 一次性获取所有界面参数
 */
@WebServlet("/LoginServlet1")
public class LoginServlet1 extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        //1.设置编码
        req.setCharacterEncoding("utf-8");
        // 2. 获取所有请求参数
        Map<String, String[]> map = req.getParameterMap();
        // 3.1 创建user对象
        User loginUser = new User();
        // 3.2 使用BeanUtils封装
        try {
            BeanUtils.populate(loginUser,map);
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        }

        //4.调用UserDao的login方法
        UserDao dao = new UserDao();
        System.out.println("dao");
        User user = dao.login(loginUser);

        //5.判断user
        if(user == null){
            //登录失败
            req.getRequestDispatcher("/FailServlet").forward(req,resp);
        }else{
            //登录成功
            //存储数据
            req.setAttribute("user",user);
            //转发
            req.getRequestDispatcher("/SuccessServlet").forward(req,resp);
        }

    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        this.doGet(req,resp);
        System.out.println("no problem");
    }
}

