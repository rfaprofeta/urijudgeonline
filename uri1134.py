# -*- coding: utf-8 -*-
a=[];b=[];c=[]
while True:
	z=int(input())
	if z == 1:
		a.append(z)
	elif z == 2:
		b.append(z)
	elif z == 3:
		c.append(z)
	elif z == 4:
		break
print('MUITO OBRIGADO')
print('Alcool: {0}'.format(len(a)))
print('Gasolina: {0}'.format(len(b)))
print('Diesel: {0}'.format(len(c)))