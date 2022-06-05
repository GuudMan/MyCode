#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->dlib_face_recogniyion_video
# @Time      :2022/6/5 16:53
# @Author    :Peng neng
# @File      :dlib_face_recogniyion_video.py
# ===============================
import cv2
import face_recognition
import matplotlib.pyplot as plt


# 显示图片
def show_img(img, title):
    plt.title(title)
    plt.imshow(img)
    plt.axis('off')


# 绘制关键点
def show_landmarks(img, landmarks):
    for landmark_dict in landmarks:
        for landmark_key in landmark_dict.keys():
            for p in landmark_dict[landmark_key]:
                cv2.circle(img, p, 3, (0, 0, 255), -1)
    return img


def main():
    # 主函数
    # 读取图片
    # img = cv2.imread("./data/input_img/hezhao1.jpg")
    cap = cv2.VideoCapture(0)
    if cap.isOpened() is False:
        print("camera error")

    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_landmarks = face_recognition.face_landmarks(gray, None, 'large')

            img_landmark = show_landmarks(frame, face_landmarks)

            cv2.imshow("face det dlib", img_landmark)

        if cv2.waitKey(1) == 27:
            break

    # 退出
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
