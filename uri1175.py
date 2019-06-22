# -*- coding: utf-8 -*-
lista = [];contador = 0
while contador < 20:
	value = int(input())
	lista.append(value)
	contador+=1
for enum, numero in enumerate(lista):
	print("N[{0}] = {1}".format(enum,lista[len(lista)-enum-1]))
	