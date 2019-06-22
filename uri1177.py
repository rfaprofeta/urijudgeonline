# -*- coding: utf-8 -*-
value = int(input())
check = 0;contador = 0
while contador < 1000:
	print('N[{}] = {}'.format(contador,check))
	check+=1
	contador+=1
	if check == value:
		check = 0
	