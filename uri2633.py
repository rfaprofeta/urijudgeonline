# -*- coding: utf-8 -*-

while True:
	try:
		ls=[];sl=[]
		a=input()
		for i in range(a):
			ls,sl=(map(input().split(' ')))

	except EOFError:
		break