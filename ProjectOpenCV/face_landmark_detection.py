#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->face_landmark_detection
# @Time      :2022/6/5 8:48
# @Author    :Peng neng
# @File      :face_landmark_detection.py
# ===============================
import cv2
import dlib
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 读取图片
    img = cv2.imread("./data/input_img/liuyifei.jpg")

    # 调用人脸检测器
    detector = dlib.get_frontal_face_detector()
    # 加载预测关键点模型
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # 灰度转换
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 人脸检测
    faces = detector(gray, 1)

    # 循环：遍历每张人脸，绘制矩形和关键点
    for face in faces:
        # 绘制矩形
        cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 5)

        # 预测关键点
        shape = predictor(img, face)

        # 显示/绘制关键点
        for pt in shape.parts():
            pt_position = (pt.x, pt.y)
            # -1 表示填满圆圈
            cv2.circle(img, pt_position, 4, (0, 0, 255), -1)

    # 显示效果图
    plt.imshow(img)
    plt.axis("off")
    plt.show()