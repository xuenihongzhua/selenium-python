#coding:utf-8
import unittest
from pages.login_page import LoginPage
from selenium import webdriver
from common.base import Base
url = "http://120.77.156.30:8080/zentao/user-login.html"
'''
case1：输入错误的账户，正确的密码，点击登录
case2：输入错误的密码，正确的账户，点击登录
case3：不输入密码，只输入账户，点击登录
case4：不输入账户和密码，点击登录
case5：输入正确的账户和密码，点击登录
'''


class LoginTestCase(unittest.TestCase,Base):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_case = LoginPage(cls.driver)


    def setUp(self):
        self.driver.get(url)
        self.is_alert_present()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_case_01(self):
        self.login_case.input_user("admin1")
        self.login_case.input_pwd("123456.")
        self.login_case.click_login_button()
        result = self.login_case.get_login_name()
        self.assertTrue(result  =="")

    def test_case_02(self):
        self.login_case.input_user("admin")
        self.login_case.input_pwd("123456")
        self.login_case.click_login_button()
        result = self.login_case.get_login_name()
        self.assertTrue(result  == "")

    def test_case_03(self):
        self.login_case.input_user("admin")
        self.login_case.input_pwd("")
        self.login_case.click_login_button()
        result = self.login_case.get_login_name()
        self.assertTrue(result  == "")

    def test_case_04(self):
        self.login_case.input_user("")
        self.login_case.input_pwd("")
        self.login_case.click_login_button()
        result = self.login_case.get_login_name()
        self.assertTrue(result  =="")

    def test_case_05(self):
        self.login_case.input_user("admin")
        self.login_case.input_pwd("123456.")
        self.login_case.click_login_button()
        result = self.login_case.get_login_name()
        self.assertTrue(result  == "admin")



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()