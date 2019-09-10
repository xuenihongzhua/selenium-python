#coding:utf-8
from selenium import webdriver
import time
import unittest
url = "http://120.77.156.30:8080/zentao/user-login.html"

class LoginTest(unittest.TestCase):
    '''测试类说明：测试类'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        time.sleep(2)

    def get_login_username(self):
        try:
           t =  self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
           print(t)
           return t
        except:
            return ""

    def alert_exist(self):
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def test_01(self):
        '''用例说明：测试用例01'''
        self.driver.find_element_by_id("account").send_keys("wangqiang")
        self.driver.find_element_by_name("password").send_keys("123456.")
        self.driver.find_element_by_id("submit").click()
        time.sleep(3)

        #判断登录是否成功
        t = self.get_login_username()
        print("获取登录的结果：%s"%t)
        #断言
        self.assertTrue(t=="王强")

    def test_02(self):
        '''用例说明：测试用例02'''
        self.driver.find_element_by_id("account").send_keys("wangqiang22")
        self.driver.find_element_by_name("password").send_keys("1234567.")
        self.driver.find_element_by_id("submit").click()
        time.sleep(3)
         #判断登录是否成功
        t = self.get_login_username()
        print("获取登录的结果：%s"%t)
        #断言
        self.assertTrue(t=="")
        #判断登录是否成功
        #t =  self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
        #print(t)
        #断言
        #self.assertTrue(t=="王强")


    def tearDown(self):
        time.sleep(4)
        self.driver.delete_all_cookies() #清空所有的cookis
        self.driver.refresh()   #刷新页面
        self.alert_exist()   #alert处理
        self.driver.close()

    if __name__ =="__main__":
        unittest.main()



