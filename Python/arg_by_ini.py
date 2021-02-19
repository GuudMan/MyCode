# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :2021年2月10日09:33:49
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :python脚本通过配置文件传递参数

# 读取配置文件传递参数
from configparser import ConfigParser


class Config():
    """
    读取配置文件
    """
    # 实例化ConfigParser对象
    config = ConfigParser.configParser()
    # 读取ini格式的配置文件，设定解码方式
    config.read("config.ini") # config中文件以键值对的形式存放变量，如下所示
    """
    [config]
    name = 'lisi'
    age = 23
    ...
    """
    # 获取姓名
    name = config.get('config', 'name')
# 实例化变量
config = Config()
# 得到用户名变量
user_name = config.name