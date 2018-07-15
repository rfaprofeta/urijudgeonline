# -*- coding: utf-8 -*-
def mdc(a,b):
	if a<0:
		a = -a
	if b<0:
		b = -b
	result = a%b
	if result == 0:
		return b
	else:
		return mdc(b,result)

a=int(input())
for i in range(a):
	z=[]
	z=input().split(' ')
	if z[3] == '+':
		den=(int(z[0])*int(z[6])) + (int(z[4])*int(z[2]))
		num=(int(z[2])*int(z[6]))
		value = mdc(den,num)
	elif z[3] == '-':
		den=(int(z[0])*int(z[6])) - (int(z[4])*int(z[2]))
		num=(int(z[2])*int(z[6]))
		value = mdc(den,num)
	elif z[3] == '*':
		den=(int(z[0])*int(z[4]))
		num=(int(z[2])*int(z[6]))
		value = mdc(den,num)
	elif z[3] == '/':
		den=(int(z[0])*int(z[6]))
		num=(int(z[4])*int(z[2]))
		value = mdc(den,num)
	print('{0}/{1} = {2}/{3}'.format(den,num,int(den/value),int(num/value)))