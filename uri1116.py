# -*- coding: utf-8 -*-
a=int(input())
for i in range(a):
	a,b=map(int,input().split())
	if b == 0:
		print('divisao impossivel')
	else:
		print('{:.1f}'.format(a/b))