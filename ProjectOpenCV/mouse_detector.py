#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->mouse_detector
# @Time      :2022/6/7 21:49
# @Author    :Peng neng
# @File      :mouse_detector.py
# ===============================
import os
import sys

import cv2
import dlib
import numpy as np

PREDICTOR_PATH = 'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(PREDICTOR_PATH)
cascade_path = 'haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# 关键点检测
def get_landmarks(im):
    rects = cascade.detectMultiScale(im, 1.3, 5)
    x, y, w, h = rects[0]
    rect = dlib.rectangle(x, y, x + w, y + h)
    return np.matrix([[p.x, p.y] for p in predictor(im, rect).parts()])


# 在图像上显示关键点
def annotate_landmarks(im, landmarks):
    im = im.copy()
    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0, 1])
        cv2.putText(im, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=0.4, color=(0, 0, 255))
        cv2.circle(im, pos, 5, color=(0, 0, 255))
    return im


def get_lipfrom_image(im, landmarks):
    xmin = 1000
    xmax = 0
    ymin = 1000
    ymax = 0

    #  这是嘴唇区域
    for i in range(48, 67):
        x = landmarks[i, 0]
        y = landmarks[i, 1]
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    print("xmin", xmin)
    print("xmax", xmax)
    print("ymin", ymin)
    print("ymax", xmax)

    roiwidth = xmax - xmin
    roiheight = ymax - ymin

    roi = im[ymin:ymax, xmin:xmax, 0:3]
    if roiwidth > roiheight:
        dstlen = 1.5 * roiwidth
    else:
        dstlen = 1.5 * roiheight

    diff_xlen = dstlen - roiwidth
    diff_ylen = dstlen - roiheight

    newx = xmin
    newy = ymin
    imagerows, imagecols, channel = im.shape
    if newx >= diff_xlen / 2 and newx + roiwidth + diff_xlen / 2 < imagecols:
        newx = newx - diff_xlen / 2
    elif newx < diff_xlen / 2:
        newx = 0
    else:
        newx = imagecols - dstlen
    if newy > diff_ylen / 2 and newy + roiheight + diff_ylen / 2 < imagerows:
        newy = newy - diff_ylen / 2
    elif newy < diff_ylen / 2:
        newy = 0
    else:
        newy = imagerows - dstlen
    roi = im[int(newy):int(newy + dstlen), int(newx): int(newx + dstlen), 0:3]
    return roi


def listfile(rootdir):
    list_dirs = os.walk(rootdir)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(os.path.join(root, d))
        for f in files:
            fileid = f.split('.')[0]
            file_type = f.split('.')[1]
            file_path = os.path.join(root, f)
            try:
                im = cv2.imread(file_path, 1)
                landmarks = get_landmarks(im)
                show_im = annotate_landmarks(im, landmarks)
                roi = get_lipfrom_image(im, landmarks)
                roipath = file_path.replace('.' + file_type, '_mouth.png')

                # if im.shape[1] == 512 and im.shape[0] == 512:
                # cv2.imshow("keypoint", show_im)
                # cv2.waitKey(0)
                cv2.imshow("32", roi)
                cv2.waitKey(0)
                cv2.imwrite(roipath, roi)
                cv2.destroyAllWindows()
            except:
                print(file_path + " process error")
                continue


if __name__ == '__main__':
    path = 'img'
    listfile(path)

