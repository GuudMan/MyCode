#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->gray_histgrom_mask
# @Time      :2022/6/4 13:53
# @Author    :Peng neng
# @File      :gray_histgrom_mask.py
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
    plt.subplot(2, 2, pos)
    plt.imshow(img_RGB)


# 显示直方图
def show_histogram(hist, title, pos, color):
    # 显示标题
    plt.title(title)
    plt.subplot(2, 2, pos)
    plt.xlim([0, 256])
    plt.plot(hist, color=color)


def main():
    plt.figure(figsize=(15, 6))
    plt.suptitle("灰度直方图 with mask", fontsize=4, fontweight='bold')

    img_gray = cv2.imread('./data/input_img/child.jpg', cv2.COLOR_BGR2GRAY)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_hray_hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    show_img(img_gray, 'img gray', 1)
    show_histogram(img_hray_hist, 'img gray hist', 2, 'm')

    # 计算mask
    mask = np.zeros(img_gray.shape[:2], np.uint8)
    mask[50:200, 80:200] = 255  # 获取mask并赋颜色
    img_mask_hist = cv2.calcHist([img_gray], [0], mask, [256], [0, 256])

    # 通过与运算，计算带有mask的灰度图片
    mask_img = cv2.bitwise_and(img_gray, img_gray, mask=mask)

    show_img(mask_img, 'gray image with mask', 3)
    show_histogram(img_mask_hist, 'gray img mask', 4, 'm')

    plt.show()


if __name__ == '__main__':
    main()
