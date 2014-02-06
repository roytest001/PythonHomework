import unittest
import HTMLTestRunner
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import login
class WordPressTestCase(unittest.TestCase):
    dr = None
    login_url = 'http://localhost/wordpress/wp-login.php'
    post_list_url = 'http://localhost/wordpress/wp-admin/edit.php'
    usrname = 'root'
    pswd = '123456roy'

    def setUp(self):
        self.dr = webdriver.Firefox()

    def test_1_login(self):
        print 'test login'
        login.login(self, self.usrname, self.pswd)
        print self.dr.current_url
        self.assertTrue('wp-admin' in self.dr.current_url)

    def tearDown(self):
        sleep(3)
        login.quit(self)

if __name__ == '__main__':
    unittest.main()