#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->dlib_face_recognition
# @Time      :2022/6/5 16:22
# @Author    :Peng neng
# @File      :dlib_face_recognition.py
# ===============================
# 导入库
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
    img = cv2.imread("./data/input_img/hezhao1.jpg")

    # 灰度转换
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 调用face_recognition方法
    face_landmarks = face_recognition.face_landmarks(gray, None, "large")

    # 绘制关键点
    img_landmark = show_landmarks(img.copy(), face_landmarks)
    # 创建画布
    plt.figure(figsize=(9, 6))
    plt.suptitle('face landmark with face recognition', fontsize=8, fontweight='bold')
    # 显示效果
    show_img(img_landmark, 'face recognition landmark')
    plt.show()


if __name__ == '__main__':
    main()
