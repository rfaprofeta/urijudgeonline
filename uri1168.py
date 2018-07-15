# -*- coding: utf-8 -*-
dictionary={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
a=int(input())
for i in range(a):
	d=0
	b=input()
	for ii in b:
		c=dictionary[int(ii)]
		d+=int(c)
	print('{0} leds'.format(d))