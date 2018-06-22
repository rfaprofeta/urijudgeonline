# -*- coding: utf-8 -*-
a=[]
a=input().split(' ')
if int(a[3]) == 1 and int(a[4]) == 0:
	print('Jogador 1 ganha!')
if int(a[3]) == 0 and int(a[4]) == 1:
	print('Jogador 1 ganha!')
if int(a[3]) == 1 and int(a[4]) == 1:
	print('Jogador 2 ganha!')
if int(a[3]) == 0 and int(a[4]) == 0:
	if int(a[0]) == 1:
		if (int(a[1])+int(a[2]))%2 == 0:
			print('Jogador 1 ganha!')
		else:
			print('Jogador 2 ganha!')
	if int(a[0]) == 0:
		if (int(a[1])+int(a[2]))%2 == 0:
			print('Jogador 2 ganha!')
		else:
			print('Jogador 1 ganha!')