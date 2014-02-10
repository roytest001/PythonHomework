#coding=utf-8
import sys 
sys.path.append("\Test_Case")
from Test_Case import *
import WordPress

def caselist():
    alltestnames = [WordPress.WordPressTestCase]
    print "success  read case list!!"
    return alltestnames

caselist()