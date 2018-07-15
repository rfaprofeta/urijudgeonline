# -*- coding: utf-8 -*-
a=input()
for i in range(a):
	d=0
	b=raw_input()
	for z in b:
		ii = int(z)
		if ii == 0 or ii == 6 or ii == 9:
			d+=6
		elif ii == 2 or ii == 3 or ii == 5:
			d+=5
		elif ii == 1:
			d+=2
		elif ii == 4:
			d+=4
		elif ii == 7:
			d+=3
		elif ii == 8:
			d+=7
	print('{0} leds'.format(d))