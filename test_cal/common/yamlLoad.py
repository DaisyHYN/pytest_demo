#!/usr/bin/env python
# encoding: utf-8
"""
@author: HYN
@file: yamlLoad.py
@time: 2022/4/14 18:37
@desc: 操作yaml文件
"""
import yaml

# 读取yaml
def read_yaml(path) -> list:
    with open(path, mode='r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value

# 追加内容
def write_yaml(path,data):
    with open(path, mode='a', encoding='utf-8') as f:
        yaml.dump(data=data, stream=f, encoding='utf-8', allow_unicode=True)

# 清空yaml
def clear_yaml(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.truncate()




if __name__ == '__main__':
    a = read_yaml("../data/div_precision.yaml")