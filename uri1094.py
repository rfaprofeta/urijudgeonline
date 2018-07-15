# -*- coding: utf-8 -*-
C=0;R=0;S=0
a=input()
for i in range(a):
	b=raw_input().split(' ')
	if b[1] == 'C':
		C+=int(b[0])
	elif b[1] == 'R':
		R+=int(b[0])
	elif b[1] == 'S':
		S+=int(b[0])
print('Total: {0} cobaias'.format(C+R+S))
print('Total de coelhos: {0}'.format(C))
print('Total de ratos: {0}'.format(R))
print('Total de sapos: {0}'.format(S))
print('Percentual de coelhos: {:.2f} %'.format(C/(C+R+S)*100))
print('Percentual de ratos: {:.2f} %'.format(R/(C+R+S)*100))
print('Percentual de sapos: {:.2f} %'.format(S/(C+R+S)*100))