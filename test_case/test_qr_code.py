#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-06-07 21:14
# @Author  : 狐狸糊涂
# @File    : test_qr_code.py
# @Software: PyCharm
"""
    添加二维码，并验证流程是否正确
"""
import os
import time
import pytest
from page_object.qr_code_page import QrPage
from base.yaml_tuil import yamlUtil


class Test_QR_login:
    route = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取路径


    # 用例重跑  重跑3次，等待1秒
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    # 调用特使登录方法，查看钢瓶信息，充装信息
    @pytest.mark.parametrize("args",  yamlUtil(route+r"\data\bar_new_code2.yaml").read_yaml())
    def test_01_login(self, args, chrome_options):
        self.driver = chrome_options
        lp = QrPage(self.driver)

        # 登录操作验证
        lp.login(args["data"][0]['url'], args["data"][1]['barcode'], args["data"][2]['confirm'])

        # 钢瓶信息验证
        lp.cylinder_information(args["data"][3]['cylinder_ID'], args["data"][2]['confirm'], args["data"][1]['barcode'],
                                args["data"][5]['cylinder_type'])

        # 充装信息验证
        lp.filling_information(args["data"][4]['filling'], args["data"][2]['confirm'], args["data"][5]['cylinder_type'],
                               args["data"][1]['barcode'])

    # # 用例重跑  重跑3次，等待1秒
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    # 调用普通登录方法 只看页面显示内容是否正常
    @pytest.mark.parametrize("args", yamlUtil(route+r"\data\bar_new_code1.yaml").read_yaml())
    def test_02_login(self, args, chrome_options):
        self.driver = chrome_options
        lp = QrPage(self.driver)
        lp.login(args["data"][0]['url'], args["data"][1]['barcode'], args["data"][2]['confirm'])

    # 用例重跑  重跑3次，等待1秒
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    # 调用特使登录方法，查看钢瓶信息，充装信息，配送信息
    @pytest.mark.parametrize("args",  yamlUtil(route+r"\data\bar_new_code.yaml").read_yaml())
    def test_03_login(self, args, chrome_options):
        self.driver = chrome_options
        lp = QrPage(self.driver)

        # 登录操作验证
        lp.login(args["data"][0]['url'], args["data"][1]['barcode'], args["data"][2]['confirm'])

        # 钢瓶信息验证
        lp.cylinder_information(args["data"][3]['cylinder_ID'], args["data"][2]['confirm'], args["data"][1]['barcode'],
                                args["data"][5]['cylinder_type'])

        # 充装信息验证
        lp.filling_information(args["data"][4]['filling'], args["data"][2]['confirm'], args["data"][5]['cylinder_type'],
                               args["data"][1]['barcode'])

        # 配送信息验证
        lp.delivery_information(args["data"][6]['delivery'], args["data"][2]['confirm'])


        # # 安全须知验证
        # lp.safety_instructions(args["data"][10]['safety'], args["data"][11]['safety_ID'])
        # time.sleep(3)
        #
        # # 企业宣传验证
        # lp.enterprise_publicity(args["data"][12]['enterprise'], args["data"][13]['enterprise_ID'])
        # time.sleep(3)
        #
        # # 一键订气验证
        # lp.gas_fixation(args["data"][14]['gas_fixation'], args["data"][15]['gas_fixation_ID'])
        # time.sleep(3)


# 调试
if __name__ == '__main__':
    pytest.main(['-sv', 'test_qr_code.py'])
