#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->object_tracking_dlib
# @Time      :2022/6/5 20:07
# @Author    :Peng neng
# @File      :object_tracking_dlib.py
# ===============================
# 导入库
import cv2
import dlib


def show_info(frame, tracking_state):
    pos1 = (10, 20)
    pos2 = (10, 40)
    pos3 = (10, 60)
    info1 = "put left button, select an area, start tracking"
    info2 = "'1' , start tracking, '2: stop tracking, 'q': exit"
    info3 = "put left button, select an area, start tracking"
    cv2.putText(frame, info1, pos1, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    cv2.putText(frame, info2, pos2, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    if tracking_state:
        cv2.putText(frame, "tracking now...", pos3,
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    else:
        cv2.putText(frame, "stop tracking...", pos3,
                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))


# 存放鼠标点击事件坐标
points = []


# 定义方法：鼠标点击事件
def mouse_event_handler(event, x, y, flag, params):
    global points
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键按下
        points = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))


if __name__ == '__main__':
    # 打开摄像头
    cap = cv2.VideoCapture(0)
    # 设置窗口名称
    nameWindow = "Object Tracking"
    cv2.namedWindow(nameWindow)

    # 将鼠标事件绑定到窗口上
    cv2.setMouseCallback(nameWindow, mouse_event_handler)

    # 启动跟踪器
    tracker = dlib.correlation_tracker()

    # 假设跟踪状态
    tracking_state = False
    while True:
        ret, frame = cap.read()
        # 显示提示信息：调用方法
        show_info(frame, tracking_state)
        # 如果获取到的坐标点为两个，则绘制矩形，也要让dlib的rectangel()知道坐标在哪
        if len(points) == 2:
            cv2.rectangle(frame, points[0], points[1], (255, 0, 0), 3)
            dlib_rec = dlib.rectangle(points[0][0], points[0][1], points[1][0], points[1][1])
        # 如果跟踪状态为true，那么更新跟踪，获取位置，绘制矩形
        if tracking_state is True:
            tracker.update(frame)
            # 获取坐标
            pos = tracker.get_position()
            cv2.rectangle(frame, (int(pos.left()), int(pos.top())),
                          (int(pos.right()), int(pos.bottom())), (255, 0, 0), 3)
        # 事件判断 1， 2， q
        key = cv2.waitKey(1) & 0xFF
        if key == ord('1'):
            if len(points) == 2:
                tracker.start_track(frame, dlib_rec)
                tracking_state = True
                points = []
        if key == ord('2'):
            points = []
            tracking_state = False
        if key == ord('q'):
            break
        # 显示整体效果
        cv2.imshow(nameWindow, frame)

    cap.release()
    cv2.destroyAllWindows()