#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->utils
# @Time      :2022/9/25 21:53
# @Author    :Peng neng
# @File      :utils.py
# ===============================
import re
import unicodedata
from langconv import *

def unicode2Ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )


def normalizeString(s):
    """
    lowcase, trim, and remove non-letter characters
    :param s:
    :return:
    """
    s = unicode2Ascii(s.lower().strip())
    s = re.sub("([.!?])", "\1", s)
    s = re.sub("[^a-zA-Z]+", " ", s)
    return s

def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line
