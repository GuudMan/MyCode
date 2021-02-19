# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :CSV大文件切分为小文件
"""
python实现CSV大文件切分为小文件
实现思路：
1、 读取CSV文件
2、 创建新文件
3、 逐行读取
4、 计数，读到一定数量的行时，将文件写入到新文件中
5、 新文件添加后缀，新文件的命名从源文件中解析出来，后面添加index，splitext()函数返回的是
文件的前缀和后缀
"""
import pandas as pd
import os
import time


def new_sub_file(buf, srcfilename, header, index):
    """

    :param buf:
    :param srcfilename:
    :param header:
    :param index:
    :return:
    """
    # 得到源文件的前缀名
    [file_prefix, file_postfix] = os.path.splitext(srcfilename)
    name_new_file = file_prefix + '_' +str(index) + file_postfix
    # 新建文件
    new_fopen = open(name_new_file, 'w')
    try:
        new_fopen.writelines(header)
        new_fopen.writelines(buf)
        return index + 1
    finally:
        new_fopen.close()


def file_csv_split(filename, count):
    """

    :param filename:
    :param count:
    :return:
    """
    try:
        # 读取CSV文件
        fopen = open(filename, encoding='gbk')
        # 单独读取文件的头
        header = fopen.readline()
        # 创建缓存器
        buff = []
        sub_index = 1
        for file_line in fopen:
            buff.append(file_line)
            if len(buff) == count:
                # 文件达到指定的行数
                sub_index = new_sub_file(buff, file_line, header, sub_index)
                buff = []
        # 最后多余的部分，会从上面的循环中跳出来
        if len(buff) != 0:
            sub_index = new_sub_file(buff, filename, header, sub_index)
    finally:
        fopen.close()


if __name__ == '__main__':
    path = "文件路径,带文件名"
    file_csv_split(path, 1000)
