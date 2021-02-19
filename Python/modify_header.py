# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :修改CSV文件表头
"""
原始的CSV文件是存放在压缩包中，所以先执行解压操作，然后修改CSV文件，最后执行压缩
"""
import os
import shutil
import zipfile
import pandas as pd

def unzip(zipfilename):
    """
    解压文件件
    :param zipfilename:
    :return:
    """
    print("即将解压文件夹为：", zipfilename)
    z = zipfile.ZipFile(zipfilename, 'r')
    dirname = zipfilename.split(".zip")[0]
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    z.extractall(dirname)
    z.close()
    print("dir name:", dirname)
    return dirname


def zip_file(zipdirname):
    """
    解压文件夹
    :param zipdirname:
    :return:
    """
    z = zipfile.ZipFile(zipdirname + ".zip", 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirname, filenames in os.walk(zipdirname):
        fpath = dirpath.replace(zipdirname, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
            z.close()
            print("压缩成功")


def deletedir(dir):
    shutil.rmtree(dir)
    print("文件删除完毕")


def modify_csv_header(pathdir):
    """
    修改文件表头
    :return:
    """
    # 定义新的表头
    my_columns_list = ['name', 'age', '列名1', '列名2', '列名3']
    # 读取压缩包文件
    # topdown=False：表示先遍历子目录，后返回根目录
    for root, dirs, files in os.walk(pathdir, topdown=False):
        for name in files:
            if '.zip' == name[-4:]:
                # 执行解压操作
                print("正在处理的压缩包为：", name)
                name_folder = unzip(os.path.join(root,name))
                # 读取压缩后的CSV文件
                for root_zip, dir_zips, file_zips in os.walk(name_folder):
                    for file_zip in file_zips:
                        # 因为一个压缩包中可能有多个CSV文件，所以需要循环
                        file_pd = pd.read_csv(os.path.join(root_zip, file_zip), low_memory=False,
                                                           encoding='utf-8')
                        # 更换列名
                        file_pd.columns = my_columns_list
                        file_pd.to_csv(os.path.join(root_zip, file_zip), index=False)
                        print("CSV文件修改完毕")
                    # 重新打包修改后的文件
                    zip_file(name_folder)
                    # 删除第一次解压后的文件夹
                    deletedir(name_folder)
            # 处理根目录下的CSV文件
            if '.csv' == name[-4:]:
                # 读取csv文件
                file_pd = pd.read_csv(os.path.join(root, name), low_memory=False, encoding='utf-8')
                file_pd.columns = my_columns_list
                # 写CSV文件
                file_pd.to_csv(os.path.join(root, name), index=False)
                # 修改完毕
                print("CSV表头文件修改完毕")


if __name__ == '__main__':
    path = "文件路径"
    modify_csv_header(path)
