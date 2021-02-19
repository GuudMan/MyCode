# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :p修改文件类型
"""
修改文件中的内容，一般是用在安装软件需要修改配置文件的时候，这个时候就可以使用这个脚本来修改了
具体思路：
首先新建一个文件new,然后逐行读取源文件，修改对应的行，将行写入到一个新文件中，删除源文件，将新文件重命名为源文件
"""
import os


def modify_file(path):
    """

    :param path:
    :return:
    """
    print("开始修改文件内容")
    os.chdir(path) # path为函数传入的参数，表示需要修改的文件路径，
    try:
        # 打开文件
        file_modify = open(path + os.sep +'filename.txt', 'r+')
        # 新建一个临时文件
        file_tmp = open(path + os.sep + 'filename_tmp.txt', 'w+')
    except FileNotFoundError:
        print("文件打开失败")
    else:
        # 文件没有打开错误的时候，就会执行else中的内容
        # 逐行读取
        file_lines = file_modify.readlines()
        # 注意这里有readline和readlines，一定要注意选择带s的，如果没有s，那么就是只能读取一行，而不是所有的
        # 逐行循环
        for line in file_lines:
            if 'memory' in line:
                line = 'memory_modify'
            if 'cluster' in line:
                line = 'cluster_modify'
            file_tmp.write(line)
        file_tmp.close()
        file_modify.close()
        # 删除源文件
        os.remove(path + os.sep + 'filename.txt')
        # 重命名
        os.rename(path + os.sep + 'filename_tmp.txt',path + os.sep + 'filename.txt')

