# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 0001 下午 21:14
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : readconfig.py
# @Software: PyCharm
import configparser
import os

import platform
WL = platform.system()
if WL == 'Windows':
    from utils import pylog
    from utils import readconfig
elif WL == 'Linux':
    import sys
    sys.path.append('./utils/pylog.py')
    import pylog

log_level = "debug"
log_filename = "info.log"

def read_config(cf_name,param):
    '''
    cf_name:配置名称,param：对应参数
    '''
    #ini_dir = os.path.split(os.path.realpath(__file__))[0]
    ini_dir = os.environ.get("HOME") + "/workspace/"

    iniPath = os.path.join(ini_dir, "config.ini")
    log_level = "debug"
    log_filename="info.log"

    if os.path.exists(iniPath):
        #pylog.write_log(filename=log_filename, level=log_level).debug("配置文件：" + iniPath)
        cf = configparser.ConfigParser()
        cf.read(iniPath)
        value = cf.get(cf_name, param)
        return value
    else:
        pylog.write_log(filename=log_filename, level=log_level).warning("配置文件：" + iniPath+'不存在!')

if __name__ == '__main__':
    cnt_ip = read_config("DATABASE",'cnt_ip')
    pylog.write_log(filename=log_filename, level=log_level).debug("配置IP：" + cnt_ip)