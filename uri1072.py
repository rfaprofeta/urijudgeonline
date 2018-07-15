# -*- coding: utf-8 -*-
a=int(input())
dentro=0;fora=0
for i in range(a):
	z=int(input())
	if z <= 20 and z >=10:
		dentro+=1
	else:
		fora+=1
print('{0} in'.format(dentro))
print('{0} out'.format(fora))