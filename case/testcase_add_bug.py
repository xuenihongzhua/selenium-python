#coding:utf-8
import time
import unittest
from selenium import webdriver
from pages.add_bug_page import AddBugPage
from pages.login_page import LoginPage


url = "http://120.77.156.30:8080/zentao/user-login.html"


class TestAddBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(url)
        cls.bug = AddBugPage(cls.driver)
        cls.login = LoginPage(cls.driver)

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d %H:%M:%S")
        title = "测试标题"+timestr
        self.login.login()
        self.bug.enter_bug()
        self.bug.add_bug(title)
        result = self.bug.is_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ =="__main__":
    unittest.main()