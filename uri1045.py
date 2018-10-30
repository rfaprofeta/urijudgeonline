# -*- coding: utf-8 -*-
a=input().split(' ')
vet = [float(i) for i in a]
vet.sort()
if vet[2]>=(vet[1]+vet[0]):
	print ("NAO FORMA TRIANGULO")
elif vet[2]**2==(vet[1]**2+vet[0]**2):
	print ("TRIANGULO RETANGULO")
	if (vet[0]==vet[1]) and (vet[1]==vet[2]) and (vet[2]==vet[0]):
		print ("TRIANGULO EQUILATERO")
	elif (vet[0]==vet[1]) or (vet[1]==vet[2]) or (vet[2]==vet[0]):
		print ("TRIANGULO ISOSCELES")
elif vet[2]**2>(vet[1]**2+vet[0]**2):
	print ("TRIANGULO OBTUSANGULO")
	if (vet[0]==vet[1]) and (vet[1]==vet[2]) and (vet[2]==vet[0]):
		print ("TRIANGULO EQUILATERO")
	elif (vet[0]==vet[1]) or (vet[1]==vet[2]) or (vet[2]==vet[0]):
		print ("TRIANGULO ISOSCELES")
elif vet[2]**2<(vet[1]**2+vet[0]**2):
	print ("TRIANGULO ACUTANGULO")
	if (vet[0]==vet[1]) and (vet[1]==vet[2]) and (vet[2]==vet[0]):
		print ("TRIANGULO EQUILATERO")
	elif (vet[0]==vet[1]) or (vet[1]==vet[2]) or (vet[2]==vet[0]):
		print ("TRIANGULO ISOSCELES")

'''
    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
'''