# -*- coding: utf-8 -*-
a=float(input())
if a <= 400.00:
	c=15
	b = a*c/100
if a >= 400.01 and a<= 800.00:
	c=12
	b = a*c/100
if a >= 800.01 and a<= 1200.00:
	c=10
	b = a*c/100
if a >= 1200.01 and a<= 2000.00:
	c=7
	b = a*c/100
if a > 2000.00:
	c=4
	b = a*c/100
print('Novo salário: {:.2f}'.format(a+b))
print('Reajuste ganho: {:.2f}'.format(b))
print('Em percentual: {0} %'.format(c))