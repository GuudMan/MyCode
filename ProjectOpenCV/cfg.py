#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : cfg.py
# @Author  : 10285659
# @Date    : 2022/07/01
# @describe: 全局配置文件

import logging as log

# 日志配置
# LOG_FORMAT = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
# LOG_FILE = '../data/log_file/log_file.txt'
# log.basicConfig(level=log.INFO, format=LOG_FORMAT)

# 创建一个logger
import os
logger = log.getLogger()
logger.setLevel(log.INFO)
# 创建一个handler，用于写入日志文件
file_name = "./data/log_file/log_file.txt"
if not os.path.exists(file_name):
    os.makedirs(os.path.dirname(file_name))
fh = log.FileHandler(file_name, mode='w')
fh.setLevel(log.INFO)
fh.setFormatter(log.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'))
logger.addHandler(fh)
# 创建一个handler，输出到控制台
ch = log.StreamHandler()
ch.setLevel(log.INFO)
ch.setFormatter(log.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'))
logger.addHandler(ch)

base_path = 'data' + os.sep