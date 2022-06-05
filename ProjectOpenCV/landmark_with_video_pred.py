#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->landmark_with_video_pred
# @Time      :2022/6/5 9:34
# @Author    :Peng neng
# @File      :landmark_with_video_pred.py
# ===============================
# 加载库
import cv2
import matplotlib.pyplot as plt
import dlib


if __name__ == '__main__':
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 获取人脸检测器
    detector = dlib.get_frontal_face_detector()

    # 获取关键点检测模型
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    # 读取视频流
    if cap.isOpened() is False:
        print("camera error!")
    while True:
        ret, frame = cap.read()

        # 灰度转换
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        faces = detector(gray, 1)
        # 绘制人脸和关键点
        for face in faces:
            # 绘制矩形框
            cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 3)
            # 检测到关键点
            shape = predictor(gray, face)
            # 获取关键点坐标
            for pt in shape.parts():
                # 绘制关键点
                cv2.circle(frame, (pt.x, pt.y), 4, (0, 0, 255), -1)
            # 显示效果
        if cv2.waitKey(1) & 0xFF == 27:
            break
        cv2.imshow("face rec lanmark with dlib", frame)
        # plt.axis("off")
        # plt.show()
    cap.release()
    cv2.destroyAllWindows()









