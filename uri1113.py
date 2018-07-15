# -*- coding: utf-8 -*-
while True:
	a,b=map(int,input().split(' '))
	if a < b:
		print('Crescente')
	elif a > b:
		print('Decrescente')
	elif a == b:
		break
