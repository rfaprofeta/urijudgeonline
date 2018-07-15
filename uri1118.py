# -*- coding: utf-8 -*-
nota1=0;nota2=0
while True:
	a=float(input())
	if a < 0 or a > 10:
		print('nota invalida')
	else:
		if nota1 == 0:
			nota1=a
		else:
			nota2=a
			print('media = {:.2f}'.format((nota1+nota2)/2))
			while True:
				print('novo calculo (1-sim 2-nao)')
				b=int(input())
				if b == 1 or b == 2:
					nota1=0
					break
			if b == 2:
				break