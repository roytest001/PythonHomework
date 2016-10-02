#coding=utf-8

import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='/root/Downloads/datamodels.xml')
print tree
a = tree.getroot()
print a

for child_of_root in a:
    print child_of_root.tag

