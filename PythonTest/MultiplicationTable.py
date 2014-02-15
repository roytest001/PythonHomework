#coding=utf-8

def MultiplicationTable():
	for i in range(1, 10):  
   		print " ".join(["%d*%d=%d" % (j, i, i*j) for j in range(1, i+1)])  

MultiplicationTable()
