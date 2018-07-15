# -*- coding: utf-8 -*-
a=int(input())
for i in range(1,a+1):
	if i%2 == 0:
		print('{0}^2 = {1}'.format(i,i**2))