#coding:utf-8
from common.base import Base
from selenium import webdriver
import time
url = "http://120.77.156.30:8080/zentao/user-login.html"

class LoginPage(Base): #继承
    #定位登录元素
    loc_user = ("id","account")
    loc_pwd = ("css selector","[name='password']")
    loc_button = ("xpath",".//*[@id='submit']")
    loc_keep_login = ("id","keepLoginon")
    loc_forget_pwd = ("link text","忘记密码")
    loc_get_username = ("xpath",".//*[@id='userMenu']/a")
    loc_forget_pwd_page = ("xpath","html/body/div[1]/div/div[2]/p/a")


    def input_user(self,username):
        self.sendKeys(self.loc_user,username)

    def input_pwd(self,password):
        self.sendKeys(self.loc_pwd,password)

    def click_login_button(self):
        self.click(self.loc_button)

    def keep_login(self):
        self.click(self.loc_keep_login)

    def forget_pwd_click(self):
        self.click(self.loc_forget_pwd)

    def get_login_name(self):
        username = self.get_text(self.loc_get_username)
        return username


    def alert_choice(self):
        alert_choice = self.is_alert_present()
        alert_choice.accpet()
        print(alert_choice)
        return alert_choice

    def is_refresh_exist(self):
        '''忘记密码页面，刷新按钮定位'''
        r = self.isElementExist(self.loc_forget_pwd_page)
        return r




    #登录功能,封装起来供其他人来调用
    def login(self,user="admin",pwd="123456.",keep_login=False):
        self.driver.get(url)
        self.input_user(user)
        self.input_pwd(pwd)
        if keep_login:self.keep_login()
        self.click(self.loc_button)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get(url)
    login = LoginPage(driver)
    time.sleep(3)
    login.get_login_name()