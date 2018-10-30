#-*- coding: utf-8 -*-
inter = 0;gremio = 0;
grenal = 0;empate = 0
while True:
	a,b = map(int,input().split(" "))
	if a == b:
		empate+=1
	elif a > b:
		inter+=1
	else:
		gremio+=1
	grenal+=1
	print('Novo grenal (1-sim 2-nao)')
	b = int(input())
	if b == 2:
		break
if grenal == 1:
	print("{0} grenal".format(grenal))
else:
	print("{0} grenais".format(grenal))
print("Inter:{0}".format(inter))
print("Gremio:{0}".format(gremio))
print("Empates:{0}".format(empate))
if inter > gremio:
	print("Inter venceu mais")
else:
	print("Gremio venceu mais")