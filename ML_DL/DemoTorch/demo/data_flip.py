#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->data_flip
# @Time      :2022/8/9 20:28
# @Author    :Peng neng
# @File      :data_flip.py
# ===============================
import cv2
import torch

if __name__ == '__main__':
    data = cv2.imread('../data/image_07729.jpg')
    cv2.imshow("test1", data)
    out = torch.from_numpy(data)
    out = torch.flip(out, dims=[0])
    data2 = out.numpy()
    cv2.imshow("test2", data2)
    print(out)
    # out = out.to(torch.device("cuda"))
    # data3 = out.to(torch.device("cpu"))
    # cv2.imshow("test3", data3)
    # print(out)
    cv2.waitKey(0)
    # cv2.destroyWindow()