# -*- coding: utf-8 -*-
while True:
	a,b=map(int,raw_input().split(' '))
	if a == 0 or b == 0:
		break
	if a > 0 and b > 0:
		print('primeiro')
	elif a > 0 and b < 0:
		print('quarto')
	elif a < 0 and b > 0:
		print('segundo')
	elif a < 0 and b < 0:
		print('terceiro')