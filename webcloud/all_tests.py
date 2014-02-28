#coding=utf-8
import unittest 
import HTMLTestRunner
import os ,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#读取测试用例文件
listaa='E:\\selenium_test_case\\webcloud'
def creatsuitel():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,
                      pattern ='*_sta.py', #读取符合规则的用例
                      top_level_dir=None)

    for test_suite in discover:
        for  test_case in test_suite:
            testunit.addTests(test_case)
            #print testunit
    return testunit

alltestnames = creatsuitel()

#生成测试报告
now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
filename = 'E:\\selenium_test_case\\report\\'+now+'result.html'
fp = file(filename,'wb') 

#读取浏览器类型
br =open("E:\\selenium_test_case\\data\\browser.txt", "r")
browser = br.read()
print br

runner =HTMLTestRunner.HTMLTestRunner(
     stream=fp,
     title=u'快播私有云测试报告',
     description=u'运行浏览器：'+ browser)

runner.run(alltestnames)
