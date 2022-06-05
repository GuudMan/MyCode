#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->color_histgram
# @Time      :2022/6/4 14:22
# @Author    :Peng neng
# @File      :color_histgram.py
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
    plt.subplot(3, 2, pos)
    plt.imshow(img_RGB)
    plt.axis("off")


def show_histogram(hist, title, pos, color):
    # 显示标题
    plt.title(title)
    plt.subplot(3, 2, pos)
    plt.xlim([0, 256])
    for h, c in zip(hist, color):
        plt.plot(h, color=c)


def calc_color_hist(img):
    hist = []
    hist.append(cv2.calcHist([img], [0], None, [256], [0, 256]))
    hist.append(cv2.calcHist([img], [1], None, [256], [0, 256]))
    hist.append(cv2.calcHist([img], [2], None, [256], [0, 256]))
    return hist


def main():
    plt.figure(figsize=(15, 6))
    plt.suptitle("灰度直方图 with mask", fontsize=4, fontweight='bold')

    img = cv2.imread('./data/input_img/child.jpg')

    img_hist = calc_color_hist(img)

    show_img(img, 'img rgb', 1)
    show_histogram(img_hist, 'img rgb hist', 2, ('b', 'g', 'r'))

    # 原始图片中像素增加50
    M = np.ones(img.shape, dtype='uint8') * 50
    added_img = cv2.add(img, M)

    add_img_hist = calc_color_hist(added_img)

    show_img(added_img, 'add img', 3)
    show_histogram(add_img_hist, 'add img hist', 4, ('b', 'g', 'r'))

    # 原始图片中像素减少50
    N = np.ones(img.shape, dtype='uint8') * 50
    subbed_img = cv2.subtract(img, N)

    sub_img_hist = calc_color_hist(subbed_img)

    show_img(subbed_img, 'sub img', 5)
    show_histogram(sub_img_hist, 'sub img hist', 6, ('b', 'g', 'r'))

    plt.show()


if __name__ == '__main__':
    main()