# -*- coding : latin -*-
# Python 3.7

n = int(input('Informe um número inteiro para verificar se é um número primo ou digite "1" para ver todos até 100: '))

if n == 1:
    while n < 100:
        n += 1
        if n == 2 or n == 3 or n == 5:
            print(int(n), 'é primo')
        elif (n % 2 != 0) & (n % 3 != 0) & (n % 5 != 0):
            print(int(n), 'é primo')
        else:
            print(int(n), 'não é primo')


elif n == 2 or n == 3 or n == 5:
    print('O número é primo !')
elif (n % 2 != 0) & (n % 3 != 0) & (n % 5 != 0):
    print('O número é primo !')
else:
    print('O número não é primo')
