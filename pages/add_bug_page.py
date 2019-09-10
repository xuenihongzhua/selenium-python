#coding:utf-8
from common.base import Base
from selenium import webdriver
import time
url = "http://120.77.156.30:8080/zentao/user-login.html"

class AddBugPage(Base): #继承
    '''
    #定位登录元素
    loc1 = ("id","account")
    loc2 = ("css selector","[name='password']")
    loc3 = ("xpath",".//*[@id='submit']")
    '''

    #添加BUG
    loc_test = ("xpath",".//*[@id='mainmenu']/ul/li[4]/a")
    loc_bug = ("link text","Bug")
    loc_addbug = ("xpath",".//*[@id='createActionMenu']/a/i")
    loc_trunk = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_choice_trunk = ("xpath",".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_title = ("id","title")
    #有iframe需要先进行切换
    loc_body = ("class name","article-content") #副文本通过body来定位
    loc_save = ("id","submit")#保存提交

    '''
    #登录功能
    def login(self,user="admin",pwd="123456."):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,pwd)
        self.click(self.loc3)
    '''
    #进入测试页面
    def enter_bug(self):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
    #填写和提交bug
    def add_bug(self,title):
        self.click(self.loc_trunk)
        self.click(self.loc_choice_trunk)
        self.sendKeys(self.loc_title,title)
        frame = self.find_element(self.loc_body)
        self.driver.switch_to.frame(frame)           #切换到iframe
        strtime = time.strftime("%Y_%m_%d %H:%M:%S")
        self.sendKeys(self.loc_title,title+strtime)
         #输入内容
        body ="【操作步骤】：XXX" \
              "【预期结果】：XXXXX" \
              "【实际结果】：XXX"

        self.sendKeys(self.loc_body,body)
        self.driver.switch_to.default_content()  #切换出iframe
        self.click(self.loc_save)   #提交Bug



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get(url)
    bug = AddBugPage(driver)
    bug.enter_bug()
    bug.add_bug("测试标题")














