#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->face_dlib
# @Time      :2022/6/4 21:19
# @Author    :Peng neng
# @File      :face_dlib.py
# ===============================

# 导入库
import cv2
import dlib
import numpy as np
import matplotlib.pyplot as plt


# 显示图片
def show_img(image, title, pos):
    # BGR 2 RGB ::-1表示将顺序倒过来
    img_RGB = image[:, :, ::-1]
    # 显示标题
    plt.title(title)
    plt.subplot(3, 2, pos)
    plt.imshow(img_RGB)
    plt.axis("off")


# 绘制人脸矩形框
# 3. 绘制人脸矩形框
def plot_rectangle(img, faces):
    # 拿到人脸数据  坐标，宽和高，
    for face in faces:
        cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 3)
    return img


def main():
    # 读取图片
    img = cv2.imread('../data/input_img/face.jpg')

    # 灰度转变
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 调用dlib进行检测
    detector = dlib.get_frontal_face_detector()
    det_ret = detector(gray, 1)  # 1 表示将图片放大一倍进行检测

    # 绘制检测的人脸框
    img_ret = plot_rectangle(img.copy(), det_ret)

    # 创建画布
    plt.figure(figsize=(9, 6))
    plt.suptitle("face detection with dlib", fontsize=14, fontweight='bold')

    # 显示检测结果
    show_img(img_ret, 'face_detection', 1)
    plt.show()


if __name__ == '__main__':
    main()
