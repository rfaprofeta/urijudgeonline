# -*- coding: utf-8 -*-
while True:
	try:
		lista=[]
		a=int(input())
		for i in range(a):
			b=input()
			lista.append(b)
		lista.sort()
		for ii in lista:
				print(ii+'\n')
	except EOFError:
		break

