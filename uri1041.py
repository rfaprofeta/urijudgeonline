# -*- coding: utf-8 -*-
x,y=map(float,input().split(' '))
if x == y == 0.0:
	print('Origem')
if x > 0.0 and y > 0.0:
	print('Q1')
if x < 0.0 and y > 0.0:
	print('Q2')
if x < 0.0 and y < 0.0:
	print('Q3')
if x > 0.0 and y < 0.0:
	print('Q4')
if x > 0.0 and y == 0.0 or x < 0.0 and y == 0.0:
	print('Eixo X')
if x == 0.0 and y > 0.0 or x == 0.0 and y < 0.0:
	print('Eixo Y')

