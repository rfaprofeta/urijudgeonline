# -*- coding: utf-8 -*-
while True:
	z=[];value=0
	a,b=map(int,raw_input().split(' '))
	if a <= 0 or b <=0:
		break
	if a > b:
		for i in range (b,a+1):
			z.append(str(i))
			value+=i
		ref=' '.join(z)
		print('{0} Sum={1}'.format(ref,value))
	else:
		for i in range (a,b+1):
			z.append(str(i))
			value+=i
		ref=' '.join(z)
		print('{0} Sum={1}'.format(ref,value))