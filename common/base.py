#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select  #只有选项是option的时候，才能用select方法
from selenium.webdriver.support import expected_conditions as EC  #EC中有16中常见的元素判断方法
from selenium.webdriver.common.action_chains import ActionChains


class Base():
    '''初始化'''
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.3
        self.driver.maximize_window()

    def find_element(self,locator):   #形参放前面，实参放后面
        '''locator('id','wd')定位元素传入属性id、classname、linktext xpath、css等'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","value")')
        else:
            print("正在定位的元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_element(*locator))
            return ele

    def find_elements(self,locator):
        '''定位一组元素'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型：loc = ("id","value")')
        else:
            print("正在定位的元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x:x.find_elements(*locator))
            return eles

    #新方法
    def find_element_new(self,locator):
        ele1 = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele1


    def is_title(self,_title):
        '''判断title是否存在，结果是bool类型'''
        try:
            t = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return t
        except:
            return False

    def is_title_contains(self,_title):
        '''判断title是否包含某些字符，结果是bool类型'''
        try:
            t = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return t
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''判断元素文本中的内容，结果是bool类型'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,value):
        '''判断元素属性value的值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False

    def is_alert_present(self):
        '''判断当前是否有alert弹窗'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            print(result)
            return result
        except:
            return False

    def js_scroll_end(self):
        '''滚动到底部'''
        js_height = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_height)

    def js_scroll_top(self):
        '''回到顶部'''
        js_top = "window.scrollTo(0,0)"
        self.driver.execute_script(js_top)

    def js_focus(self,locator):
        '''聚焦元素,最实用的方法'''
        target = self.find_element(locator)
        self.driver.execute_script("argument[0].scrollIntoView();",target)

    def select_by_index(self,locator,index=0):
        '''通过索引定位，index是索引第几个，从0开始，为默认第一个'''
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性定位'''
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过text文本值定位'''
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)


    def sendKeys(self,locator,text):
        '''输入事件'''
        ele = self.find_element(locator)
        ele.send_keys(text)
        return ele

    def click(self,locator):
        '''点击事件'''
        ele = self.find_element(locator)
        ele.click()
        return ele

    def move_to_mouse(self,locator):
        '''鼠标悬停操作'''
        ele = self.find_element(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def isSelected(self,locator):
        '''判断元素是否被选中'''
        self.find_element(locator)
        r = self.isSelected(locator)
        return r

    def get_text(self,locator):
        '''获取文本'''
        try:
            t = self.find_element(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ''

    def get_login_result(self,locator,_text):
        '''获取登录结果'''
        result = self.is_text_in_element(locator,_text)
        return result

    def isElementExist(self,locator):
        '''判断元素是否存在'''
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def isElementsExist(self,locator):
        '''判断元素组是否存在'''
        eles = self.find_element(locator)
        n = len(eles)
        if n ==0:
            return False
        elif n ==1:
            return True
        else:
            print("找到一组元素%s"%n)
            return True

    def radioSelected(self,locator):
        '''radio定位选择'''
        self.find_element(locator)
        r = self.isSelected()
        return r

    def isElementExist01(self,locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def isElementExist02(self,locator):
        eles = self.find_element(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素个数为：%s"%n)
            return True



if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://120.77.156.30:8080/zentao/user-login.html")
    zentao = Base(driver)
    #表达方式1
    #locator1 = (By.ID,"account")
    #locator2 = (By.CSS_SELECTOR,"[name='password']")
    #locator3 = (By.XPATH,".//*[@id='submit']")

    #表达方式2
    locator1 = ("id","account")
    locator2 = ("css selector","[name='password']")
    locator3 = ("xpath",".//*[@id='submit']")


    zentao.find_element(locator1).send_keys("admin")
    zentao.find_element(locator2).send_keys("123456.")
    zentao.find_element(locator3).click()