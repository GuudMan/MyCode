# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :����������ɾ����
"""
ʵ��˼·��
��ȡCSV�ļ�
ִ����ɾ������
�����ļ���д�뵽һ�����ļ���
"""
import pandas as pd
import os


def drop_columns(filename, filepath):
    # ��ȡCSV�ļ�
    # ����һ���µ��ļ�
    file_new = open(filepath + os.sep + 'tmp.csv', 'w')
    # ��ȡCSV�ļ�
    fp = pd.read_csv(filename, low_memory=False,encoding='utf-8')
    col_list = list()
    for i in fp.columns:
        col_list.append(i)
    print("col_list���б�Ϊ��", col_list)
    print("fpΪ��", fp)
    # ɾ������Ϊage����
    d = fp.drop('age', axis=1)
    d.to_csv(file_new, header=False, index=False)


if __name__ == '__main__':
    drop_columns("�ļ�·��1", "�ļ�·��2")

    """
    ע�⣺ ɾ���У�fp.drop�᷵��ɾ�����fp,����ԭ�ȵ�fp��Ȼ����䣬 �����Ҫ��ɾ��
    �����д�뵽һ�����ļ��У���ʱdropɾ��������Ҫ��ֵ�����գ�Ȼ���ý��յ�ֵд�뵽to_csvָ�����ļ���
    """