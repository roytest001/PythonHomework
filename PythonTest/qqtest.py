#coding=utf-8

'''
随机测试
打开连接
http://sports.qq.com/seriea/
打印国米板块右侧所有的新闻标题和内容
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

dr = webdriver.Firefox()
dr.get('http://sports.qq.com/seriea')
inter = WebDriverWait(dr, 10).until(lambda driver: dr.find_element_by_id('inter'))
hot_list = inter.find_element_by_class_name('hot_list')
links = hot_list.find_elements_by_tag_name('a')

sub = webdriver.Firefox()

for link in links:
    print link.get_attribute('href')
    print link.text
    print '#'*64
    sub.get(link.get_attribute('href'))

    try:
        mainpage = sub.find_element_by_id('Cnt-Main-Article-QQ')
        print mainpage
        contents = mainpage.find_elements_by_tag_name('p')
        for content in contents:
            print content.text
    except Exception, e:
        contents = sub.find_elements_by_tag_name('p')
        for content in contents:
            print content.text
    print '#'*64
    print '\n'

sub.quit()
dr.quit()