# -*-coding: utf-8 -*-

import sqlite3

con = sqlite3.connect('IMC1.db')

cur = con.cursor()


# cur.execute("CREATE TABLE IMC1 (nome text, peso integer, altura integer, IMC integer)")


def calcula():
    nome = str(input("informe seu nome "))
    peso = int(input("informe seu peso: "))
    alt = int(input("informe sua altura: "))

    imc = peso / alt ** 2 * 10000
    print(nome, "o seu IMC é: %.2f" % imc)
    cur.execute("INSERT INTO IMC1 VALUES ('" + nome + "'," + str(peso) + " ," + str(alt) + "," + str(imc) + ")")
    con.commit()


sair = 'a'
while sair != 's':
    calcula()
    sair = str(input('digite s para sair o pressione qualquer tecla para continuar: '))
