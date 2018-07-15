# -*- coding: utf-8 -*-
I=0;J=1;II=0
while True:
	for i in range(3):
		if I == 0 or I == 1 or I == 2:
			print('I={0} J={1}'.format(int(I),int(J+I+i)))
		else:
			print('I={:.1f} J={:.1f}'.format(I,J+I+i))
	I+=0.2
	I=round(I,2)
	if I>2:
		break