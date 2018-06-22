# -*- coding: utf-8 -*-
a=[];c=0.0
b=[2,3,4,1]
a=input().split(' ')
for i in range(4):
	d=float(a[i])*float(b[i])
	c=c+d
c=c/10
if c >= 7.0:
	print('Media: {:.1f}'.format(c))
	print('Aluno aprovado.')
elif c >= 5.0 and c < 7.0:
	e=float(input())
	f=(c+e)/2
	print('Media: {:.1f}'.format(c))
	print('Aluno em exame.')
	print('Nota do exame: {:.1f}'.format(e))
	if f >= 5.0:
		print('Aluno aprovado.')
	if f <= 5.0:
		print('Aluno reprovado.')
	print('Media final: {:.1f}'.format(f))
else:
	print('Media: {:.1f}'.format(c))
	print('Aluno reprovado.')