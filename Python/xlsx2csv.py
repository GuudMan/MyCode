# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :xlxs转CSV文件,用在linux中，需要传递参数
import pandas as pd
import sys

if __name__ == '__main__':
    print(sys.argv)
    xlxs_file = pd.ExcelFile(sys.argv[1])
    tables = xlxs_file.sheet_names
    print(tables)
    for table in tables:
        print(table)
        data_header = pd.read_excel(xlxs_file, sheet_name=table, header=None, nrows=1)
        data_value = pd.read_excel(xlxs_file, sheet_name=table, header=None, nrows=5)
        data = data_header.append(data_value, ignore_index=True)
        data.to_csv("{0}/{1}.csv".format(sys.argv[2], table), index=False, header=False)