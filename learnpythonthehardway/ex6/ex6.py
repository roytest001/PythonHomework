#coding=utf-8

# 给变量x赋值字符串
x = "There are %d types of people." % 10
#给变量 binary 赋值
binary = "binary"
#给变量do_not 赋值
do_not = "don't"
#给变量y赋值字符串
y = "Those who know %s and those who %s." % (binary, do_not)
#打印变量x
print x
#打印变量y
print y
#打印字符串
print "I said: %r." % x
#打印字符串
print "I also said: '%s'." % y
#给变量hilarious 赋值
hilarious = False
#给变量joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"
#打印字符串
print joke_evaluation % hilarious
#给变量w赋值
w = "This is the left side of..."
#给变量e赋值
e = "a string with a right side."
#打印字符串
print w + e