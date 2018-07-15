# -*- coding: utf-8 -*-
maior=0;pos=0;num=0
for i in range(100):
	a=int(input())
	num+=1
	if maior < a:
		maior = a
		pos = num
print(maior)
print(pos)