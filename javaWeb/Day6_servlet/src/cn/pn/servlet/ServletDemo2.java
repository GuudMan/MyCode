package cn.pn.servlet;

import javax.servlet.*;
import java.io.IOException;

// servlet方法
public class ServletDemo2 implements Servlet {
    /*
    初始化方法，在servlet被创建时执行，只会执行一次
     */
    @Override
    public void init(ServletConfig servletConfig) throws ServletException {
        System.out.println("inti------");
    }
    // servlet配置对象
    @Override
    public ServletConfig getServletConfig() {
        return null;
    }
    /*
    service:提供服务的方法，执行多次
     */
    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        System.out.println("service-----");
    }
    // 获取servlet的信息，版本，作者，一般不会使用，重点掌握与生命周期相关的方法
    @Override
    public String getServletInfo() {
        return null;
    }
    /*
    销毁方法，在servlet正常关闭时执行，只会执行一次
     */
    @Override
    public void destroy() {
        System.out.println("destory------");
    }
}
