#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

def login(self, username, password):
	self.dr.get(self.login_url)
	time.sleep(3)
	self.dr.find_element_by_name('log').clear()
	time.sleep(3)
	self.dr.find_element_by_name('log').send_keys(username)
	time.sleep(3)
	self.dr.find_element_by_name('pwd').send_keys(password)
	self.dr.find_element_by_name('wp-submit').click()
    self.dr.maximize_window()

def quit(self):
	self.dr.quit()
