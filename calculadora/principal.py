from tkinter import *
from tkinter import ttk
#cores 
cor1 = '#ffffff' #branco
cor2 = "#000033" #azul diferenciado 
cor3 = "#000000" #preto
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela = Tk()
janela.title("calculadora")
janela.geometry("240x263+300+140")
janela.config(bg=cor1)
janela.resizable(False,FALSE)


frame_cabeca = Frame(janela,width=240,height=45,bg= cor2)
frame_cabeca.grid(row=0,column=0)


frame_corpo = Frame(janela,width=240,height=218)
frame_corpo.grid(row=1,column=0)

#variavel todos valores
todos_valores = ""
resultado = StringVar()
# mostrar o numero digitado/ calcular
def mostrar_valor(evento):
    global todos_valores

    todos_valores = todos_valores + str(evento)
    
    resultado.set(todos_valores)

def calcular():
    global todos_valores
    resultado.set(eval(todos_valores))

#limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    resultado.set("")


#janela das contas 

contas = Label(frame_cabeca, textvariable=resultado, width=29,height=3, padx=3, relief=FLAT, anchor="e", justify=RIGHT, font='Ivy 10 bold',bg=cor2,fg=cor1)
contas.place(x=0,y=0)


#botões

b1 = Button(frame_corpo, text="C", width=16, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE,command=limpar_tela) 
b1.place(x=0, y=0)

b2 = Button(frame_corpo, text="%", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("%"))
b2.place(x=123,y=0)

b3 = Button(frame_corpo, text="/", width=7, height=2, bg=cor5, fg= cor1, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("/"))
b3.place(x=185,y=0 )

b4 = Button(frame_corpo, text="7", width=7,height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("7"))
b4.place(x=0,y=44)

b5 = Button(frame_corpo, text="8", width=7,height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("8"))
b5.place(x=60,y=44)

b6 = Button(frame_corpo,text="9", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("9"))
b6.place(x=123,y=44)

b7 = Button(frame_corpo,text="*", width=7, height=2, bg=cor5, fg= cor1, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("*"))
b7.place(x=185,y=44)

b8 = Button(frame_corpo,text="4", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("4"))
b8.place(x=0,y=88)

b9 = Button(frame_corpo,text="5", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("5"))
b9.place(x=60,y=88)

b10 = Button(frame_corpo,text="6", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("6"))
b10.place(x=123,y=88)

b11 = Button(frame_corpo,text="-", width=7, height=2, bg=cor5, fg= cor1, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("-"))
b11.place(x=185,y=88)
#
b12 = Button(frame_corpo,text="1", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("1"))
b12.place(x=0,y=132)

b13 = Button(frame_corpo,text="2", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("2"))
b13.place(x=60,y=132)

b14 = Button(frame_corpo,text="3", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("3"))
b14.place(x=123,y=132)

b15 = Button(frame_corpo,text="+", width=7, height=2, bg=cor5, fg= cor1, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("+"))
b15.place(x=185,y=132)

b16 = Button(frame_corpo,text="0", width=16, height=2, bg=cor4,  font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor("0"))
b16.place(x=0,y=176)

b17 = Button(frame_corpo,text=",", width=7, height=2, bg= cor4, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: mostrar_valor(","))
b17.place(x=123,y=176)

b18 = Button(frame_corpo,text="=", width=7, height=2, bg=cor5, fg= cor1, font=('Ivy 8 bold'), relief='raised',overrelief=RIDGE, command= lambda: calcular())
b18.place(x=185,y=176)




janela.mainloop()
