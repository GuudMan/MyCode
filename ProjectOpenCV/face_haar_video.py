#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->face_haar_video
# @Time      :2022/6/4 21:01
# @Author    :Peng neng
# @File      :face_haar_video.py
# ===============================
# 1. 导入库
import cv2
import matplotlib.pyplot as plt
import numpy as np


# 3. 绘制人脸矩形框
def plot_rectangle(img, faces):
    # 拿到人脸数据  坐标，宽和高，
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    return img


def main():
    # 4、 主函数
    capture = cv2.VideoCapture(0)
    # 通过opencv自带的方法，加载级联分类器，
    face_at2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    if capture.isOpened() is False:
        print("camera error!")

    while True:
        ret, frame = capture.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 对图像中的人脸进行检测
            face_alt2_detect = face_at2.detectMultiScale(gray)
            face_alt2_ret = plot_rectangle(frame.copy(), face_alt2_detect)

            cv2.imshow("face recognition", face_alt2_ret)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()