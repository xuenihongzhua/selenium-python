#coding:utf-8
from common.base import Base



class NewAddBugPage(Base):
    #新增bug统计
    loc_new_bug = ("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def new_add_bug_account(self,_text):
        #验证bug是否提交成功
        n = self.is_text_in_element(self.loc_new_bug,_text)
        print(n)
        return n




if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Firefox()
    addbug = NewAddBugPage(driver)
    addbug.new_add_bug_account("新增bug")