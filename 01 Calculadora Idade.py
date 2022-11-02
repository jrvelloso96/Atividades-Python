# -*- coding : latin -*-
# Python 3.7

idade = int(input('informe a idade em dias: '))

anos = idade / 360
meses = (anos % 360 - (int(anos))) * 12
dias = (meses - (int(meses))) * 30

print(int(anos), 'anos', int(meses), 'meses e', int(dias), 'dias')
