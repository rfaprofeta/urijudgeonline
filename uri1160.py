# -*- coding: utf-8 -*-
a=int(input())
for i in range(a):
	lista=[];valuea=0;valueb=0;cont=0
	lista=input().split(' ')
	while True:
		lista[0]=int(lista[0])+(int(lista[0])*float(lista[2])/100)
		lista[1]=int(lista[1])+(int(lista[1])*float(lista[3])/100)
		cont+=1
		if cont > 100:
			print('Mais de 1 seculo.')
			break
		if int(lista[0]) > int(lista[1]):
			print('{0} anos.'.format(cont))
			break