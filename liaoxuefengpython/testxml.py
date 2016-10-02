#coding=utf-8
import xml.dom.minidom

dom = xml.dom.minidom.parse('/root/aaa.xml')

root = dom.documentElement

print 'node name is: %s' %root.nodeName
print 'node vlaue is %s' %root.nodeValue
print 'node Type is %s' %root.nodeType
print 'node Elenment is %s' %root.ELEMENT_NODE


bb = root.getElementsByTagName('maxid')
b= bb[0]
print b.nodeName
print b.nodeValue

bb = root.getElementsByTagName('login')
b= bb[0]
print b.nodeName
print b.nodeValue



bb = root.getElementsByTagName('caption')
b= bb[1]
print b.nodeName

bb = root.getElementsByTagName('item')
b= bb[1]
print b.nodeName




itemlist = root.getElementsByTagName('login')
item = itemlist[0]
un=item.getAttribute("username")
print un
pd=item.getAttribute("passwd")
print pd

ii = root.getElementsByTagName('item')
i1 = ii[0]
i=i1.getAttribute("id")
print i

i2 = ii[1]
i=i2.getAttribute("id")
print i

cc=dom.getElementsByTagName('caption')
c1=cc[0]
print c1.firstChild.data

c2=cc[1]
print c2.firstChild.data

c3=cc[2]
print c3.firstChild.data

