#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->gray_hisgram
# @Time      :2022/6/4 9:10
# @Author    :Peng neng
# @File      :gray_hisgram.py
# ===============================
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 显示图片
def show_img(image, title, pos):
    # BGR 2 RGB ::-1表示将顺序倒过来
    img_RGB = image[:, :, ::-1]
    # 显示标题
    plt.title(title)
    plt.subplot(2, 3, pos)
    plt.imshow(img_RGB)


# 显示直方图
def show_histogram(hist, title, pos, color):
    # 显示标题
    plt.title(title)
    plt.subplot(2, 3, pos)
    plt.xlabel('Bins')
    plt.ylabel('Pixels')
    plt.xlim([0, 256])
    # plt.ylim()
    plt.plot(hist, color=color)


# main
def main():
    plt.figure(figsize=(15, 6))
    plt.suptitle("灰度直方图", fontsize=14, fontweight='bold')
    img = cv2.imread('./data/input_img/child.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist_img = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    # 展示灰度直方图
    img_bgr = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    show_img(img_bgr, "bgr, img", 1)
    show_histogram(hist_img, "gray img histogram", 4, 'm')
    plt.show()


if __name__ == '__main__':
    main()
