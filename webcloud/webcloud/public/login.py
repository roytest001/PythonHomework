#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import csv  #导入csv包

#读取浏览器类型
browser = open("E:\\selenium_test_case\\data\\browser.txt", "r")
br = browser.read()

def browser(self):
    driver =webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                              desired_capabilities={'platform': 'ANY',
                                                    'browserName':br,
                                                    'version': '',
                                                    'javascriptEnabled': True,
                                                    })
    return driver

#读取data目录cvs文件
my_file='E:\\selenium_test_case\\data\\userinfo.csv'
login_data=csv.reader(file(my_file,'rb'))


#登录模块
for user in login_data:

    def url(self):
        url = user[2]
        return url
    
    def login(self):
        driver = self.driver
        we = self.we
        driver.maximize_window() #浏览器全屏
        we.findId(driver,"user_name").clear()
        we.findId(driver,"user_name").send_keys(user[0])
        we.findId(driver,"user_pwd").clear()
        we.findId(driver,"user_pwd").send_keys(user[1])
        we.findId(driver,"dl_an_submit").click()
        time.sleep(3)
        we.findClassName(driver,"guide-ok-btn").click() #新功能引导
        time.sleep(2)



#退出模块
def logout(self):
    driver = self.driver
    we = self.we
    we.findClassName(driver,"Usertool").click()
    time.sleep(2)
    we.findLinkText(driver,"退出").click()
    time.sleep(2)

    
