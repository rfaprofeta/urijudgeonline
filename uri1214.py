# -*- coding: utf-8 -*-
a=int(input())
for i in range (a):
	media=0;upmedia=0;n=0
	c=input().split(' ')
	for i in range(1,len(c)):
		media+=int(c[i])
		n+=1
	media=int(media/n)

	for ii in range(1,len(c)):
		if int(c[ii]) > media:
			upmedia+=1
	print('{:.3f}%'.format(upmedia/n*100))
