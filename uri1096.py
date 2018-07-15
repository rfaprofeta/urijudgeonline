# -*- coding: utf-8 -*-
I=1
while True:
	J=8
	for i in range(3):
		J-=1
		print('I={0} J={1}'.format(I,J))
	I+=2
	if I > 9 and J == 5:
		break