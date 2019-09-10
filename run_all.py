#coding:utf-8
import unittest

from common import HTMLTestRunner

#用例的路径
casePath = "E:\web_auto\\case"
#匹配规则
rule = "test*.py"
#查找用例所在（发现）
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

#stream报告存放路径加后缀
reportPath = "E:\web_auto\\report\\"+"report.html"
fp = open(reportPath,"wb") #读取文件
send = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                    title=u"测试报告",
                                    description="登录验证报告")
#执行找到的用例
send.run(discover)
fp.close()  #关闭打开的文件，省得占内存




