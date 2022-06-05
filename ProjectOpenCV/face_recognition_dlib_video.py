#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->face_recognition_dlib_video
# @Time      :2022/6/5 8:31
# @Author    :Peng neng
# @File      :face_recognition_dlib_video.py
# ===============================
import cv2
import dlib
import matplotlib.pyplot as plt
import numpy as np

def plot_rectangle(img, faces):
    # 拿到人脸数据  坐标，宽和高，
    for face in faces:
        cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()), (255, 0, 0), 3)
    return img

def main():
    # 1. 打开摄像头
    cap = cv2.VideoCapture(0)
    # 2.判断摄像头是否正常工作
    if cap.isOpened() is False:
        print("camera error!")

    # 3. 摄像头打开，循环读取每一帧
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 4. 调用dlib进行检测
            detector = dlib.get_frontal_face_detector()
            det_ret = detector(gray, 1)
            # 5. 绘制检测结果
            det_img = plot_rectangle(frame, det_ret)
            # 6. 实时显示检测结果
            cv2.imshow("face det dlib", det_img)
            # 7. 退出 esc
            if cv2.waitKey(1) == 27:
                break
    # 8. 释放资源
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()