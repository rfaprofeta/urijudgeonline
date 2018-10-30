# -*- coding: utf-8 -*-
a=int(input())
b=int(input())
c=0
if a>b:
	for i in range (b,a+1):
		if i%13 != 0:
			c+=i
else:
	for i in range (a,b+1):
		if i%13 != 0:
			c+=i
print (c)