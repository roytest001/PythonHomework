#coding=utf-8
import time
#缩略图模式切换为列表模式
def list_mode(self):
    driver = self.driver
    driver.find_element_by_class_name("list-mode-btn").click()
    time.sleep(2)

#新功能引导
def guide(self):
    driver = self.driver
    we = self.we
    we.findClassName(driver,"guide-ok-btn").click()
    time.sleep(3)
