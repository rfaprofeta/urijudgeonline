# -*- coding: utf-8 -*-
lista = []
a = int(input())
b = a
lista.append(a // 100)
a = a - lista[0] * 100
lista.append(a // 50)
a = a - lista[1] * 50
lista.append(a // 20)
a = a - lista[2] * 20
lista.append(a // 10)
a = a - lista[3] * 10
lista.append(a // 5)
a = a - lista[4] * 5
lista.append(a // 2)
a = a - lista[5] * 2
lista.append(a)
print('{0}'.format(b))
print('{0} nota(s) de R$ 100,00'.format(lista[0]))
print('{0} nota(s) de R$ 50,00'.format(lista[1]))
print('{0} nota(s) de R$ 20,00'.format(lista[2]))
print('{0} nota(s) de R$ 10,00'.format(lista[3]))
print('{0} nota(s) de R$ 5,00'.format(lista[4]))
print('{0} nota(s) de R$ 2,00'.format(lista[5]))
print('{0} nota(s) de R$ 1,00'.format(lista[6]))
