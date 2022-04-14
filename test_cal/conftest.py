#!/usr/bin/env python
# encoding: utf-8
"""
@author: HYN
@file: conftest.py
@time: 2022/4/14 18:12
@desc:  固件函数，设置前后置和夹具, 实现全局共享调用
"""
import pytest


@pytest.fixture(scope="session", autouse=True)
def start_session():
    """
    测试整体执行开始/结束阶段，打印：测试开始/结束
    :return:
    """
    print("测试开始")
    yield
    print("\n测试结束")


@pytest.fixture(scope="function", autouse=True)
def start_case():
    """
    每条用例执行开始/结束阶段，打印：计算开始/结束
    :return:
    """
    print("计算开始")
    yield
    print("\t计算结束")

