#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->gray_hisogram_add
# @Time      :2022/6/4 9:49
# @Author    :Peng neng
# @File      :gray_hisogram_add.py
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

    # 对图片中的像素值增加50
    M = np.ones(img_gray.shape, np.uint8) * 50

    added_img = cv2.add(img_gray, M)

    add_img_hist = cv2.calcHist([added_img], [0], None, [256], [0, 256])
    added_img_bgr = cv2.cvtColor(added_img, cv2.COLOR_GRAY2BGR)
    show_img(added_img_bgr, "add img", 2)
    show_histogram(add_img_hist, "add img hist", 5, "m")

    # 减50
    N = np.ones(img_gray.shape, np.uint8) * 50

    subbed_img = cv2.subtract(img_gray, N)

    sub_img_hist = cv2.calcHist([subbed_img], [0], None, [256], [0, 256])
    subbed_img_bgr = cv2.cvtColor(subbed_img, cv2.COLOR_GRAY2BGR)
    show_img(subbed_img_bgr, "sub img", 3)
    show_histogram(sub_img_hist, "sub img hist", 6, "m")

    plt.show()


if __name__ == '__main__':
    main()
