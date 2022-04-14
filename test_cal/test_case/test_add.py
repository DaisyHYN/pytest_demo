#!/usr/bin/env python
# encoding: utf-8
"""
@author: HYN
@file: test_add.py
@time: 2022/4/14 18:38
@desc:
"""
import pytest
from test_cal.common.yamlLoad import read_yaml
from calculator import Calculator


class TestAdd:
    @pytest.mark.add
    @pytest.mark.p1
    @pytest.mark.parametrize("params", read_yaml("./data/add_format.yaml"))
    def test_format(self, params):
        """
        测试输入参数的长度
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.add(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 add 的 " + params["name"]

    @pytest.mark.add
    @pytest.mark.p1
    @pytest.mark.parametrize("params", read_yaml("./data/add_length.yaml"))
    def test_length(self, params):
        """
        测试输入参数的长度
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.add(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 add 的 " + params["name"]
        pass

    @pytest.mark.add
    @pytest.mark.p0
    @pytest.mark.parametrize("params", read_yaml("./data/add_cal.yaml"))
    def test_cal(self, params):
        """
        测试计算结果
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.add(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 add 的 " + params["name"]

    @pytest.mark.add
    @pytest.mark.p1
    @pytest.mark.parametrize("params", read_yaml("./data/add_precision.yaml"))
    def test_format(self, params):
        """
        测试计算结果的精度 跟随输入数据的精度
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.add(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 add 的 " + params["name"]