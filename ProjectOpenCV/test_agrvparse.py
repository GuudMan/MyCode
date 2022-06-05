#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :ProjectOpenCV->test_agrv
# @Time      :2022/6/1 22:25
# @Author    :Peng neng
# @File      :test_agrvparse.py
# ===============================
import argparse

# 获取所有参数
parser = argparse.ArgumentParser()

parser.add_argument("number1", help="第一个参数", type=int)  # 第一个参数

parser.add_argument("number2", help="第二个参数", type=int)

# 解析所有参数
args = parser.parse_args()

print("第一个参数", args.number1)
print("第2个参数", args.number2)
print("所有参数", args)