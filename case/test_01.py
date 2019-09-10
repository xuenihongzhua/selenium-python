#coding:utf-8
import unittest

class IntegerTestCase(unittest.TestCase):   #执行框架
    #每个用例运行之前都要先执行一次
    def setUp(self):
        print("打开浏览器")
    def test_add(self):
        '''用例说明：测试用例add'''
        self.assertEqual((1+2),3)
        print("失败！")
        self.assertEqual((0+1),1)

    def test_sub(self):
        '''用例说明：测试用例sub'''
        self.assertEqual((0*20),0)
        self.assertEqual((3*5),15)
     #每个用例运行之前都要先执行一次
    def tearDown(self):
        print("关闭浏览器")

if __name__ =="__main__":   #执行脚本
    unittest.main()