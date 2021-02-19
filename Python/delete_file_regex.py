# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :利用正则表达式进行文件删除

import zipfile
import re
import pandas as pd
import os
import shutil

for root_zip, dirs_zip, files_zip in os.walk(dirname, topdown=False):
    for name_zip in files_zip:
        text = re.compile(".*[0-9]$")
        if text.match(name_zip.split('.')[0]):
            print("保留的文件为：", name_zip)
        else:
            print("删除的文件为：", os.path.join(root_zip, name_zip))
            os.remove(os.path.join(root_zip, name_zip))
