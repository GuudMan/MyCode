#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->face_landmark_detec_video
# @Time      :2022/6/5 9:20
# @Author    :Peng neng
# @File      :face_landmark_detec_video.py
# ===============================
import cv2
import matplotlib.pyplot as plt
import dlib


def plot_rectangle(img, faces):
    # 拿到人脸数据  坐标，宽和高，
    for face in faces:
        cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 3)
    return img


if __name__ == '__main__':
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    # 判断摄像头状态
    if cap.isOpened() is False:
        print("camera error!")

    # 检测每帧
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 绘制检测结果
            detector = dlib.get_frontal_face_detector()
            predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
            faces = detector(gray, 1)

            plot_rectangle(frame, faces)
            pre_ret = predictor(frame, faces)

            for pt in pre_ret.parts():
                cv2.circle(frame, (pt.x(), pt.y()), 5, (0, 0, 255), -1)

            cv2.imshow("face det dlib", frame)

            if cv2.waitKey(1) == 27:
                break

        # 退出
        cap.release()
        cv2.destroyAllWindows()

    # 释放资源