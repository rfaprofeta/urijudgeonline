# -*- coding: utf-8 -*-
b=[]
a=int(input())
for i in range(a):
	b=input().split(' ')
	if str(b[0]) == 'Thor':
		print('Y')
	else:
		print('N')