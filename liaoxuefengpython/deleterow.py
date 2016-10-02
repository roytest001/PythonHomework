#coding=utf-8

f = open('/root/Downloads/preconfiguration_global.xml','r')

fr = f.readlines()
fr.pop()
print fr
print len(fr)
f.close()
fs = open('/root/Downloads/preconfiguration_global.xml','wb+')
fs.writelines(fr)
fs.close()
