# -*- coding: utf-8 -*-
contador = 0
while contador < 100:
	value = float(input())
	if value <= 10:
		print("A[{0}] = {1}".format(contador,value))
	contador+=1

	