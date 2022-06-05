#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->read_camera
# @Time      :2022/6/3 9:31
# @Author    :Peng neng
# @File      :read_camera.py
# ===============================

import cv2
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("index_camera", help="camera id", type=int)
    args = parser.parse_args()
    print("the camera index", args.index_camera)

    # 捕获视频
    capture = cv2.VideoCapture(args.index_camera)

    # 获取帧长、宽
    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = capture.get(cv2.CAP_PROP_FPS)
    print("帧的宽度", frame_width)
    print("帧的高度", frame_height)
    print("帧的FPS", fps)

    # 判断摄像头是否打开
    if capture.isOpened() is False:
        print("camera Error!")
    # 读取视频到关闭
    while capture.isOpened():
        # 获取每一帧r
        ret, frame = capture.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 显示
        cv2.imshow("image", frame)
        cv2.imshow("gray frame", gray_frame)
        # 键盘输入q, 就关闭
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    # 释放资源
    capture.release()
    cv2.destroyAllWindows()
