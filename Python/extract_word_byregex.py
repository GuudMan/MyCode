# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :����
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :��ȡ�ı��е��ض��ַ���
"""
��������ȡ����������D��ͷ�������9λ���ֵ��ַ���
"""
import re


def extrac_word(filename):
    # ��ȡ�ļ�
    try:
        fopen = open(filename, 'r', encoding='gbk')
        print(fopen)
        fopen_new = open(filename.split('.')[0] + 'word.txt', 'w')
        # fopen_new ��ʾ��һ�����ļ������ڴ����ȡ�ļ�����
        # ��������ƥ����
        text = re.recompile("D[0-9]{9}")
        # �������зֹ���
        text_split = re.compile('[,]|[+]|[*]|[/]') # |��ʾ��[]�а��������з�����
        k = 1
        # set�е�Ԫ�ز����ظ�
        buffer = set()
        # ���ж�ȡ
        file_lines = fopen.readlines()
        for i in file_lines:
            # ��ÿһ�н����з�
            # ��һ������Ϊ�з��������ڶ�������Ϊ��Ҫ�зֵĶ���
            line_cut = re.split(text_split, i)
            for j in line_cut:
                res_match = re.findall(text, j)
                for k in res_match:
                    print(k)
                    buffer.add(k)

        print("set ���ϣ�", buffer)
        # set ���������ܣ�������Ҫ��setתΪlist
        buffer_list = list(buffer)
        # ����
        buffer_list.sort()
        for c in buffer_list:
            print(c)
            fopen_new.write(c + '\n')

    finally:
        fopen.close()
        fopen_new.close()

    if __name__ == '__main__':
        extrac_word("��Ҫ��ȡ���ļ���·��")