# -*- coding: utf-8 -*- 
# @Time : 2023/2/15 14:51 
# @Author : wxy
# @File : test_supervision_login.py
import allure
import pytest

from pageobj.supervision_login import SupervisonLogin
from public import read_pytestdata


class TestSupervisionLogin:
    @allure.feature("督办登录")  # 测试用例特性（主要功能模块）
    @allure.story("督办登录")  # 模块说明
    @allure.title("用户输入正确的用户名和正确的密码,登录成功")  # 用例标题
    @allure.description('用户输入正确的用户名和正确的密码,登录成功')  # 用例描述
    @pytest.mark.test_supervision_login  # 用例标记
    @pytest.mark.parametrize('username, password', read_pytestdata(__file__, 'test_supervision_login_success'))  # 测试数据
    def test_supervision_login_success(self, goDriver, username, password):
        login_page = SupervisonLogin(goDriver)
        with allure.step('输入用户名'):
            login_page.input_username(username)
        with allure.step('输入密码'):
            login_page.input_password(password)
        with allure.step('点击登录'):
            login_page.click_login_button()
            login_page.sleep(3)
            search_relust = login_page.screen_shot('search')