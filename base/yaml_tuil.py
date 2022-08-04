#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-21 20:41
# @Author  : 狐狸糊涂
# @File    : yaml_tuil.py
# @Software: PyCharm
import yaml


class yamlUtil:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取YAML文件
    def read_yaml(self):
        with open(self.yaml_file, encoding="UTF-8",) as f:
            value = yaml.load(f, Loader=yaml.FullLoader)  # 文件流，加载方式
            print(value)
            return value


if __name__ == '__main__':
    yamlUtil(r"E:\python\QR_code_pytest_demo\data\bar_new_code2.yaml").read_yaml()
