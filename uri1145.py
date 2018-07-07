# -*- coding: utf-8 -*-
a,b=map(int,input().split(' '))
z=[]
for i in range(1,b+1):
	z.append(i)
	if i % a == 0:
		numeros = ' '.join([str(x) for x in z])
		print(numeros)
		z=[]
if b % a != 0:
	numeros = ' '.join([str(x) for x in z])
	print(numeros)