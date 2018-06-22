# -*- coding: utf-8 -*-
dictionary={1:4.00,2:4.50,3:5.00,4:2.00,5:1.50}
a,b=map(int, input().split(' '))
c=dictionary[a]
print('Total: R$ {:.2f}'.format(c*b))