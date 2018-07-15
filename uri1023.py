# -*- coding: utf-8 -*-
def ordena(z):
	lista=[];z.sort()
	value = int(z[0])
	cont = 0
	for ref in z:
		if ref == value:
			cont+=1
		else:
			lista.append(str(cont)+'-'+str(value))
			value = ref
			cont=1
	lista.append(str(cont)+'-'+str(value))
	txt = ' '.join(lista)
	return(txt)
city=0
while True:
	a=int(input())
	md1=0;md2=0
	if a == 0:
		break
	if city>0:
		print('\n')
	city+=1;z=[]
	for test in range(a):
		mrd,cons=map(int,input().split(' '))
		for i in range(mrd):
			z.append(int(cons/mrd))
		md1+=cons;md2+=mrd;
	media=md1/md2
	texto = ordena(z)
	print('Cidade# {0}:'.format(city))
	print(texto)
	print('Consumo medio: {:.2f} m3'.format(media))