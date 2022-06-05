#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->show_image
# @Time      :2022/6/1 22:38
# @Author    :Peng neng
# @File      :show_image.py
# ===============================
import cv2
import argparse

if __name__ == '__main__':
    # 方法1
    # img = cv2.imread('./data/input_img/open_cv_log.jpg')
    # cv2.imshow('log', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 方法2
    parser = argparse.ArgumentParser()

    parser.add_argument("path_img", help="path to input the image")
    # 解析参数
    arg = parser.parse_args()
    # 加载图片
    # 方法1
    img = cv2.imread(arg.path_img)
    cv2.imshow("log", img)

    # 方法2
    args_dict = vars(parser.parse_args())
    img2 = cv2.imread(args_dict['path_img'])
    cv2.imshow("log2", img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
