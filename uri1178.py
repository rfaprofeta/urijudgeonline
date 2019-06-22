# -*- coding: utf-8 -*-
entrada = float(input())
contador = 0
while contador < 100:
	print('N[{}] = {:.4f}'.format(contador,entrada))
	entrada/=2
	contador+=1