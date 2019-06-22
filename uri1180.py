# -*- coding: utf-8 -*-
value = int(input())
lista = input().split(' ')
count = lista[0]
position = 0
for item in range(value):
	if int(lista[item]) < int(count):
		count = lista[item]
		position = item
print('Menor valor: {}\nPosicao: {}'.format(count,position))