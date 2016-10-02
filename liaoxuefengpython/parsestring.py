#coding=utf-8

import re

f = open('/root/Downloads/datamodel.xml','r')

fr = f.readlines()

newfr=[]

for i in fr:
    print i
    print len(i)
    substr = i[:-2]
    print substr
    print len(substr)
    newfr.append(substr)

print len(fr)
print newfr
print len(newfr)
print "######### start match node with re ##########"

passwordnodes=[]
for i in newfr:
    m = re.match(r'.*ssword>$', i)
    if m:
        print i
        passwordnodes.append(i)

print passwordnodes

print len(passwordnodes)

