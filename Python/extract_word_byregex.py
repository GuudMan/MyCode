# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :提取文本中的特定字符串
"""
案例，提取文中所有以D开头，后面带9位数字的字符串
"""
import re


def extrac_word(filename):
    # 读取文件
    try:
        fopen = open(filename, 'r', encoding='gbk')
        print(fopen)
        fopen_new = open(filename.split('.')[0] + 'word.txt', 'w')
        # fopen_new 表示打开一个新文件，用于存放提取的计数器
        # 定义正则匹配项
        text = re.recompile("D[0-9]{9}")
        # 定义行切分规则
        text_split = re.compile('[,]|[+]|[*]|[/]') # |表示或，[]中包含的是切分条件
        k = 1
        # set中的元素不会重复
        buffer = set()
        # 逐行读取
        file_lines = fopen.readlines()
        for i in file_lines:
            # 对每一行进行切分
            # 第一个参数为切分条件，第二个参数为需要切分的对象
            line_cut = re.split(text_split, i)
            for j in line_cut:
                res_match = re.findall(text, j)
                for k in res_match:
                    print(k)
                    buffer.add(k)

        print("set 集合：", buffer)
        # set 中无排序功能，所以需要将set转为list
        buffer_list = list(buffer)
        # 排序
        buffer_list.sort()
        for c in buffer_list:
            print(c)
            fopen_new.write(c + '\n')

    finally:
        fopen.close()
        fopen_new.close()

    if __name__ == '__main__':
        extrac_word("需要提取的文件的路径")