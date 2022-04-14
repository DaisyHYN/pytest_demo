#!/usr/bin/env python
# encoding: utf-8
"""
@author: HYN
@file: logger.py
@time: 2022/4/14 18:10
@desc:记录操作日志
      参考思路  将python自带的logging模块封装了一下，从配置文件读取并设置固定的logger
"""
import logging
import os
import time
import inspect
from logging import handlers


def get__function_name():
    # 获取正在运行函数(或方法)名称
    return inspect.stack()[1][3]

LOG_DIR = "../logs"

class Logs:
    __logger = None
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    @classmethod
    def get_logger(cls, level_file='info', level_stdout='error'):
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger('hyn')
            cls.__logger.setLevel(cls.level_relations.get(level_file))
            # os.mkdir(LOG_DIR)
            # log_path = BASE_DIR + os.sep + "log" + os.sep + "{}.log".format(time.strftime("%Y%m%d"))
            log_path = LOG_DIR + "/DMTest-{}.log".format(time.strftime("%Y%m%d"))
            f_handlers = logging.handlers.TimedRotatingFileHandler(
                filename=log_path, when="midnight", interval=1, backupCount=30, encoding="utf-8")
            # 获取流处理器，用于输出到控制台
            s_handlers = logging.StreamHandler()
            # 获取格式器
            formatter = logging.Formatter(
                "%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s:%(message)s)")
            # 设置文件处理器/流处理器的默认级别、格式
            f_handlers.setLevel(cls.level_relations.get(level_file))
            s_handlers.setLevel(cls.level_relations.get(level_stdout))
            f_handlers.setFormatter(formatter)
            s_handlers.setFormatter(formatter)
            # 将文件/流处理器 加入到日志处理器中
            cls.__logger.addHandler(f_handlers)
            cls.__logger.addHandler(s_handlers)
        return cls.__logger


if __name__ == '__main__':
    Logs.get_logger()