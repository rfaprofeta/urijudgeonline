# -*- coding: utf-8 -*-
while True:
	a=int(input());z=[]
	if a == 0:
		break
	for i in range(1,a+1):
		z.append(i)
	n = ' '.join([str(x) for x in z])
	print(n)