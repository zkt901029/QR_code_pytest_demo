#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-16 22:43
# @Author  : 狐狸糊涂
# @File    : main.py
# @Software: PyCharm
"""
    程序主入口
"""
import pytest
from base.Allure_modification import set_windos_title, get_json_data, write_json_data
import os
from base.copy_history import copy_history

if __name__ == '__main__':
    # 运行报告程序
    def run():
        pytest.main(['-n', '2', '--alluredir', './result', '--clean-alluredir'])
        os.system('copy environment.properties result\\environment.properties')
        # 复制报告路径
        copy_history()
        os.system('allure generate ./result/ -o ./report_allure/ --clean')
        # 自定义测试报告网页标题
        set_windos_title("祥康--二维码测试自动脚本")

        # 自定义测试报告标题
        report_title = get_json_data("祥康--二维码测试报告")
        write_json_data(report_title)

    # 运行新报告内容
    def run1():
        pytest.main(['--report=demo.html', '--title=祥康--二维码测试报告', '--tester=狐狸糊涂',
                     '--desc=二维码测试报告详情， ', '--template=2'])


    if __name__ == '__main__':
        # run1()
        run()
        # input('please input any key to exit')


