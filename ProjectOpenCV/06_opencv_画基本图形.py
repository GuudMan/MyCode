#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->06_opencv_画基本图形
# @Time      :2022/6/4 15:29
# @Author    :Peng neng
# @File      :06_opencv_画基本图形.py
# ===============================
import cv2
import matplotlib.pyplot as plt
import numpy as np

# 定义颜色
colors = {
    'blue': (0, 0, 255),
    'green': (0, 255, 0),
    'yellow': (0, 255, 255),
    'magenta': (255, 0, 255),
    'cyan': (255, 255, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'gray': (0, 255, 255),
    'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
    'dark_gray': (50, 50, 50),
    'light_gray': (220, 220, 220)
}


# 显示图像
def show_img(img, title):
    img_RGB = img[:, :, ::-1]
    plt.title(title)
    plt.imshow(img_RGB)
    plt.show()


if __name__ == '__main__':
    # 创建画布
    canvas = np.zeros((400, 400, 3), np.uint8)
    canvas[:] = colors['white']
    show_img(canvas, 'Background')

    # 画直线
    cv2.line(canvas, [0, 0], [400, 400], colors['green'], 5)
    cv2.line(canvas, [0, 400], [400, 0], colors['black'], 5)
    show_img(canvas, 'line', )
