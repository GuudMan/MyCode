# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :实现CSV文件列名定制，并使CSV文件的列按照额定的列表顺序进行排序

import pandas as pd
import os
import sys


def insert_columns(filename, col_lsit_add):
    # 读取CSV文件
    fp = pd.read_csv(filename, encoding='utf-8')
    # 插入需要添加的元素
    for i in col_lsit_add:
        insert = fp.insert(len(fp.columns), i, '', allow_duplicates=False)
        fp.to_csv(filename, index=False)
        print("新增的列名为：", insert)


def delete_columns(filename, col_list_add):
    # 第一步删除操作，注意所有的操作都是在原先的列表中进行的，最终需要原先的列表与理想的列表一致
    for i in col_list_add:
        fp = pd.read_csv(filename, encoding='utf-8')
        if i in fp:
            d = fp.drop(i, axis=1)
            print("删除的元素为：", i)
            print("删除后的d为：", d)
            print("删除后的fp为：", fp)
            # 写入到文件中
            d.to_csv(filename, index=False)
    print("多余列删除完毕")


def sort_columns(filename, col_list_new):
    fp = pd.read_csv(filename, encoding='utf-8')
    fp.to_csv(filename, encoding='utf_8_sig', index=False, columns=col_list_new)
    print("排序完毕")


if __name__ == '__main__':
    filename = "文件路径名"
    # 读取CSV文件
    fp = pd.read_csv(filename, encoding='utf-8')
    # 定义初始表格的表头
    col_list_old = list()
    # 定义需要的表格表头
    col_list_new = ['s1', 's2', 's3', 's4']
    # 得到表格的初始表头
    for i in fp.columns:
        col_list_old.append(i)

    # 得到并集
    col_list_intersection = set(col_list_new) | set(col_list_old)

    # 得到需要删除的元素的列表
    col_list_del = set(col_list_intersection) - set(col_list_new)

    # 得到需要添加的元素
    col_list_add = set(col_list_intersection) - set(col_list_old)

    # 删除列名
    delete_columns(filename, col_list_del)

    # 插入列名
    insert_columns(filename, col_list_add)

    # 重新排序
    sort_columns(filename, col_list_new)