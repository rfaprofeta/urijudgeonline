# -*- coding: utf-8 -*-
a=int(input())
for i in range(a):
	b,c=map(int,input().split(' '))
	z=[];num=0
	if b % 2 == 0:
		b=b+1
		z.append(b)
		for ii in range (c-1):
			b+=2
			z.append(b)
		for n in z:
			num+=n
	else:
		z.append(b)
		for ii in range (c-1):
			b+=2
			z.append(b)
		for n in z:
			num+=n
	print(num)