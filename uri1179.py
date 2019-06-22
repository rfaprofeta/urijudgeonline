# -*- coding: utf-8 -*-
def impress(tipo,lista):
	for num, item in enumerate(lista):
		print('{}[{}] = {}'.format(tipo,num,item))

contador = 0
par = [];impar = []
while contador < 15:
	entrada = int(input())
	if entrada%2 == 0:
		par.append(entrada)
	else:
		impar.append(entrada)
	if len(par) == 5:
		impress('par',par)
		par = []
	elif len(impar) == 5:
		impress('impar',impar)
		impar = []
	contador+=1

impress('impar',impar)
impress('par', par)