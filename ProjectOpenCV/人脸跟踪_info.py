#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->人脸跟踪
# @Time      :2022/6/5 17:00
# @Author    :Peng neng
# @File      :人脸跟踪.py
# ===============================
# 导入库
import cv2
import dlib


# 增加功能2， 信息提示
def show_info(frame, track_state):
    pos1 = (20, 40)
    pos2 = (20, 80)
    cv2.putText(frame, "'1': reset", pos1, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
    #  根据状态，显示不同的信息
    if track_state is True:
        cv2.putText(frame, "tracking now...", pos2, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    else:
        cv2.putText(frame, "no tracking", pos2, cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))


def main():
    # 主函数
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 基于dlib获取人脸检测器
    detector = dlib.get_frontal_face_detector()

    # 基于dlib实时跟踪
    tracker = dlib.correlation_tracker()

    # tracking_state=False 跟踪状态
    tracking_state = False

    # 增加功能一，保存视频
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_high = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_fps = cap.get(cv2.CAP_PROP_FPS)
    # 设置视频格式
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # 设置输出格式
    output = cv2.VideoWriter("./data/output_file/recod.avi", fourcc, int(frame_fps),
                             (int(frame_width), int(frame_high)), True)

    # 循环读取每一帧
    while True:
        # 没有跟踪，启动跟踪器
        ret, frame = cap.read()

        # 显示提示信息
        show_info(frame, tracking_state)

        if tracking_state is False:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            dets = detector(gray, 1)
            if len(dets) > 0:
                tracker.start_track(frame, dets[0])  # dets[0]人脸坐标
                tracking_state = True
        # 正在跟踪，实时获取人脸的位置
        if tracking_state is True:
            tracker.update(frame)  # 更新画面
            pos = tracker.get_position()
            cv2.rectangle(frame, (int(pos.left()), int(pos.top())),
                          (int(pos.right()), int(pos.bottom())), (0, 0, 255), 5)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        if key == ord('1'):
            tracking_state = False

        cv2.imshow('face track', frame)
        # 报存视频
        output.write(frame)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
