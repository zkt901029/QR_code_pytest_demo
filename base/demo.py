#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-06-09 16:16
# @Author  : 狐狸糊涂
# @File    : demo.py
# @Software: PyCharm
from SafeDriver.drivers import driver, option


option.headless = True
dr = driver()
dr.get("https://www.baidu.com")
dr.quit()