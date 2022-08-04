#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-16 19:54
# @Author  : 狐狸糊涂
# @File    : options.py
# @Software: PyCharm
"""
    浏览器配置项，主流浏览器包含Chrome、IE浏览器、Firefox浏览器、Edge浏览器等。
    这里对每个浏览器都进行了封装，需要使用某个浏览器时，只需要调用即可。
    ps：注意在调用时，需要安装与浏览器一致的driver 否则会报错。
"""
import time
import SafeDriver
from selenium import webdriver
import pytest


def Chrome_options():  # 设置chrome浏览器配置项
    try:
        options = webdriver.ChromeOptions()  # 创建chrome浏览器配置项
        options.page_load_strategy = 'eager'  # 页面加载策略  "normal", "eager", "none"
        options.add_argument('start-maximized')  # 浏览器最大化
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation', 'enable-logging'])  # 去掉浏览器提示自动化黄条,去掉控制台多余日志信息

        # 去掉账号密码弹出框
        prefs = dict()
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enable'] = False
        options.add_experimental_option('prefs', prefs)
        # 无头模式：不在桌面实现浏览器的运行，作为后台静默运行，虽然看不到，但是一切照旧。偶尔场景会有异常，但很少
        options.add_argument('--headless')

        # 去掉控制台多余信息。
        options.add_argument('--log_level=3')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
    except:
        options = SafeDriver.drivers.driver()
    return options


def Ie_Options():  # 设置Ie浏览器配置项
    try:
        options = webdriver.IeOptions()
        options.add_argument('--start-maximized')  # 浏览器最大化
    except:
        options = SafeDriver.drivers.driver()
    return options


def Firefox_Options():  # 设置火狐浏览器配置项
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')  # 浏览器最大化
    except:
        options = SafeDriver.drivers.driver()
    return options


def Edge_Options():  # 设置Edge浏览器配置项
    try:
        options = webdriver.EdgeOptions()  # 创建Edge浏览器配置项
        options.page_load_strategy = 'eager'  # 页面加载策略  "normal", "eager", "none"
        options.add_argument('start-maximized')  # 浏览器最大化
        # options.add_experimental_option('excludeSwitches',
        #                                 ['enable-automation', 'enable-logging'])  # 去掉浏览器提示自动化黄条,去掉控制台多余日志信息
        # 去掉账号密码弹出框
        prefs = dict()
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enable'] = False
        options.add_experimental_option('prefs', prefs)
        # 去掉控制台多余信息。
        options.add_argument('--log_level=3')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
    except:
        options = SafeDriver.drivers.driver()
    return options


# 运行代码内容尝试代码是否有误
@pytest.mark.skip(reason="调试内容")
def test_options():
    driver = webdriver.Chrome(options=Chrome_options())
    driver.get('http://www.baidu.com')
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    pytest.main(['-sv', 'options.py'])

