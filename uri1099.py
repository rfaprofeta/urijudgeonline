#-*- coding: utf-8 -*-
z=0
a=int(input())
for i in range(a):
	a,b=map(int,input().split(" "))
	if a>b:
		for ii in range(b+1,a):
			if ii%2 != 0:
				z+=ii
		print(z)
		z=0
	else:
		for ii in range(a+1,b):
			if ii%2 != 0:
				z+=ii
		print(z)
		z=0