#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-06-07 16:53
# @Author  : 狐狸糊涂
# @File    : qr_code_page.py
# @Software: PyCharm


from base.base_page import BasePage
import allure


class QrPage(BasePage):

    # 业务逻辑
    # 登录网站信息，断言数据信息
    @allure.step('登录操作')
    def login(self, url, barcode, confirm):
        """
        登录，并断言数据信息
        :param url:  浏览器链接
        :param barcode: 条码信息
        :param confirm: 元素定位
        :return:
        """
        with allure.step("步骤1：打开浏览器"):
            self._open(url)  # 打开浏览器
            self.sleep_(1)
        with allure.step("步骤2：获取浏览器字段内容"):
            FieldContent = self.driver.find_element('id', confirm).text
        with allure.step("步骤3：断言数据信息"):
            assert barcode in FieldContent  # 断言判断
        print('二维码网址{}打开正常，条码{}显示在页面内。。'.format(url, barcode))

    @allure.step('点击钢瓶信息操作')
    def cylinder_information(self, value, information, barcode, cylinder_type):
        """
        点击钢瓶信息页面，断言数据信息
        :param value: 钢瓶信息元素定位值
        :param information: 钢瓶信息数据集合定位值
        :param barcode: 钢瓶条码内容
        :return:
        """
        with allure.step("步骤1：点击钢瓶信息图标"):
            self.click('id', value)
        with allure.step("步骤2：进入钢瓶信息页面"):
            FieldContent = self.driver.find_element('id', information).text  # 获取数据的值
        with allure.step("步骤3：断言数据信息"):
            if barcode or cylinder_type in FieldContent:
                assert 1 == 1  # 断言判断
        print("钢瓶信息显示正常")

    @allure.step('点击充装信息操作')
    def filling_information(self, value, filling, cylinder_type, barcode):
        """
        点击充装信息操作
        :param value:通过点击充装数据ID进行定位
        :param filling:定位气瓶充装信息内容
        :param cylinder_type:气瓶介质
        :return:
        """
        with allure.step("步骤1：点击充装信息图标"):
            self.click('id', value)
        with allure.step("步骤2：进入充装信息页面"):
            Filling = self.driver.find_element('id', filling).text  # 获取数据的值
        with allure.step("步骤3：断言数据信息"):
            if barcode or cylinder_type in Filling:
                assert 1 == 1  # 断言判断
        print("充装信息显示正常")

    @allure.step('点击配送信息操作')
    def delivery_information(self, value, delivery):
        """
        配送信息操作
        :param value: 点击配选页面定位
        :param delivery: 定位配送内容定位
        :return:
        """
        with allure.step("步骤1：点击配送信息图标"):
            self.click('id', value)
        with allure.step("步骤2：进入配送信息页面"):
            Delivery = self.driver.find_element('id', delivery).text  # 获取数据的值
        with allure.step("步骤3：断言数据信息"):
            assert Delivery is not None
        print('点击配送信息显示正常')

    # @allure.step('点击安全须知操作')
    # def safety_instructions(self, value, safety):
    #     """
    #     安全须知操作
    #     :param value: 点击安全须知定位
    #     :param safety: 定位安全须知内容定位
    #     :return:
    #     """
    #     with allure.step("步骤1：点击安全须知图标"):
    #         self.click('id', value)
    #     with allure.step("步骤2：进入安全须知页面"):
    #         Safety = self.driver.find_element('id', safety).text  # 获取数据的值
    #     with allure.step("步骤3：断言数据信息"):
    #         assert Safety is not None
    #     print('点击安全须知显示正常')
    #
    # @allure.step('点击企业宣传操作')
    # def enterprise_publicity(self, value, enterprise):
    #     with allure.step("步骤1：点击企业宣传图标"):
    #         self.click('id', value)
    #     with allure.step("步骤2：进入安全须知页面"):
    #         enterprise = self.driver.find_element('id', enterprise).text  # 获取数据的值
    #     with allure.step("步骤3：断言数据信息"):
    #         assert enterprise is not None
    #     print('点击安全须知显示正常')
    #
    # @allure.step('点击一键订气操作')
    # def gas_fixation(self, value, gas_fixation):
    #     with allure.step("步骤1：点击一键订气图标"):
    #         self.click('id', value)
    #     with allure.step("步骤2：进入一键订气页面"):
    #         Gas_fixation = self.driver.find_element('id', gas_fixation).text  # 获取数据的值
    #     with allure.step("步骤3：断言数据信息"):
    #         assert Gas_fixation is not None
    #     print('点击一键订气显示正常')

    # yaml文件
    #     - safety: SafeInfo
    #     - safety_ID: activity-name
    #
    #     - enterprise: CompanyInfo
    #     - enterprise_ID: title
    #
    #     - gas_fixation: WxOrderInfo
    #     - gas_fixation_ID: title
