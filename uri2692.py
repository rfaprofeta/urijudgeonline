# -*- coding: utf-8 -*-
a,b = map(int, input().split(' '))
dic = {}
for i in range(a):
	y = input().split(' ')
	dic[y[0]] = y[1];dic[y[1]] = y[0]
for ii in range(b):
	k = input()
	klista=[]
	for char in k:
		klista.append(char)
		value = dic.get(char)
		if value != None:
			klista.pop(-1)
			klista.append(value)
	klista = ''.join(klista)
	print(klista)