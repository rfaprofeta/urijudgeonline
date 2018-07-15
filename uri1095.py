# -*- coding: utf-8 -*-
I=1;J=60
while True:
	print('I={0} J={1}'.format(I,J))
	I+=3;J-=5
	if J < 0:
		break