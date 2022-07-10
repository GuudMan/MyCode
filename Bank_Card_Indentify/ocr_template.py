#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :银行卡号识别->ocr_template
# @Time      :2022/7/10 19:59
# @Author    :Peng neng
# @File      :ocr_template.py
# ===============================
import cv2
import numpy as np
base_path = './img/'

if __name__ == '__main__':
    card_Gray = cv2.imread('./img/bank_card41.jpg', 0)
    card_Gray4 = cv2.resize(card_Gray, (4*card_Gray.shape[1], 4*card_Gray.shape[0]))
    # cv2.imshow("card_Gray", card_Gray)
    # cv2.imshow("card_Gray4", card_Gray4)

    # 自适应阈值筛选
    adaptive_threshold = cv2.adaptiveThreshold(card_Gray4, 255,
                                               cv2.ADAPTIVE_THRESH_MEAN_C,
                                               cv2.THRESH_BINARY_INV, 13, 3)
    # cv2.imshow("adaptive_threshold", adaptive_threshold)

    # 轮廓筛选
    contours, hierarchy = cv2.findContours(adaptive_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 轮廓面积小于一定阈值，就填充黑色
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < 160:
            adaptive_threshold = \
                cv2.drawContours(adaptive_threshold, contours, i, (0, 0, 0), -1)  # 厚度为-1表示填充模式
    # cv2.imshow("adaptive_threshold2", adaptive_threshold)

    kernel = np.ones((15, 15), dtype=np.uint8)
    # 黑帽处理
    blackhat = cv2.morphologyEx(adaptive_threshold, cv2.MORPH_BLACKHAT, kernel)
    # cv2.imshow("blackhat", blackhat)
    # 开运算
    kernel = np.ones((3, 3), dtype=np.uint8)
    opening = cv2.morphologyEx(blackhat, cv2.MORPH_OPEN, kernel)
    # cv2.imshow("opening", opening)

    # 再次找出所有轮廓
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 通过外接矩形与长宽比的限制，就可去除噪音
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        aspect_ratio = float(w) / h
        area = w * h
        if area < 1800 or area > 6000:
            erosion = cv2.drawContours(opening, contours, i, (0, 0, 0), -1)
        else:
            if aspect_ratio > 0.7 or aspect_ratio < 0.5:
                erosion = cv2.drawContours(opening, contours, i, (0, 0, 0), -1)
    # cv2.imshow("opening2", opening)

    # 将目标图片加粗
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    cv2.imshow('dilation', dilation)

    # 获取模板图片
    numTemplate_GRAY = cv2.imread('./img/bankCardNumTemplate.jpg', 0)
    ret, numTemplate_GRAY = cv2.threshold(numTemplate_GRAY, 200, 255, cv2.THRESH_BINARY)
    # cv2.imshow("numTemplate_GRAY", numTemplate_GRAY)

    # 检测目标数字
    # 轮廓排序函数
    def sequence_contours(image, width, height):
        contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 定义存储外接矩形参数的矩阵
        n = len(contours)
        RectBoxes0 = np.ones((n, 4), dtype=int)
        for i in range(n):
            RectBoxes0[i] = cv2.boundingRect(contours[i])

        RectBoxes = np.ones((n, 4), dtype=int)
        # 将第i行的x坐标与其余比较, 按照x大小进行排序
        for i in range(n):
            sequence = 0
            for j in range(n):
                if RectBoxes0[i][0] > RectBoxes0[j][0]:
                    sequence += 1
            RectBoxes[sequence] = RectBoxes0[i]

        # 将外接轮廓的参数转为对应的单个图片
        ImgBoxes = [[] for i in range(n)]
        for i in range(n):
            x, y, w, h = RectBoxes[i]
            ROI = image[y: y+h, x: x+w]
            ROI = cv2.resize(ROI, (width, height))
            # 重置尺寸后二值化处理
            thresh_val, ROI = cv2.threshold(ROI, 200, 255, cv2.THRESH_BINARY)
            ImgBoxes[i] = ROI

        return RectBoxes, ImgBoxes

    # 模板
    RectBoxes_Temp, ImgBoxes_Temp = sequence_contours(numTemplate_GRAY, 50, 80)
    print(RectBoxes_Temp)
    # cv2.imshow("ImgBoxes_Temp[1]", ImgBoxes_Temp[1])

    # 目标图片
    RectBoxes, ImgBoxes = sequence_contours(dilation, 50, 80)
    # cv2.imshow("ImgBoxes_Temp[1]", ImgBoxes[1])

    # 进行模板匹配
    result = []
    for i in range(len(ImgBoxes)):
        score = np.zeros(len(ImgBoxes_Temp), dtype=int)
        for j in range(len(ImgBoxes_Temp)):
            score[j] = cv2.matchTemplate(ImgBoxes[i], ImgBoxes_Temp[j], cv2.TM_SQDIFF)
        min_val, max_val, min_indx, max_indx = cv2.minMaxLoc(score)
        result.append(min_indx[1])
    print(result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()