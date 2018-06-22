# -*- coding: utf-8 -*-

while True:
	a=[];b=[];match=0;result=0
	al=[];bl=[]
	a,b = input().split(' ')
	if a == '0' and b == '0':
		break
	counta = 9 - int(len(a))
	countb = 9 - int(len(b))
	al = [0] * counta
	bl = [0] * countb
	al.append(a);al=''.join(map(str,al))
	bl.append(b);bl=''.join(map(str,bl))
	for i in range(9):
			x=(i+1)*-1
			if int(al[x])+int(bl[x])+match >= 10:
				match=1;result+=1
			else:
				match=0
	if result == 0:
		print('No carry operation.')
	elif result == 1:
		print('{0} carry operation.'.format(result))
	else:
		print('{0} carry operations.'.format(result))