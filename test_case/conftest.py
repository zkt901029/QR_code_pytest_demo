#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-06-08 8:58
# @Author  : 狐狸糊涂
# @File    : conftest.py
# @Software: PyCharm
import pytest
import allure
from base.options import Chrome_options
from selenium import webdriver


# 配置浏览器
@pytest.fixture(scope='class', autouse=True)
# @allure.step("调用配置浏览器信息")
def chrome_options():
    # 定义全局变量
    global driver
    # 初始化浏览器 并打开浏览器
    driver = webdriver.Chrome(options=Chrome_options())
    # 返回浏览器给到用例
    yield driver
    # 浏览器关闭
    driver.quit()


# 失败截图
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport():
    # 可以获取测试用例的执行结果，yield，返回一个result对象
    out = yield
    report = out.get_result()
    # 仅仅获取用例call阶段的执行结果，不包含setup和teardown
    if report.when == 'call':
        # 获取用例call执行结果为结果为失败的情况
        xfail = hasattr(report, "wasxfail")
        if(report.skipped and xfail) or (report.failed and not xfail):
            # 添加allure报告截图
            with allure.step("添加失败截图。。"):
                # 使用allure自带的添加附件的方法：三个参数分别为：源文件、文件名、文件类型
                allure.attach(driver.get_screenshot_as_png(), "失败截图",
                              allure.attachment_type.PNG)
