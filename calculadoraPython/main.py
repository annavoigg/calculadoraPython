# importando tkinter
from distutils.command.clean import clean
from tkinter import *
from tkinter import ttk
from turtle import right
from unittest import result

# cores

cor1 = "#3B3B3B" # black
cor2 = "#FEFFFF" # white
cor3 = "#38576B" # dark blue 
cor4 = "#ECEFF1" # gray
cor5 = "#FFAB40" # orange


janela = Tk()

# titulo da janela
janela.title("Calculadora")
# definindo largura x comprimento da janela
janela.geometry("235x310")
# cor do fundo da jenala, não inclui o frame do display ainda
janela.config(bg=cor1)

# dividindo janela com tkinter (criando frames)

# frame display
frameTela = Frame(janela, width=235, height=50, bg=cor3)
frameTela.grid(row=0, column=0)

# frame corpo (botões)
frameCorpo = Frame(janela, width=235, height=268)
frameCorpo.grid(row=1, column=0)

# variável que armazena todos os valores 

recebeValores = ''

# criando label do display

valorTexto = StringVar()

# criando função

def entradaValores(event):

    global recebeValores

    recebeValores = recebeValores + str(event)

    # resultado = eval(float(armazenaValores))
    
    # passando valor para o display
    valorTexto.set(recebeValores)

# função para calcular 

def calcular():
    global recebeValores
    resultado = eval(recebeValores)
    
    valorTexto.set(str(resultado))


# função para limpar a tela 

def limpaTela():

    global recebeValores
    recebeValores = ""
    valorTexto.set('')


# display 

appLabel = Label(frameTela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg= cor3, fg= cor2)
appLabel.place(x= 0, y= 0)

# criando botões 

button1 = Button(frameCorpo, command=limpaTela, text="C", width=11, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button1.place(x= 0, y=0) # clear

button2 = Button(frameCorpo, command= lambda: entradaValores('%'), text="%", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button2.place(x= 118, y=0) # resto divisão

button3 = Button(frameCorpo, command= lambda: entradaValores('/'), text="/", width=5, height=2, bg= cor5, fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
button3.place(x= 177, y=0) 

# segunda linha - botões 

button4 = Button(frameCorpo, command= lambda: entradaValores('7'), text="7", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # n7
button4.place(x= 0, y=52)

button5 = Button(frameCorpo, command= lambda: entradaValores('8'), text="8", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button5.place(x= 59, y=52) # n8

button6 = Button(frameCorpo, command= lambda: entradaValores('9'), text="9", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
button6.place(x= 118, y=52) # n9 

button7 = Button(frameCorpo, command= lambda: entradaValores('*'), text="*", width=5, height=2, bg= cor5, fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
button7.place(x= 177, y=52) # multiplicação 

# terceira linha - botões 

button8 = Button(frameCorpo, command= lambda: entradaValores('4'), text="4", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) 
button8.place(x= 0, y=104) # n4

button9 = Button(frameCorpo, command= lambda: entradaValores('5'), text="5", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button9.place(x= 59, y=104) # n5

button10 = Button(frameCorpo, command= lambda: entradaValores('6'), text="6", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button10.place(x= 118, y=104) # n6

button7 = Button(frameCorpo, command= lambda: entradaValores('-'), text="-", width=5, height=2, bg= cor5, fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button7.place(x= 177, y=104) # subtração

# quarta linha - botões 

button11 = Button(frameCorpo, command= lambda: entradaValores('1'), text="1", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # 
button11.place(x= 0, y=156) # n1

button12 = Button(frameCorpo, command= lambda: entradaValores('2'), text="2", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # 
button12.place(x= 59, y=156) # n2

button13 = Button(frameCorpo, command= lambda: entradaValores('3'), text="3", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # 
button13.place(x= 118, y=156) # n3

button14 = Button(frameCorpo, command= lambda: entradaValores('+'), text="+", width=5, height=2, bg= cor5, fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # divisão 
button14.place(x= 177, y=156) # soma

# quinta linha - botões 

button15 = Button(frameCorpo, command= lambda: entradaValores('0'), text="0", width=11, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # clean
button15.place(x= 0, y=208) # n0

button16 = Button(frameCorpo, command= lambda: entradaValores('.'), text=".", width=5, height=2, bg= cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # 
button16.place(x= 118, y=208) # ponto

button17 = Button(frameCorpo, command= calcular, text="=", width=5, height=2, bg= cor5, fg= cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # divisão 
button17.place(x= 177, y=208) # resultado

# entradaValores()

# permite a execução da janela
janela.mainloop()


