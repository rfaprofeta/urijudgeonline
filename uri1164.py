# -*- coding: utf-8 -*-
a=int(input())
for i in range(a):
	b=int(input())
	z=[];sum=0
	for ii in range(1, b-1):
		if b % ii == 0:
			z.append(ii)
	for iii in z:
		sum+=iii
	if b == sum:
		print('{0} eh perfeito'.format(b))
	else:
		print('{0} nao eh perfeito'.format(b))