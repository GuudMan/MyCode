// package cn.pn.sertlvtDemo.Servlet;
//
// import com.fasterxml.jackson.databind.ObjectMapper;
//
// import javax.servlet.ServletException;
// import javax.servlet.annotation.WebServlet;
// import javax.servlet.http.HttpServlet;
// import javax.servlet.http.HttpServletRequest;
// import javax.servlet.http.HttpServletResponse;
// import java.io.IOException;
// import java.util.HashMap;
// import java.util.Map;
//
// @WebServlet("/FindUserServlet")
// public class FinduserServlet extends HttpServlet {
//     protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//
//         response.setContentType("text/html;charsetet=utf-8");
//         // 获取用户名
//         String username = request.getParameter("username");
//
//         Map<String,Object> map = new HashMap<String,Object>();
//
//
//
//         // 调用service判断用户是否存在
//         if("tom".equals(username)){
//             // 用户名存在
//             map.put("userExsit",true);
//             map.put("msg","用户太受欢迎，换一个");
//         }else {
//             // 不存在
//             map.put("userExsit",false);
//             map.put("msg","用户名可用");
//         }
//
//         // 将map转为json，将其传递到客户端页面上
//         ObjectMapper mapper = new ObjectMapper();
//         mapper.writeValue(response.getWriter(),map);
//     }
//
//     protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//         this.doPost(request,response);
//     }
// }


package cn.pn.sertlvtDemo.Servlet;

import com.fasterxml.jackson.databind.ObjectMapper;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@WebServlet("/FindUserServlet")
public class FinduserServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        //1.获取用户名
        String username = request.getParameter("username");

        //2.调用service层判断用户名是否存在

        //期望服务器响应回的数据格式：{"userExsit":true,"msg":"此用户名太受欢迎,请更换一个"}
        //                         {"userExsit":false,"msg":"用户名可用"}

        //设置响应的数据格式为json
        response.setContentType("application/json;charset=utf-8");
        Map<String,Object> map = new HashMap<String,Object>();

        if("tom".equals(username)){
            //存在
            map.put("userExsit",true);
            map.put("msg","此用户名太受欢迎,请更换一个");
        }else{
            //不存在
            map.put("userExsit",false);
            map.put("msg","用户名可用");
        }

        //将map转为json，并且传递给客户端
        //将map转为json
        ObjectMapper mapper = new ObjectMapper();
        //并且传递给客户端
        mapper.writeValue(response.getWriter(),map);


    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request, response);
    }
}
