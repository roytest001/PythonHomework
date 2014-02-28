#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re 

#把public目录添加到path下，这里用的相对路径
import sys 
sys.path.append("\public")
#导入登录、退出模块
from public import login,mode

#导入元素定位封装
sys.path.append("\package")
from  package import location


class Login(unittest.TestCase):
    
    def setUp(self):
        self.driver = login.browser(self)
        self.we = location
        self.driver.implicitly_wait(30)
        self.base_url = login.url(self)
        self.verificationErrors = []
        self.accept_next_alert = True

    #用户登录用例    
    def test_login(self):
        u"""用户登录"""
        driver = self.driver
        we = self.we
        driver.get(self.base_url)
        #login.login(self)  #登录
        
        try:
            login.login(self)  #登录
            
        except:
            browser.get_screenshot_as_file("E:\\selenium_test_case\\error\\loginError.png")
            raise NameError('login error!')
        
        
        login.logout(self)  #退出
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":

    unittest.main()
          

