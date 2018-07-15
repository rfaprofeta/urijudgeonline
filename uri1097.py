# -*- coding: utf-8 -*-
I=1;J=7
while True:
	for i in range(3):
		print('I={0} J={1}'.format(I,J-i))
	I+=2
	J+=2
	if I > 9 and J > 13:
		break