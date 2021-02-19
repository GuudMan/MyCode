# !/usr/bin/env python3
# _*_coding:utf-8 _*_
# @Time        :2021年2月10日09:49:07
# @Author      :彭能
# @Email       :2663017379@qq.com
# @Name        :read_config_file
# @Software    :pyCharm
# @Description :日志功能类，可以打印info,warning ,error三类日志信息
import logging
from logging import handlers


class Logger(object):
    """
    日志级别关系映射
    """
    level_relations = {
        'debug': logging.EDBUGE,
        'info': logging.INFO,
        'warnning': logging.WARNNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }


    def __init__(self, filename, level='info', when = '0', backCount=3,
                 fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - '
                       '%(levelname)s:%(message)s'):
        self.logger = logging.getLogger(filename)
        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logger.setLevel(self.level_relations.get(level))
        # 输出到控制台
        sh = logging.StreamHandler()
        # 设置控制台输出格式
        sh.setFormatter(format_str)
        # 输出到文件中，指定间隔时间自动生成文件的处理器
        th = handlers.TimedRotatingFileHandler(filename, when=when,
                                               backupCount=backCount, encoding='utf-8')
        """
        实例化TimeRotatingFileHandlder
        interval是时间间隔，backCount是备份问阿金的个数，如果超过这个个数会自动删除，when是间隔的时间单位，
        单位有以下几种：
        时 分 秒 天 每星期 每天凌晨
        interval=0 代表星期一
        """
        # 设置文件写入的格式
        th.setFormatter(format_str)
        # 把对象加到logger中
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


# 实例化日志对象
log = Logger('test_log.txt', level = 'debug')
# 使用日志
log.logger.info("这是日志信息")
log.logger.warning("这是日志提醒")
log.logger.error("这是日志错误")

