import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.util.Random;


/**
 * 重定向
 */

@WebServlet("/CheckCodeServlet3")
public class CheckCodeServlet3 extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

       // 创建一个对象，在内存中画图（代表验证码的图片对象）
        int width = 100;
        int height = 50;
        BufferedImage image = new BufferedImage(width, height,BufferedImage.TYPE_3BYTE_BGR);

        // 美化图片
        // 填充背景色
        Graphics graphics = image.getGraphics();// 获取画笔对象
        graphics.setColor(Color.pink);// 设置画笔颜色
        graphics.fillRect(0,0,width,height);

        // 画边框
        graphics.setColor(Color.blue);
        graphics.drawRect(0,0,width-1, height-1);

//        定义字符串
//        String str1 = "a";
//        String str2 = "A";
//        String str = "";
//        for(i =0; i<26; i++){
//            str += str1;
//            str +=str2;
//        }
        String str = "abcdefghijlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        // 生成随机角标
        Random random = new Random();

        // 写验证码
        for(int i = 1; i <= 4; i++){

            int index = random.nextInt(str.length());
            char ch = str.charAt(index);// 随机字符
            graphics.drawString(ch + "",width/5*i,height/2);
        }

        // 画干扰线
        // 随机生成坐标点
        for(int i = 0; i < 5; i++){
            int xLimit1 = random.nextInt(width);
            int yLimit1 = random.nextInt(height);
            int xLimit2 = random.nextInt(width);
            int yLimit2 = random.nextInt(height);
            graphics.drawLine(xLimit1,yLimit1,xLimit2,yLimit2);
        }




        // 将图片输出到页面展示 response输出流
        ImageIO.write(image, "jpg", response.getOutputStream());

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        this.doPost(request,response);
    }
}
