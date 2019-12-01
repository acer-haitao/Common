# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 0001 下午 21:14
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : pylog.py
# @Software: PyCharm

import logging
from logging import handlers
import os
from colorama import Fore


def write_log(filename, level='info', when='D', backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
    '''
    参考:https://www.cnblogs.com/nancyzhu/p/8551506.html
    '''
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }
    PATH = os.path.split(os.path.realpath(__file__))[0] + "/log"
    if not os.path.exists(PATH):
        os.mkdir(PATH)

    logger = logging.getLogger(filename)
    format_str = logging.Formatter(fmt)
    logger.setLevel(level_relations.get(level))

    # 控制台输出
    sh = logging.StreamHandler()
    sh.setFormatter(format_str)

    # 文件写入 按照时间自动分割日志文件
    th = handlers.TimedRotatingFileHandler(filename='./log/%s' % filename, when=when, backupCount=backCount,encoding='utf-8')
    th.setFormatter(format_str)

    logger.addHandler(sh)
    logger.addHandler(th)
    return logger

if __name__ == '__main__':
    write_log(filename='info.log', level="debug").debug("2019年")