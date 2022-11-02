# -*- coding : latin -*-
# Python 3.7

a = int(input('Informe um número inteiro: '))
b = int(input('Informe mais um número inteiro: '))
c = int(input('Informe o ultimo número inteiro: '))


if b > a < c:
    print('O menor número é:', a)
elif a > b < c:
    print('O menor número é:', b)
elif a > c < b:
    print('O menor número é:', c)
    