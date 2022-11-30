#Python 3.7
from tkinter import *
import sqlite3

con = sqlite3.connect('IMC.db')

cur = con.cursor()
cur.execute("CREATE TABLE IMC (nome text, endereco text, peso integer, altura integer, IMC float)")


app = Tk()
app.title("Calculadora IMC")
app.geometry("700x300")

def sair():
    app.destroy()

def calcular():
    alt= int(valt.get())
    peso= int(vpeso.get())

    resultado = peso / alt**2 * 10000

    imc_resultado['text'] = "{:.{}f}".format(resultado,2)

Label(app,text="Nome do Paciente").place(x=10,y=10)
Label(app,text="Endereço do Paciente").place(x=10,y=60)

nome=Entry(app)
nome.place(x=150,y=10,width=400,height=25)
end=Entry(app)
end.place(x=150,y=60,width=400,height=25)

Label(app,text="Altura(cm)").place(x=10,y=110)
valt=Entry(app)
valt.place(x=150,y=110,width=100,height=25)


Label(app,text="Peso(kg)").place(x=10,y=160)
vpeso=Entry(app)
vpeso.place(x=150,y=160,width=100,height=25)

imc_resultado=Label(app,text='0',bg='#ddd',font=200)
imc_resultado.place(x=350,y=100,width=200,height=150)
Label(app,text="O seu IMC é:",bg='#ddd',font=150).place(x=405,y=105)

Button(app,text="Calcular",command=calcular).place(x=30,y=220,width=75)
Button(app,text="Sair",command=sair).place(x=110,y=220,width=75)

con = sqlite3.connect('IMC.db')

cur = con.cursor()
cur.execute("CREATE TABLE IMC (nome text, endereco text, peso integer, altura integer, IMC float)")



app.mainloop()
