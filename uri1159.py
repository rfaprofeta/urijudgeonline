# -*- coding: utf-8 -*-
while True:
	value=0
	a=int(input())
	if a == 0:
		break
	if a % 2 == 0:
		for i in range (5):
			value=value+a
			a+=2
		print(value)
	else:
		a+=1
		for i in range (5):
			value=value+a
			a+=2
		print(value)