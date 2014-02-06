import unittest
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

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
        self.login(self.usrname, self.pswd)
        print self.dr.current_url
        self.assertTrue('wp-admin' in self.dr.current_url)

    def test_2_create_post(self):
        print 'test create_post'
        self.login(self.usrname, self.pswd)
        title = self.creat_post()
        print "title:" + title
        self.dr.get(self.post_list_url)
        post_list_table = self.dr.find_element_by_class_name('wp-list-table')
        self.assertTrue(title in post_list_table.text)

    def test_3_modify_articles(self):     
        print 'modify articles.'
        self.login(self.usrname, self.pswd)
        time.sleep(2)
        self.dr.find_element_by_xpath("/html/body/div//div[2]/ul/li[3]/a/div[3]").click()
        move = self.dr.find_element_by_xpath("/html/body/div/div[3]/div[2]/div/div[3]/form/table/tbody/tr/td/strong/a")
        ActionChains(self.dr).move_to_element(move).perform()
        self.dr.find_element_by_xpath("/html/body/div/div[3]/div[2]/div/div[3]/form/table/tbody/tr/td/div[2]/span/a").click()
        time.sleep(2)
        title_or_content = 'modify post' + str(time.time())
        self.dr.find_element_by_name('post_title').clear()
        self.dr.find_element_by_name('post_title').send_keys(title_or_content)
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
        print js
        self.dr.execute_script(js)
        self.dr.find_element_by_id('publish').click()
        return title_or_content
        self.dr.get(self.post_list_url)
        post_list_table = self.dr.find_element_by_class_name('wp-list-table')
        self.assertTrue(title_or_content in post_list_table.text)

    def test_4_search_articles(self):
        print 'search articles'
        pass

 
    def test_5_del_all_articles(self):
        print 'test del_all_articles'
        self.login(self.usrname, self.pswd)   
        time.sleep(2)
        self.dr.find_element_by_xpath("/html/body/div//div[2]/ul/li[3]/a/div[3]").click()
        time.sleep(2)      
        self.dr.find_element_by_id('cb-select-all-1').click()
        Select(self.dr.find_element_by_name('action')).select_by_value('trash')
        time.sleep(5)
        js_="var q=document.documentElement.scrollTop=0"
        self.dr.execute_script(js_)
        self.dr.find_element_by_id('doaction').click()
        time.sleep(5)


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

    def creat_post(self):
        create_post_url = 'http://localhost/wordpress/wp-admin/post-new.php'
        self.dr.get(create_post_url)
        title_or_content = 'new post' + str(time.time())
        self.dr.find_element_by_name('post_title').send_keys(title_or_content)
        js = "document.getElementById('content_ifr').contentWindow.document.body.innerHTML='" + title_or_content + "'"
        print js
        self.dr.execute_script(js)
        self.dr.find_element_by_name('publish').click()
        return title_or_content
    
    def tearDown(self):
        sleep(3)
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()