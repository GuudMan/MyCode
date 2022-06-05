#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->read_camera_save_video
# @Time      :2022/6/3 10:38
# @Author    :Peng neng
# @File      :read_camera_save_video.py
# ===============================
import cv2
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("video_output", help="path to the output video")

    args = parser.parse_args()

    capture = cv2.VideoCapture(0)
    if capture.isOpened() is False:
        print("camera error!")
    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_high = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = capture.get(cv2.CAP_PROP_FPS)

    # 对视频编码
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    output_gray = cv2.VideoWriter(args.video_output, fourcc, int(fps), (int(frame_width), int(frame_high)), False)

    while capture.isOpened():
        ret, frame = capture.read()
        if ret:
            # 将读取到的帧转成灰度
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #
            output_gray.write(gray_frame)
            cv2.imshow("gray", gray_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    capture.release()
    output_gray.release()
    cv2.destroyAllWindows()
