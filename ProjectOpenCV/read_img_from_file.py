#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->read_img_from_file
# @Time      :2022/6/3 9:50
# @Author    :Peng neng
# @File      :read_img_from_file.py
# ===============================
import cv2
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", help="the path to the video file")
    args = parser.parse_args()
    capture = cv2.VideoCapture(args.video_path)
    ret, frame = capture.read()
    while ret:
        cv2.imshow("video", frame)
        # 继续读取帧
        ret, frame = capture.read()
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()
