# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# @File       : spider_images.py
# @Time       ：2022/11/30 0030 15:40
# @Author     ：0399
# @version    ：python 3.9
# @Software: PyCharm
# @Description：
"""
# ====================================
# -*- encoding: utf-8 -*-
# @file       : download_image.py
# @Description:
# @Time       : 2022/02/07 17:08:26
# @Author     : gsjydys
# @Software   : python3.8.12

import re
import requests
import time
from urllib import parse  # 对汉字进行编码
import os
from fake_useragent import UserAgent  # 随机生成一个user-agent


class Picture:

    def __init__(self, name):
        self.name_ = name
        self.name = parse.quote(self.name_)  # 搜索关键词 --> 编码
        self.times = str(int(time.time() * 1000))  # 时间戳-->补全url
        self.headers = {'User-Agent': UserAgent().random}

    # 请求30张图片的链接
    def get_one_html(self, pn):
        response = requests.get(
            url=f"https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8032920601831512061&ipn=rj&ct=201326592&is=&fp=result&fr=&word={self.name}&cg=star&queryWord={self.name}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn={pn}&rn=30&gsm=1e&{self.times}=", headers=self.headers).content.decode('utf-8')
        return response

    # 请求单张图片内容
    def get_two_html(self, url):
        response = requests.get(url=url, headers=self.headers).content
        return response

    # 解析含30张图片的html的内容
    def parse_html(self, regex, html):
        content = regex.findall(html)
        return content

    # 主函数
    def run(self):
        os.makedirs(os.path.join("./spider_images",
                    self.name_.replace(" ", "-")), exist_ok=True)  # 下载路径

        response = self.get_one_html(0)
        regex1 = re.compile('"displayNum":(.*?),')
        num = int(self.parse_html(regex1, response)[0])  # 获取总的图片数量
        print(f"该关键字下一共有{num}张照片")
        if num >= 2000:
            num = 2000
        print(f"我们只取前{num}张图片")

        # 页面数量取30的整数倍，百度图库一页最多30张图片
        pn = num // 30

        j = 0  # 计数下载图片数
        for i in range(pn):  # 遍历每一个含30张图片的链接
            resp = self.get_one_html(i * 30)
            regex2 = re.compile('"middleURL":"(.*?)"')
            urls = self.parse_html(regex2, resp)  # 得到30张图片的链接（30个）
            for u in urls:  # 遍历每张图片的链接
                try:
                    content = self.get_two_html(u)  # 请求每张图片的内容
                    with open(os.path.join("./spider_images", self.name_.replace(" ", "-"), f"{u[28:35]}.jpg"), 'wb') as f:
                        f.write(content)
                    j += 1
                    print(f"完成{j}张照片")
                    time.sleep(0.01)
                finally:
                    continue


if __name__ == '__main__':
    # for i in [
    #     # '建筑施工 安全隐患', '佩戴工作证', '建筑施工 地面积水',
    #     # '建筑施工 材料码放不整齐', '建筑施工 防护网有漏洞', '建筑施工 配电箱线路混乱',
    #     # '建筑施工 配电箱未关门', '建筑施工 高处作业未系安全带', '楼梯临边隐患',
    #     #     '楼层临边隐患', \
    #             '建筑施工 孔洞隐患']:
    for i in ['建筑施工工人']:
        spider = Picture(i)
        spider.run()
