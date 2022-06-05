#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->opencv_main
# @Time      :2022/5/31 22:12
# @Author    :Peng neng
# @File      :opencv_main.py
# ===============================
import os
from cfg import *
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # img = cv2.imread(base_path + "input_img/child.jpg")
    # print("图片形状", img.shape)
    # print("img的数据类型", img.dtype)
    # print("RGB的值 实际排序是B,G,R", img[6, 40][0], img[6, 40][1], img[6, 40][2])
    # # 更换颜色
    # img[6, 40] = (0, 255, 255)
    # # 显示图片
    # cv2.imshow("child", img)
    # # 等待
    # cv2.waitKey(0)
    # # 关闭窗口
    # cv2.destroyAllWindows()

    #灰度
    # img_gray = cv2.imread(base_path + "input_img/cat_gray.png", cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("cat", img_gray)
    # print("形状", img_gray.shape)
    # value = img_gray[6, 80]
    # print("通道", value)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    #灰度
    img_log = cv2.imread(base_path + "input_img/open_cv_log.jpg")
    b, g, r = cv2.split(img_log)
    img_new = cv2.merge([r, g, b])

    plt.subplot(121)
    plt.imshow(img_log)
    plt.subplot(122)
    plt.imshow(img_new)
    plt.show()
