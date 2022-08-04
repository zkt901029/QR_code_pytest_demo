#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-06-07 13:38
# @Author  : 狐狸糊涂
# @File    : base_page.py
# @Software: PyCharm
"""
    基类: POM工具类，用于封装测试框架中运用到的方法。如后期有需要添加的，可以在该类中进行添加。
    目前封装的功能点包含：
         1.访问url
         2.创建driver对象（可以创建ChromeDriver，FirefoxDriver，EdgeDriver 等等）
         3.元素定位
         4.输入操作
         5.点击操作
         6.浏览器关闭操作
         7.显示等待
         8.强制等待
         9.句柄切换
        10.断言预期结果是否包含在实际结果内
        11.文本断言
        12.切换iframe
        13. 获取网页标题栏
        14. 标记元素定位，可以对定位的元素进行标红操作
        15. 后期有需要自己添加。。。。。
"""

import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    # 程序的url  'http://www.tl6.cc/1101/5013004213'
    # url = 'http://www.tl6.cc/'

    # 创建构造函数
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        # 用于绕过检验测试
        # self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #                 Object.defineProperty(navigator, 'webdriver', {
        #                   get: () => false
        #                 })
        #               """
        # })

    # url的访问
    def _open(self, url):
        self.driver.get(url)

    # 元素定位
    def locate(self, by, value):
        return self.driver.find_element(by, value)

    # 输入操作(对输入操作进行优化，先清除输入框内容的数据，并在做操作)
    def input_(self, by, value, txt):
        el = self.locate(by, value)
        el.clear()
        el.send_keys(txt)

    # 点击操作
    def click(self, by, value):
        self.locate(by, value).click()

    # 浏览器关闭
    def quit(self):
        self.driver.quit()

    # 显式等待
    def driver_wait(self, by, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(by, value), message='调用演示等待时，调用元素获取失败')

    # 强制等待
    def sleep_(self, time_):
        time.sleep(int(time_))

    # 断言预期结果是否包含在实际结果内
    def assert_almost_equal(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert expected in reality, '预期结果{0}不在实际结果{1}的范围内'.format(expected, reality)
            return True
        except:
            return False

    # 文本断言
    def assert_text(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert expected == reality, '文本断言预计结果{0}与文本实际结果{1}不相等'.format(expected, reality)
            return True
        except Exception as e:
            return False
            # print('文本断言失败：{}'.format(e))

    # 切换Iframe标签，可以通过值进行切换，也可以通过定位进行切换
    def switch_frame(self, by=None, value=None):
        if by is None:
            self.driver.switch_to.frame(value)
        else:
            self.driver.switch_to.frame(self.locate(by, value))

    # 获取title，获取网页标题栏
    def get_title(self):
        return self.driver.title

    # 标记元素定位，可以对定位的元素进行标红操作
    def Tab_Location(self, name, value):
        self.driver.execute_script("arguments[0].style.border='5px solid red'", self.driver.find_element(name, value))

    # 鼠标悬停
    def ActionChains(self, by, value):
        ActionChains(self, key).move_to_element(self.locate(by, value)).perform()




