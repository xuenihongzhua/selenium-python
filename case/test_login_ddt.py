import unittest
from pages.login_page import LoginPage
from selenium import webdriver
from common.base import Base
import ddt
from common.read_excel import ReadExcel
import os

url = "http://120.77.156.30:8080/zentao/user-login.html"
'''
case1：输入错误的账户，正确的密码，点击登录
case2：输入错误的密码，正确的账户，点击登录
case3：不输入密码，只输入账户，点击登录
case4：不输入账户和密码，点击登录
case5：输入正确的账户和密码，点击登录
'''
'''testdatas = [
    {"user":"admui","pwd":"123456.","expect":"result"},
    {"user":"admin","pwd":"123456","expect":"result"},
    {"user":"admin","pwd":"","expect":"result"},
    {"user":"","pwd":"","expect":"result"},
    {"user":"admin","pwd":"123456.","expect":"result"}
    ]'''
#路径不能写死，不然后面有人要调用的时候就找不到这个文件，这个时候就需要引入os模块，一层一层的往上去找到这个文件
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath,"commom","datas.xlsx")  #join是连接工程路径下的common下的datas
print(filepath)
data = ReadExcel(filepath)
testdatas = data.dict_data()
print(testdatas)

@ddt.ddt
class LoginTestCase(unittest.TestCase,Base):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_c = LoginPage(cls.driver)
        cls.driver.get(url)

    def setUp(self):
        self.driver.get(url)
        self.is_alert_present()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_case(self,user,pwd,expect):
        self.login_c.input_user(user)
        self.login_c.input_pwd(pwd)
        self.login_c.click_login_button()
        result = self.login_c.get_login_name()
        self.assertTrue(result != expect)

    @ddt.data(*testdatas)
    def test_case(self,data):
        print("--------------start----------------")
        print("测试数据:%s"%data)
        self.login_case(data["user"],data["pwd"],data["expect"])
        print("————————end————————")
    '''
    def test_case_02(self):
        print("--------------start----------------")
        testdatas2 = testdatas[1]
        self.login_case(testdatas2["user"],testdatas2["pwd"],testdatas2["expect"])
        print("————————end————————")

    def test_case_03(self):
        print("--------------start----------------")
        testdatas3 = testdatas[2]
        self.login_case(testdatas3["user"],testdatas3["pwd"],testdatas3["expect"])
        print("————————end————————")

    def test_case_04(self):
        print("--------------start----------------")
        testdatas4 = testdatas[3]
        self.login_case(testdatas4["user"],testdatas4["pwd"],testdatas4["expect"])
        print("————————end————————")
    def test_case_05(self):
        print("--------------start----------------")
        testdatas5 = testdatas[4]
        self.login_case(testdatas5["user"],testdatas5["pwd"],testdatas5["expect"])
        print("————————end————————")
    '''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ =="__main__":
    unittest.main()