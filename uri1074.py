# -*- coding: utf-8 -*-
a=int(input())
for ii in range(a):
	i=int(input())
	if i == 0:
		print('NULL')
	if i%2 == 0:
		if i>0:
			print('EVEN POSITIVE')
		elif i<0:
			print('EVEN NEGATIVE')
	else:
		if i>0:
			print('ODD POSITIVE')
		elif i<0:
			print('ODD NEGATIVE')