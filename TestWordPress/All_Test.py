#coding=utf-8

import unittest
import WordPress
import HTMLTestRunner
import time
import AllCase_List

now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
alltestnames = AllCase_List.caselist()
testunit = unittest.TestSuite()
for test in alltestnames:
    testunit.addTest(unittest.makeSuite(test))


filename = 'C:\\TestReports\\'+now+'_result.html'

fp = file(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = 'WordPress Test Report',
    description = 'Test Case Result:')

runner.run(testunit)


