#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-06-10 14:32
# @Author  : 狐狸糊涂
# @File    : copy_history.py.py
# @Software: PyCharm
import os
import shutil

# 获取路径
route = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取路径

# 报告目录
ALLURE_REPORT = route + r'\report_allure'
# 文件目录
ALLURE_RESULTS = route + r'\result'


def copy_history():
    start_path = os.path.join(ALLURE_REPORT, 'history')
    end_path = os.path.join(ALLURE_RESULTS, 'history')
    if os.path.exists(end_path):
        shutil.rmtree(end_path)
        print("复制上一运行结果成功！")
    try:
        shutil.copytree(start_path, end_path)
    except FileNotFoundError:
        print("allure没有历史数据可复制！")


if __name__ == "__main__":
    copy_history()
