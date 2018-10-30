# -*- coding: utf-8 -*-
a = float(raw_input())
if a < 0 or a > 100.00:
	print ('Fora de intervalo')
elif a >= 0 and a <= 25.00:
	print ('Intervalo [0,25]')
elif a > 25.00 and a <= 50.00:
	print ('Intervalo (25,50]')
elif a > 50.00 and a <= 75.00:
	print ('Intervalo (50,75]')
elif a > 75.00 and a <= 100.00:
	print ('Intervalo (75,100]')