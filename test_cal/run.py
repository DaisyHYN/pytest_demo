#!/usr/bin/env python
# encoding: utf-8
import pytest
import os

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate "+os.getcwd()+"./report/data -o "+os.getcwd()+"./report/html --clean")
    os.system("allure open -h 127.0.0.1 -p 8888 " + os.getcwd() + "./report/html")
