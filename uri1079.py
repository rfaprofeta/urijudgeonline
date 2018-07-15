# -*- coding: utf-8 -*-
a=int(input())
for i in range(a):
	b=raw_input().split(' ')
	c=(float(b[0])*2+float(b[1])*3+float(b[2])*5)/10
	print('{:.1f}'.format(c))
