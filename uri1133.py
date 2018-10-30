#-*- coding: utf-8 -*-
a=int(input())
b=int(input())
if a>b:
	for i in range (b,a):
		if i%5 == 3 or i%5 == 2:
			print(i)
else:
	for i in range (a,b):
		if i%5 == 3 or i%5 == 2:
			print(i)
