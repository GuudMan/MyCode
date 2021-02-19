# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :按照列名来删除列
"""
实现思路：
读取CSV文件
执行列删除操作
保存文件或写入到一个新文件中
"""
import pandas as pd
import os


def drop_columns(filename, filepath):
    # 读取CSV文件
    # 创建一个新的文件
    file_new = open(filepath + os.sep + 'tmp.csv', 'w')
    # 读取CSV文件
    fp = pd.read_csv(filename, low_memory=False,encoding='utf-8')
    col_list = list()
    for i in fp.columns:
        col_list.append(i)
    print("col_list的列表为：", col_list)
    print("fp为：", fp)
    # 删除名字为age的列
    d = fp.drop('age', axis=1)
    d.to_csv(file_new, header=False, index=False)


if __name__ == '__main__':
    drop_columns("文件路径1", "文件路径2")

    """
    注意： 删除列，fp.drop会返回删除后的fp,但是原先的fp仍然不会变， 如果需要将删除
    后的列写入到一个新文件中，这时drop删除函数需要用值来接收，然后用接收的值写入到to_csv指定的文件中
    """