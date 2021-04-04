package cn.pn.DemoJedis.Domain;


/*
** java1.8
** _*_coding:utf-8 _*_
**  @Time        :
** @Author      :彭能
**  @Email       :2663017379@qq.com
**  @Name        :
**  @Software    :IntelliJ IDEA 2019.3.3 x64
**  @Description :
 */

// 创建province类，对应数据库表

public class Province {

    private int id;
    private String province;


    @Override
    public String toString() {
        return "province{" +
                "id=" + id +
                ", province='" + province + '\'' +
                '}';
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }
}
