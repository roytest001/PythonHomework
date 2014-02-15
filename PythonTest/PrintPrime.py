# coding=utf-8

def PrintPrime():
	for i in range(2,101):
		prime = 0
		for j in range(2,i/2):
			if (i % j == 0):
				prime = 1
		if (prime == 0):
			print i

PrintPrime()