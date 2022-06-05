#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->read_process_save
# @Time      :2022/6/3 9:16
# @Author    :Peng neng
# @File      :read_process_save.py
# ===============================
import argparse

import cv2

if __name__ == '__main__':
    # 获取参数
    parser = argparse.ArgumentParser()
    # 添加参数
    parser.add_argument("input_img", help="read one image")
    parser.add_argument("output_img", help="save to image")
    # 解析参数，以字典形式保存参数和值
    args = vars(parser.parse_args())

    # 加载图片
    img = cv2.imread(args["input_img"])
    # 灰度处理, 原始图片变成灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(args["output_img"], img_gray)

    # 显示图片
    cv2.imshow("ori", img)
    cv2.imshow("gray", img_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()