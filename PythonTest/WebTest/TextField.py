#coding=utf-8
__author__ = 'roy'

from selenium import webdriver
import os
import time


class TextField(object):

    def __init__(self, dr, ele):
        self.dr = dr
        self.ele = ele

    def set(self, comments):
        self.ele.send_keys(comments)
        
    def clear(self):
        self.ele.clear()

    def click(self):
        self.ele.click()

    def foucs(self):
         self.dr.execute_script("arguments[0].focus()", self.ele)

    def high_light(self):
         self.dr.execute_script("arguments[0].style.border = '2px solid red'", self.ele)

    def quit(self):
        self.dr.quit()

file_path = 'file:///' + os.path.abspath('PythonTest.html')

dr = webdriver.Firefox()
dr.get(file_path)
ele = dr.find_element_by_id('tf')

tf = TextField(dr,ele)
time.sleep(3)
tf.set("Hellowrd!!!")
time.sleep(3)
tf.clear()
time.sleep(3)
tf.click()
time.sleep(3)
tf.foucs()
time.sleep(3)
tf.high_light()
time.sleep(3)
tf.quit()