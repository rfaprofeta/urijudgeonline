# -*- coding: utf-8 -*-
a,b,c=map(float,input().split(' '))
if ((b-c)<a<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
	print('Perimetro = {:.1f}'.format(a+b+c))
else:
	print('Area = {:.1f}'.format(((a+b)*c)/2))