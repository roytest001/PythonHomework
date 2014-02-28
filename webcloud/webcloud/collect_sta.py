#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re ,sys
sys.path.append("\public")
from public import *

sys.path.append("\package")
from  package import location

class Collect(unittest.TestCase):
    
    def setUp(self):
        self.driver = login.browser(self)
        self.we = location
        self.driver.implicitly_wait(30)
        self.base_url = login.url(self)
        self.verificationErrors = []
        self.accept_next_alert = True

    #收藏功能用例    
    def test_collect(self):
        u"""收藏用户分享文件"""
        driver = self.driver
        we = self.we
        driver.get(self.base_url) 
        login.login(self) #登陆
        
        inputs=we.findsTagName(driver,'input')
        n=0
        for i in inputs:
            if i.get_attribute('type')=="checkbox":
                n=n+1
        #print u"当前列表文件为 %d" %n
        
        #收藏操作
        we.findClassName(driver,"collect").click()
        time.sleep(3)

        inputs=we.findsTagName(driver,'input')
        ns=0
        for ii in inputs:
            if ii.get_attribute('type')=="checkbox":
                ns=ns+1
        #print u"当前列表文件为 %d" %ns

        if ns==n+1:
            print "ok!"
        else:
            raise NameError('add file error!')
            
        login.logout(self)#退出

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
