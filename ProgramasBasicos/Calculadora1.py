from tkinter import *
from tkinter import ttk

janela= Tk()
janela.title("Calculadora")
janela.geometry("270x380")

#cores usado no app
cinza="#f2f2f2"
cinzaClaro="#DCDCDC"
laranja="orange"
preto="black"
azul="#87cefa"
azulclaro="#36afca"

#Display e teclado
display=Frame(janela, width=270, height=50,bg=preto )
display.grid(row=0, column=0)
teclas=Frame(janela, width=270, height=330,bg=cinza)
teclas.grid(row=1, column=0)
 



#Criando a funcao
todos_valores=""
valor=StringVar()

def entrada_valores(event):
    global todos_valores
    todos_valores=todos_valores+str(event)
    valor.set(todos_valores)

#Criando a funcao calcular
def calcular():
    global todos_valores
    resultado=str(eval(todos_valores))
    valor.set(resultado)
    todos_valores=""

# Funcao limpar operacao
def limpar():
    global todos_valores
    todos_valores=""
    valor.set("")

#criando label
valor=StringVar()#vareial que recebe o valor do button
app_label=Label(display,textvariable=valor,width=23, height=2,font=("Ivy",15),padx=7, relief=FLAT,anchor="e", justify=RIGHT, bg=azulclaro,fg=cinza)
app_label.place(x=0, y=0)
 
#botao linha 1
bclear=Button(teclas,text="Clear",width=12, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:limpar())
bclear.place(x=10, y=4)
bporcentagem=Button(teclas,text="%",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("%"))
bporcentagem.place(x=160, y=4)
bdividir=Button(teclas,text="/",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("/"))
bdividir.place(x=210, y=4)

#botao linha 2
b7=Button(teclas,text="7",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("7"))
b7.place(x=10, y=50)
b8=Button(teclas,text="8",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("8"))
b8.place(x=60, y=50)
b9=Button(teclas,text="9",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("9"))
b9.place(x=110, y=50)
bmult=Button(teclas,text="*",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("*"))
bmult.place(x=160, y=50)
var=Button(teclas,text="",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores(""))
var.place(x=210, y=50)

#botao linha 3
b4=Button(teclas,text="4",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("4"))
b4.place(x=10, y=95)
b5=Button(teclas,text="5",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("5"))
b5.place(x=60, y=95)
b6=Button(teclas,text="6",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("6"))
b6.place(x=110, y=95)
bmenos=Button(teclas,text="-",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("-"))
bmenos.place(x=160, y=95)
var=Button(teclas,text="",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores(""))
var.place(x=210, y=95)

#botao linha 4
b1=Button(teclas,text="1",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("1"))
b1.place(x=10, y=140)
b2=Button(teclas,text="2",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("2"))
b2.place(x=60, y=140)
b3=Button(teclas,text="3",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("3"))
b3.place(x=110, y=140)
bmais=Button(teclas,text="+",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("+"))
bmais.place(x=160, y=140)
var=Button(teclas,text="",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores(""))
var.place(x=210, y=140)


#botao linha 5
var=Button(teclas,text="",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores(""))
var.place(x=10, y=185)
b0=Button(teclas,text="0",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("0"))
b0.place(x=60, y=185)
var=Button(teclas,text="",width=5, height=2, bg=cinzaClaro, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores(""))
var.place(x=110, y=185)
bponto=Button(teclas,text=".",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores("."))
bponto.place(x=160, y=185)
var=Button(teclas,text="",width=5, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:entrada_valores(""))
var.place(x=210, y=185)

#botao linha 5
bigual=Button(teclas,text="=",width=12, height=2, bg=laranja, relief=RAISED, overrelief=RIDGE, command=lambda:calcular( ))
bigual.place(x=160, y=230)



janela.mainloop()