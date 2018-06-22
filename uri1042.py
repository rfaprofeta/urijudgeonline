# -*- coding: utf-8 -*-
a=[]
a=input().split(' ')
b=[int(z) for z in a];b.sort()
for x in range(3):
	print(b[x])
print(' ')
for y in range(3):
	print(a[y])