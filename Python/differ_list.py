# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :对字符串进行布尔运算，求交 差 并集
"""
提取两个文件中的字符串
找到二者的差异
实现思路:使用正则匹配，提取两个文件中的计数器，并实现去重和排序
使用布尔运算，完成计数器的差异性对比

"""

import re


def extract_word(filename):
    # 打开文件
    fopen = open(filename, 'r')
    # 匹配规则
    pattern = re.compile("D[0-9]{9}")
    # 切分规则
    pattern_split = re.compile('[,]|[+]|[*]|[/]')

    # 逐行读取
    file_lines = fopen.readlines()
    buffer = set()
    # 逐行循环
    for file_line in file_lines:
        # 对每一行进行切分
        line_cut = re.split(pattern_split, file_line)
        for c in line_cut:
            # 循环切分后的列表
            res_match = re.findall(pattern, c)
            # 将匹配的结果写入到集合中
            for c_c in res_match:
                buffer.add(c_c)
    return buffer


if __name__ == '__main__':
    counter_set1 = extract_word("文件路径1")
    counter_set2 = extract_word("文件路径2")

    # 对比差异
    counter_cross = counter_set2 - counter_set1
    """
    交集： &
    并集：|
    差集：-
    """
    # 将sort转为list进行排序
    list_sort = list(counter_cross)
    list_sort.sort()
    for i in list_sort:
        print(1)
