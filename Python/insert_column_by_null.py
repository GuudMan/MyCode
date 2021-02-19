# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :2021年2月11日09:30:05
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :CSV文件中插入列，插入的列以空值填充
"""
实现在CSV文件中插入指定列
思路：
1. 读取CSV文件
2， 利用pandas.insert（序号，列名）插入一列空值
"""
import pandas as pd
import os
import sys


def insert_columns(filename):
    # 读取CSV文件
    fp = pd.read_csv(filename, encoding='utf-8')
    print("文件列名", type(fp.columns))
    if 'insert_columns' not in fp.columns:
        fp.insert(2, 'insert_columns', '', allow_duplicates=True)
        fp.to_csv(filename, index=False)


if __name__ == '__main__':
      insert_columns("文件路径")
