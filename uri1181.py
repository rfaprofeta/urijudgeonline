# -*- coding: utf-8 -*-
value = int(input())
tipo = input()
soma = 0.0
for linha in range(12):
	for coluna in range(12):
		valor = float(input())
		if linha == value:
			soma+=valor
if tipo == 'S':
	print('{:.1f}'.format(soma))
else:
	print('{:.1f}'.format(soma/12))