# -*- coding : latin -*-
# Python 3.7

a = int(input('informe o primeiro lado do triangulo:'))
b = int(input('informe o segundo lado do triangulo:'))
c = int(input('informe o terceiro lado do triangulo:'))


p: float = (a + b + c) / 2
fh = p*(p-a) * (p-b) * (p-c)

area = fh ** (1/2)
if ((b-c) < a < (b+c)) & ((a-c) < b < (a+c)) & ((a-b) < c < (a+b)):
    print('a area do triangulo é ', area)
else:
    print('não se trata de um triangulo')
