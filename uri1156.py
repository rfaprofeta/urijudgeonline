# -*- coding: utf-8 -*-
s=1;a=3;b=2
while True:
	z=a/b
	s=s+z
	if a == 39:
		break
	a+=2
	b*=2
print('{:.2f}'.format(s))