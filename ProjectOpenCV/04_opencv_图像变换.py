#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->04_opencv_图像变换
# @Time      :2022/6/3 20:26
# @Author    :Peng neng
# @File      :04_opencv_图像变换.py
# ===============================
import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    img = cv2.imread('./data/input_img/open_cv_log.jpg')
    width, height, chanel = img.shape
    print(width, height, chanel)
    plt.imshow(img)
    #plt.show()

    # 图像放大、缩小
    resize_img = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_LINEAR)
    plt.imshow(resize_img)

    small_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    plt.imshow(small_img)

    # 图像平移
    height, width = img.shape[:2]
    M1 = np.float32([[1, 0, 100], [0, 1, 50]])  # 图像向右移动200个像素，向下移动50个像素
    move_img1 = cv2.warpAffine(img, M1, (width, height))
    plt.imshow(move_img1)

    M2 = np.float32([[1, 0, -100], [0, 1, -50]])  # 图像向左移动200个像素，向上移动50个像素
    move_img2 = cv2.warpAffine(img, M2, (width, height))
    plt.imshow(move_img2)

    # 图像旋转
    height, width = img.shape[:2]
    centor = (width // 2, height // 2)  # 旋转中心
    M3 = cv2.getRotationMatrix2D(centor, 120, 1)  # 1表示旋转过程中不缩放
    rotation_img = cv2.warpAffine(img, M3, (width, height))
    plt.imshow(rotation_img)

    # 图像放射变换
    p1 = np.float32([[120, 35], [215, 45], [13, 120]])
    p2 = np.float32([[135, 45], [300, 110], [130, 230]])

    # 计算变换矩阵
    M4 = cv2.getAffineTransform(p1, p2)

    trans_img = cv2.warpAffine(img, M4, (width, height))
    plt.imshow(trans_img)

    # 图像裁剪
    crop_img = img[50:200, 40:100]
    plt.imshow(crop_img)

    # 位运算
    rectangle = np.zeros((300, 300), dtype='uint8')
    ret_img = cv2.rectangle(rectangle, (25, 25), [275, 275], 255, -1)
    plt.imshow(ret_img)

    circle = np.zeros((300, 300), dtype='uint8')
    circle_img = cv2.circle(circle, (150, 150), 150, 255,  -1)
    plt.imshow(circle_img)

    # y与运算
    and_img = cv2.bitwise_and(ret_img, circle_img)
    plt.imshow(and_img)

    # 或运算
    or_img = cv2.bitwise_or(ret_img, circle_img)
    plt.imshow(or_img)

    # 异或运算
    xor_img = cv2.bitwise_xor(ret_img, circle_img)
    plt.imshow(xor_img)

    # 图像分离和融合
    (B, G, R) = cv2.split(img)
    print(B, G, R)
    plt.imshow(B)
    plt.imshow(G)
    plt.imshow(R)

    # 融合
    zeros = np.zeros(img.shape[:2], dtype='uint8')
    plt.imshow(cv2.merge([zeros, zeros, R]))
    plt.imshow(cv2.merge([zeros, zeros, R]))
    plt.imshow(cv2.merge([B, zeros, zeros]))
    plt.imshow(cv2.merge([zeros, R, zeros]))

    # 颜色空间
    # 灰度
    # HSV: 色度，饱和度，纯度
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    plt.imshow(hsv)
    plt.show()


