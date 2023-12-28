from tkinter import*
import tkinter
from datetime import datetime


#variaveis de cores
preto="#000000"
cinza="#D3D3D3"
azul="#00BFFF"

janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=False, height=False)#resizable nao permite a alteracao do tamanha janela
janela.config(bg=preto)


#funcao Relogio
def relogio():
    tempo=datetime.now()
    hora=tempo.strftime("%H:%M:%S")
    dia_semana=tempo.strftime("%A")
    dia = tempo.day
    mes=tempo.strftime("%b")
    ano=tempo.strftime("%Y")
    l1.config(text=hora)
    l1.after(200,relogio)
    l2.config(text=dia_semana + "  " + str(dia) + "/" + str(mes) + "/" + str(ano))


#mostra na tela 
l1=Label(janela, text="" , font=("Arial 80"), bg=preto, fg=azul)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2=Label(janela, text="" , font=("Arial 20"), bg=preto, fg=azul)
l2.grid(row=1, column=0, sticky=NW, padx=5)


relogio()
janela.mainloop()
