#!/usr/bin/env python3
# coding:utf8

"""
@version:
@author :zhangh
@file   :py3demo.py
@time   :2017/10/10 17:18
@remark :
"""

import configparser

config = configparser.ConfigParser()

config.read('D:/Python36/zhangYs/config.ini')

print(config.get("monitor_server", "user"))

for section in config.sections():
    # print(section)
    for option in config.options(section):
        print(" ", option, "=", config.get(section, option))

