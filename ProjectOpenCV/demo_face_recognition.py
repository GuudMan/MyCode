#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->face_recongination
# @Time      :2022/6/4 19:18
# @Author    :Peng neng
# @File      :demo_face_recognition.py
# ===============================
# 1. 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 2. 显示图片
def show_img(img, title, pos):
    img_RGB = img[:, :, ::-1]
    plt.subplot(2, 2, pos)
    plt.title(title)
    plt.axis('off')
    plt.imshow(img_RGB)
    plt.show()


# 3. 绘制人脸矩形框
def plot_rectangle(img, faces):
    # 拿到人脸数据  坐标，宽和高，
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    return img


def main():
    # 4、 主函数
    # 读取图片
    img = cv2.imread('./data/input_img/zhap.jpg')
    # 转换成灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 通过opencv自带的方法，加载级联分类器，
    face_at2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    # 对图像中的人脸进行检测
    face_alt2_detect = face_at2.detectMultiScale(gray)
    face_alt2_ret = plot_rectangle(img.copy(), face_alt2_detect)
    # 创建画布
    plt.figure(figsize=(9, 6))
    plt.suptitle("Face detection haar cascade", fontsize=14, fontweight='bold')

    # 显示检测结果
    show_img(face_alt2_ret, 'face_alt2', 1)
    plt.show()


if __name__ == '__main__':
    main()
