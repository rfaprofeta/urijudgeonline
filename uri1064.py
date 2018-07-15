# -*- coding: utf-8 -*-
z=0;soma=0
for i in range(6):
	a=float(input())
	if a > 0:
		z+=1
		soma+=a
print('{0} valores positivos'.format(z))
print('{:.1f}'.format(soma/z))