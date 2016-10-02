#coding=utf-8

import xml.dom.minidom

dom = xml.dom.minidom.parse('/root/Downloads/datamodel.xml')
#dom = xml.dom.minidom.parse('/root/datamodel.xml')

root = dom.documentElement
print 'node name is: %s' %root.nodeName
print 'node vlaue is %s' %root.nodeValue
print 'node Type is %s' %root.nodeType
print 'node Elenment is %s' %root.ELEMENT_NODE

'''

nodename = []


for node in root.childNodes:
    print node
    print node.nodeName

    """
        for i in node.childNodes:
        print i.nodeName
    """
    nodename.append(node.nodeName)

print len(nodename)


'''

'''
for i in nodes:
    if i.hasAttribute('dburi'):
        print i.nodeName
        print "Type Value: %s" % i.getAttribute('v')
        print i.parentNode.nodeName
'''

print "**********check the childnodes*************"

'''
for i in nodename:
    a = root.getElementsByTagName(i)
    print a
#    print "list the node %s childnode as follows:" % a.nodeName
    for b in a:
        print b.nodeName
'''


def  digui(node):
    print node
    node_list = []
    node_name = node.nodeName
    print "Current Node Name is : %s" %node_name

    if node.childNodes:
        for child_node in node.childNodes:
            print child_node
            print "Current Child Node Name is : %s" %child_node.nodeName
            if child_node.nodeType == node.ELEMENT_NODE:
                print "Before connection string, the node_name is : %s" %node_name
                a = node_name
                node_name += child_node.nodeName
                print "After connect string, the node_name is : %s" %node_name
                node_list.append(node_name)
                node_name = a
                print "Node_Name rechanged to the init value is : %s" %node_name
                digui(child_node)
                print "*****************"
                print "*****************"

            else:
                print "This node is not ELEMENT_NODE, can not apppend in to node list!!!"
    else:
        print "This node have no child node!!!"
    return node_list




'''

def  digui(node):
    node_list = []
    node_name = node.nodeName

    if node.childNodes:
        for child_node in node.childNodes:
            if child_node.nodeType == node.ELEMENT_NODE:
                node_name += child_node.nodeName
                print node_name
                digui(child_node)
            else:
                node_list.append(node_name)
                #print node_list
    return node_list


'''

print digui(root)




