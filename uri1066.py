par=0;impar=0;positivo=0;negativo=0
for i in range(5):
    a=int(input())
    if a%2 == 0:
        par+=1
    else:
        impar+=1
    if a>0:
        positivo+=1
    elif a<0:
        negativo+=1
print('{0} valor(es) par(es)'.format(par))
print('{0} valor(es) impar(es)'.format(impar))
print('{0} valor(es) positivo(s)'.format(positivo))
print('{0} valor(es) negativo(s)'.format(negativo))