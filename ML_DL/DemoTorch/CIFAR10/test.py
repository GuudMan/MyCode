#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->test
# @Time      :2022/9/4 10:04
# @Author    :Peng neng
# @File      :test.py
# ===============================
import torch
import glob
import cv2
from PIL import Image
from torchvision import transforms
import numpy as np
from restnet import resnet


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

net = resnet()

net.load_state_dict(torch.load("D:/1Temp/project/pythonProject/DemoTorch/CIFAR10/models/1.pth"))


