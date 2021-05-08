package com.pn.spring5;

import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.util.Arrays;

public class JDKProxy {
    public static void main(String[] args) {
        // 创建接口实例类代理对象
        // 第二个参数 接口
        Class[] interfaces = {UserDao.class};
        UserDaoImpl userDao = new UserDaoImpl();
        UserDao dao = (UserDao) Proxy.newProxyInstance(
                JDKProxy.class.getClassLoader(), interfaces, new UserDaoProxy(userDao));
        int result = dao.add(1,2);
        System.out.println(result);
        // System.out.println(dao.update("hfhgf"));
    }
}

// 创建代理对象
class UserDaoProxy implements InvocationHandler{

    // 创建的是谁的代理对象，需要把谁传过来
    // 有参构造
    private Object object;
    public UserDaoProxy(Object object){
        this.object = object;
    }

    // 增强的逻辑
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

        // 方法之前
        System.out.println("方法执行之前执行。。。" + method.getName()
                + "传递的参数" + Arrays.toString(args));
        // 被增强的方法执行
        Object invoke = method.invoke(object, args);
        // 方法之后
        System.out.println("方法之后执行" + object.toString());
        return invoke;
    }
}
