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

class Rename(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://passport.kuaibo.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_rename(self):
        u"""文件/文件重命名回车确认"""
        driver = self.driver
        driver.get(self.base_url + "/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

        #浏览器全屏 
        driver.maximize_window()
        #登陆
        login.login(self)
        #新功能引导
        mode.guide(self)
        #列表模式
        mode.list_mode(self)

        #选择文件重命名
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[4]/table/tbody[5]/tr/td/input").click()
        time.sleep(3)
        
        element=driver.find_element_by_class_name("more-fe")
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(2)

        lis=driver.find_elements_by_tag_name('li')
        for li in lis:
            if li.get_attribute('data-action') == 'rename':
                li.click()
        time.sleep(2)

        inputs=driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute('type') == 'text':
                input.send_keys(u"ipkasdf文件")
                input.send_keys(Keys.ENTER)#回车确认重命名
                time.sleep(2)
        
        #退出
        login.quit_(self)
        
    def test_rename2(self):
        u"""文件/文件重命名确认按钮确认"""
        driver = self.driver
        driver.get(self.base_url + "/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

        #浏览器全屏 
        driver.maximize_window()
        #登陆
        login.login(self)
        #新功能引导
        mode.guide(self)
        #列表模式
        mode.list_mode(self)

        #选择文件重命名
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[4]/table/tbody[6]/tr/td/input").click()
        time.sleep(3)
        
        element=driver.find_element_by_class_name("more-fe")
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(2)

        lis=driver.find_elements_by_tag_name('li')
        for li in lis:
            if li.get_attribute('data-action') == 'rename':
                li.click()
        time.sleep(2)

        inputs=driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute('type') == 'text':
                input.send_keys(u"aaacde文件cc")
                driver.find_element_by_link_text(u"确认").click() #确认按钮
                #input.send_keys(Keys.ENTER)#回车确认重命名
                time.sleep(2)
        
        #退出
        login.quit_(self)

    def test_rename3(self):
        u"""Esc取消文件/文件重命名"""
        driver = self.driver
        driver.get(self.base_url + "/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

        #浏览器全屏 
        driver.maximize_window()
        #登陆
        login.login(self)
        #新功能引导
        mode.guide(self)
        #列表模式
        mode.list_mode(self)

        #选择文件重命名
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[4]/table/tbody[5]/tr/td/input").click()
        time.sleep(3)
        
        element=driver.find_element_by_class_name("more-fe")
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(2)

        lis=driver.find_elements_by_tag_name('li')
        for li in lis:
            if li.get_attribute('data-action') == 'rename':
                li.click()
        time.sleep(2)

        inputs=driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute('type') == 'text':
                input.send_keys(u"qetadglkj文件")
                input.send_keys(Keys.ESCAPE)#Esc取消文件/文件重命名
                time.sleep(2)
        
        #退出
        login.quit_(self)
        

        
    def test_rename4(self):
        u"""取消按钮文件/文件重命名"""
        driver = self.driver
        driver.get(self.base_url + "/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

        #浏览器全屏 
        driver.maximize_window()
        #登陆
        login.login(self)
        #新功能引导
        mode.guide(self)
        #列表模式
        mode.list_mode(self)

        #选择文件重命名
        driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[4]/table/tbody[6]/tr/td/input").click()
        time.sleep(3)
        
        element=driver.find_element_by_class_name("more-fe")
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(2)

        lis=driver.find_elements_by_tag_name('li')
        for li in lis:
            if li.get_attribute('data-action') == 'rename':
                li.click()
        time.sleep(2)

        inputs=driver.find_elements_by_tag_name('input')
        for input in inputs:
            if input.get_attribute('type') == 'text':
                input.send_keys(u"文件asddcc")
                driver.find_element_by_link_text(u"取消").click() #取消按钮
                time.sleep(2)
        
        #退出
        login.quit_(self)

        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #unittest.main()
    
    suite = unittest.TestSuite()
        
    suite.addTest(Rename("test_share"))
    
    results = unittest.TextTestRunner().run(suite)
    


                   

