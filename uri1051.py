# -*- coding: utf-8 -*-
a=float(input())
if a <= 2000.00:
	print('Isento')
if a > 2000.00 and a<= 3000.00:
	print('R$ {:.2f}'.format((a-2000.00)*8/100))
if a > 3000.00 and a<= 4500.00:
	print('R$ {:.2f}'.format(((a-3000.00)*18/100)+(1000.00*8/100)))
if a > 4500.00:
	print('R$ {:.2f}'.format(((a-4500.00)*28/100)+(1000.00*8/100)+(1500.00*18/100)))