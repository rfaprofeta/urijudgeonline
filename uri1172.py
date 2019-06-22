# -*- coding: utf-8 -*-
contador = 0
while contador < 10:
	a = int(input())
	if a <= 0:
		print("X[{0}] = 1".format(contador))
	else:
		print("X[{0}] = {1}".format(contador,a))
	contador+=1