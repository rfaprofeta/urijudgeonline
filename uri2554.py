# -*- coding: utf-8 -*-
while True:
	try:
		amigos,datas = map(int, input().split(' '))
		for i in range(datas):
			eventos = input().split(' ')
			soma = 0;num = 0
			for ii in range(1,amigos + 1):
				soma += int(eventos[ii])
				num += 1
				if soma == amigos:
					print(eventos[0])
			if num == amigos:
				print('Pizza antes de FdI')
	except EOFError:
		break