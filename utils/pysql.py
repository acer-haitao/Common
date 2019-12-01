# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 0001 下午 21:17
# @Author  : HT
# @Email   : acer_yuhaitao@163.com
# @File    : pysql.py
# @Software: PyCharm

import platform
WL = platform.system()
if WL == 'Windows':
    from utils import pylog
    from utils import readconfig
elif WL == 'Linux':
    import sys
    sys.path.append('./utils/pylog.py')
    sys.path.append('./utils/readconfig.py')
    import pylog,readconfig


import pymysql

log_level = "error"
log_filename = "erro.log"

def mysql_cnt(cnt_ip,cnt_port,cnt_user,cnt_pwd,cnt_db):
    '''
        Mysql数据库连接，python3.6.8
    '''
    try:
        conn = pymysql.connect(host=cnt_ip, port=3306, user=cnt_user, passwd=cnt_pwd, db=cnt_db, charset='UTF8')
        cur = conn.cursor()
        pylog.write_log(filename='info.log',level='info').info("数据库连接成功,用户名:{},数据库:{},端口:{}".format(cnt_user,cnt_db,cnt_port))
        return cur
    except Exception as e:
        pylog.write_log(filename=log_filename,level=log_level).error("错误信息:{}".format(e))
        pass

if __name__ == '__main__':

    cnt_ip = readconfig.read_config("DATABASE",'cnt_ip')
    cnt_port = readconfig.read_config("DATABASE", 'cnt_port')
    cnt_user = readconfig.read_config("DATABASE", 'cnt_user')
    cnt_pwd = readconfig.read_config("DATABASE", 'cnt_pwd')
    cnt_db = readconfig.read_config("DATABASE", 'cnt_db')
    print(cnt_ip, cnt_port, cnt_db, cnt_pwd, cnt_user)
    cur = mysql_cnt(cnt_ip=cnt_ip, cnt_port=3306, cnt_user=cnt_user, cnt_pwd=cnt_pwd, cnt_db=cnt_db)
    print(cur)
