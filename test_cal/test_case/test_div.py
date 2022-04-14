#!/usr/bin/env python
# encoding: utf-8
"""
@author: HYN
@file: test_div.py
@time: 2022/4/14 18:38
@desc:
"""
import pytest
from test_cal.common.yamlLoad import read_yaml
from calculator import Calculator


class TestDiv:
    @pytest.mark.div
    @pytest.mark.p1
    @pytest.mark.parametrize("params", read_yaml("./data/div_format.yaml"))
    def test_format(self, params):
        """
        测试输入参数的长度
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.div(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 div 的 " + params["name"]

    @pytest.mark.div
    @pytest.mark.p1
    @pytest.mark.parametrize("params", read_yaml("./data/div_length.yaml"))
    def test_length(self, params):
        """
        测试输入参数的长度
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.div(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 div 的 " + params["name"]
        pass

    @pytest.mark.div
    @pytest.mark.p0
    @pytest.mark.parametrize("params", read_yaml("./data/div_cal.yaml"))
    def test_cal(self, params):
        """
        测试计算结果
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.div(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 div 的 " + params["name"]

    @pytest.mark.div
    @pytest.mark.p1
    @pytest.mark.parametrize("params", read_yaml("./data/div_precision.yaml"))
    def test_format(self, params):
        """
        测试计算结果的精度
        1）有限小数结果尽量短。最多8位，超过则四舍五入
        2）无限小数精确到小数点后8位，四舍五入
        :param params: a,b,validate
        :return:
        """
        cal = Calculator()
        result = cal.div(params["data"]['a'], params["data"]['b'])
        assert params["validate"] == result, "方法 div 的 " + params["name"]
