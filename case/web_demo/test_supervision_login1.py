# -*- coding: utf-8 -*- 
# @Time : 2023/2/15 16:42 
# @Author : wxy
# @File : test_supervision_login1.py

import os

import allure
import pytest

from public.read_data import read_pytestdata
from public.web_base import AutoRunCase


# 修改 setting  URL
class TestSupervisionLogin:
    @allure.feature("督办登录")  # 测试用例特性（主要功能模块）
    @allure.story("督办登录")  # 模块说明
    @allure.title("用户输入正确的用户名和正确的密码,登录失败")  # 用例标题
    @allure.description('用户输入正确的用户名和正确的密码,登录失败')  # 用例描述
    @pytest.mark.test_supervision_login1  # 用例标记
    @pytest.mark.parametrize('testdata', read_pytestdata(__file__, 'test_supervision_login_fail'))  # 测试数据
    def test_supervision_login_fail(self, goDriver, testdata):
        with allure.step('用户输入正确的用户名和正确的密码,登录成功'):
            login_page = AutoRunCase(goDriver)
            login_page.run(__file__, 'test_supervision_login_fail', test_date=testdata, forwait=1)
            # login_page.screen_shot('login')

    @allure.feature("督办登录")  # 测试用例特性（主要功能模块）
    @allure.story("督办登录")  # 模块说明
    @allure.title("用户输入正确的用户名和正确的密码,登录成功")  # 用例标题
    @allure.description('用户输入正确的用户名和正确的密码,登录成功')  # 用例描述
    @pytest.mark.test_supervision_login1  # 用例标记
    @pytest.mark.parametrize('testdata', read_pytestdata(__file__, 'test_supervision_login_success'))  # 测试数据
    def test_supervision_login_success(self, goDriver, testdata):
        with allure.step('用户输入正确的用户名和正确的密码,登录成功'):
            login_page = AutoRunCase(goDriver)
            login_page.run(__file__, 'test_supervision_login_success', test_date=testdata, forwait=1)
            # login_page.screen_shot('login')
