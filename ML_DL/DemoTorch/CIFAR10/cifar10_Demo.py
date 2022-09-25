#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->cifar10_Demo
# @Time      :2022/8/17 14:35
# @Author    :Peng neng
# @File      :cifar10_Demo.py
# ===============================
import glob
import numpy as np
import cv2
import os

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


label_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

# 数据解析
train_list = glob.glob("../data/CIFAR10/test_batch*")
save_path = "../data/CIFAR10/TEST"


for l in train_list:
    l_dict = unpickle(l)

    for im_idx, im_data in enumerate(l_dict[b'data']):

        # 利用索引号得到标签和文件名
        im_label = l_dict[b'labels'][im_idx]
        im_name = l_dict[b'filenames'][im_idx]

        print(im_label, im_name, im_data)

        im_label_name = label_names[im_label]

        im_data = np.reshape(im_data, [3, 32, 32])
        im_data = np.transpose(im_data, (1, 2, 0))

        # cv2.imshow("im_data", cv2.resize(im_data, (200, 200)))
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        if not os.path.exists("{}/{}".format(save_path, im_label_name)):
            os.mkdir("{}/{}".format(save_path, im_label_name))

        cv2.imwrite("{}/{}/{}".format(save_path,
                                      im_label_name,
                                      im_name.decode('utf-8')), im_data)







