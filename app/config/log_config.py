#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/20 20:36
# @Author: xk
# @File  : log_config.py

import os
import logging
from logging.handlers import RotatingFileHandler


def setup_log():
    """配置日志"""
    LOG_NAME = 'flask-demo.log'
    # 需要确保 {0}/logs/{1} 路径存在
    logfile = "{0}/logs/{1}".format(os.path.abspath('.'), LOG_NAME)
    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler(logfile, maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
