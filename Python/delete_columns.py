# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :删除CSV文件中的指定列

"""
实现思路： 删除CSV文件中的指定列
读取CSV文件
执行列删除操作
保存文件或将文件写入到一个新文件中
"""
import pandas as pd
import os


def drop_columns_csv(filepath1, filepath2):
    for root, dirs, files in os.walk(filepath1, topdown=False):
        for name in files:
            if ".csv" == name[-4:]:
                print("正在进行处理的文件：", name)
                fp = pd.read_csv(os.path.join(root, name), header=None, low_memory=False
                                 , encoding='utf-8')
                d = fp.drop([12, 16, 17], axis=1)
                """
                [12,16,17]:表示需要删除的列号，从0开始
                axis=1 表示删除列
                """
                d.to_csv(filepath2 + os.sep + name, header=None, index=False)
                print(name, "处理完毕")

if __name__ == '__main__':
    drop_columns_csv("文件路径1", "文件路径2")