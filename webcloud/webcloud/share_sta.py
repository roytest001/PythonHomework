#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, sys
sys.path.append("\public")
from public import *
sys.path.append("\package")
from  package import location

class Share(unittest.TestCase):
    
    def setUp(self):
        self.driver = login.browser(self)
        self.we = location
        self.driver.implicitly_wait(30)
        self.base_url = login.url(self)
        self.verificationErrors = []
        self.accept_next_alert = True

    #用户分享操作用例    
    def test_share(self):
        u"""用户分享"""
        driver = self.driver
        we = self.we
        driver.get(self.base_url)

        #登陆
        login.login(self)

        #分享操作
        we.findClassName(driver,"public-btn").click()
        time.sleep(3)
        we.findClassName(driver,"share-btn-style").click()
        time.sleep(3)
        we.findClassName(driver,"close-btn").click()
        time.sleep(2)

                        
        #退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    
    suite.addTest(Share("test_share"))
    
    results = unittest.TextTestRunner().run(suite)



                   

