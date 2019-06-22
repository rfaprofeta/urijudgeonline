# -*- coding: utf-8 -*-
while True:
	value = int(input())
	if value == 0:
		break
	numero = 0
	for linha in range(value):
		for coluna in range(value):
			if value%2 == 0:
				ref = 'par'
			else:
				ref = 'impar'
			epct = value//2
			if linha == coluna:
				numero+=1
			print('\t',end="")
			print(numero,end="")
		print('\n')
#	print('\n')
