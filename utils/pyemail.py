#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: pyemail.py
# Author: yuhaitao
# mail: acer_yuhaitao@163.com
# Created Time: Mon 02 Dec 2019 08:21:51 PM CST
#########################################################################
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

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

def send_email(subject,to_user,content):
    print("send ....")
    host = readconfig.read_config("EMAIL", 'host')
    port = readconfig.read_config("EMAIL", 'port')
    user = readconfig.read_config("EMAIL", 'user')
    pwd = readconfig.read_config("EMAIL", 'pwd')
    try:
        print(host,port)
        smtpserver = smtplib.SMTP()
        smtpserver.connect(host,port)
        pylog.write_log(filename='info.log', level='info').info("邮件连接成功！")
        print("connect sucess!")
    except Exception as what:
        print("connect fail!")
        pylog.write_log(filename='error.log', level='error').error("邮件连接失败！")
        pass

    try:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(user, pwd)
        pylog.write_log(filename='info.log', level='info').info("邮件登录成功！")
    except Exception as what:
        pylog.write_log(filename='error.log', level='error').error("邮件登录失败！{}".format(what))

    # 邮件正文解决方案
    msg = MIMEText(content, 'plain', 'utf-8')  # 第二个参数不是format
    msg["Accept-Language"] = "zh-CN"
    msg["Accept-Charset"] = "ISO-8859-1,utf-8"


    msg['Subject'] = Header(subject,'utf-8')

    # 发件人
    msg['From'] = user

    # 收件人
    msg['To'] = to_user

    try:
        smtpserver.sendmail(user, to_user.split(','), msg.as_string())
        pylog.write_log(filename='info.log', level='info').info("邮件发送成功！")
    except Exception as what:
        pylog.write_log(filename='error.log', level='error').error("邮件发送失败！{}".format(what))
    smtpserver.quit()

if __name__ == '__main__':
    subject = "Hello world"
    content = "Good night！"
    # Fuck! 554, b'DT:SPM ---> must be the same mailbox?
    user = "acer_yuhaitao@163.com"
    print("hello world!")
    send_email(subject=subject,to_user=user,content=content)