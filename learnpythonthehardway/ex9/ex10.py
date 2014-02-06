#coding=utf-8
# Here is some new strange  stuff, remember type is exactly.

days = "Mon Tue Wed Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

###怎样将月份显示在新的一行?
###为什么使用 %r 时 \n 新行就不灵了? %r就是这个样子,它打印出的是你写出来的方式(或者近似方式)。它是用来 debug的原始格 式。
###为什么在三引号之间加入空格就会出错?
###你必须写成 """ 而不是 " " ",引号之间不能有空格。
###为什么你打印时用了 \+ 而不是逗号?
###因为我的目的是将两个字符串连接起来,组建成一个新的字符串。后面你会学到,"print" 里的逗号其实是分隔参数的一种方式
