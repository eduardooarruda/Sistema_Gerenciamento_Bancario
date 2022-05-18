from cProfile import label
from sys import implementation
from Endereco import Endereco
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from tkinter import *
from tkinter import Tk, ttk

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters



# end = Endereco('Ceara', 'Fortim', 'N Senhora', 'São Joao', '38')

# c = ContaCorrente('Eduardo', '999.999.999-99', end, 'edu37659', True)

# print(c.getEndereco.getEstado)

# print(c.getCpf)

# print(c.getSenha)

#print(c.atualizarSaldo())

menu_inicial = Tk()
menu_inicial.title('Sistema de Gerênciamento Bancário')
menu_inicial.geometry('450x500')
menu_inicial.configure(background=co1)
menu_inicial.resizable(width=False, height=False)

#Titulo da parte de cima da janela
frame_titulo = Frame(menu_inicial, width=450, height=50, bg=co1, relief='flat')
frame_titulo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(menu_inicial, width=450, height=450, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


#configurando o frame que contém o título

label_titulo = Label(frame_titulo, text='Informações Pessoais',anchor=CENTER, font=('Ivy 20'), bg=co1, fg=co4)

label_titulo.place(x=5, y=5)
#label_titulo.pack()

menu_inicial.mainloop()