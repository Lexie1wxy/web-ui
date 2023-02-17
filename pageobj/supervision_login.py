# -*- coding: utf-8 -*-
# @File: login.py
# @Author: Wxy
# @E-mail: Wxy@163.com
# @Time: 2023/10/22  16:21

import os
import sys
sys.path.append(os.pardir)
from public import Web


class SupervisonLogin(Web):
    def input_username(self, username):
        """
        输入用户名
        :param username: 输入用户名
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, text=username)

    def input_password(self, password):
        """
        输入密码
        :param password: 输入密码
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, text=password)

    def click_login_button(self):
        """
        点击登录
        :return:
        """
        self.webexe(__file__, sys._getframe().f_code.co_name)

    def get_web_title(self, assertion, assertype):
        """
        获取网站标题并断言
        :return:
        """
        self.webexe(__file__, sys._getframe().f_code.co_name, assertion=assertion, assertype=assertype)





