# -*- coding: utf-8 -*-
a=int(input());num=0
for i in range(a):
	ls=[]
	b,c=map(int,input().split(' '))
	if b % 2 == 0:
		d = b // c
	else:
		d = (b // c )-1
	print(d)
	for i in range(b):
		ls.append(i+1)
	while True:
		try:
			print('São {0} itens'.format(len(ls)))
			for i in range(d):
				num+=c-1
				ls.pop(num)
				b=len(ls)
		except:
			break

'''
		for item in (ls, c):
			ls.pop(num)
			num+=c
'''
print(ls)

