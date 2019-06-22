# -*- coding: utf-8 -*-
tipo = input()
soma = 0.0
counter = 0
for linha in range(12):
	for coluna in range(12):
		valor = float(input())
		if coluna > linha and coluna + linha > 11:
			soma+=valor
			counter+=1
if tipo == 'S':
	print('{:.1f}'.format(soma))
else:
	print('{:.1f}'.format(soma/counter))