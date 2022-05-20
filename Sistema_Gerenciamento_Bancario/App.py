from tkinter import messagebox
from Endereco import Endereco
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from tkinter import *

class App:
# co0 = "#f0f3f5"  # Preta / black 
    def __init__(self):
        self.__cor_branco= "#feffff"  # branca / white
# co2 = "#3fb5a3"  # verde / green
# co3 = "#38576b"  # valor / value
# co4 = "#403d3d"   # letra / letters
        self.__cor_indigo = "#4B0082"
        self.__conta = None
        self.__tela_inicial = None
        self.__tipo_conta = None
        self.__tela_inf_pessoais = None
        self.__tela_endereco = None



    def menu_inicial(self):
        self.__tela_inicial = Tk()
        self.__tela_inicial.title('Sistema de Gerênciamento Bancário')
        self.__tela_inicial.geometry('250x250+610+153')
        self.__tela_inicial.configure(background=self.__cor_indigo)
        self.__tela_inicial.resizable(width=False, height=False)


        label_titulo = Label(self.__tela_inicial, text='Escolhar uma opção', font=('Ivy 15'), bg=self.__cor_indigo, fg=self.__cor_branco)

        # label_1 = Label(self.__tela_inicial, text='Escolhar uma opção', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        # label_2 = Label(self.__tela_inicial, text='Escolhar uma opção', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        btn_CriarConta = Button(self.__tela_inicial, text='Criar uma Conta', font=('Ivy 11'), command=self.__escolher_tipo_conta)

        btn_AcessarConta = Button(self.__tela_inicial, text='Acessar Conta', font=('Ivy 11'))


        label_titulo.grid(row=0)
        # label_1.grid(row=1,column=0)

        btn_CriarConta.grid(row=1)
        # label_2.grid(row=3)
        btn_AcessarConta.grid(row=2)

        self.__tela_inicial.mainloop()
    
    def __escolher_tipo_conta(self):
        self.__tela_tipo_conta = Tk()
        self.__tela_tipo_conta.title('Sistema de Gerênciamento Bancário')
        self.__tela_tipo_conta.geometry('250x250+610+153')
        self.__tela_tipo_conta.configure(background=self.__cor_indigo)
        self.__tela_tipo_conta.resizable(width=False, height=False)
        
        # global tipo_conta
        tipo_conta = StringVar()

        label_titulo = Label(self.__tela_tipo_conta, text='Escolhar o Tipo de Conta', font=('Ivy 15'), bg=self.__cor_indigo, fg=self.__cor_branco)

        btn_corrente = Button(self.__tela_tipo_conta, text='Corrente', font=('Ivy 11'), command=lambda: self.__criar_conta('P'))

        btn_poupanca = Button(self.__tela_tipo_conta, text='Poupança', font=('Ivy 11'), command=lambda: self.__criar_conta('C'))

        label_titulo.grid(row=0)
        btn_corrente.grid(row=3)
        btn_poupanca.grid(row=4)
        
        self.__tela_inicial.destroy()

        
    def __criar_conta(self, tipo):
        if tipo == 'P':
            self.__conta = ContaPoupanca()
        if tipo == 'C':
            self.__conta = ContaCorrente()

        # print(self.__conta)
        self.__tela_tipo_conta.destroy()
        self.__adicionar_informacoes_pessoais()

    def __adicionar_informacoes_pessoais(self):
        self.__tela_inf_pessoais = Tk()
        self.__tela_inf_pessoais.title("Cadastrar nova Conta")
        self.__tela_inf_pessoais.geometry("250x250+610+153")
        self.__tela_inf_pessoais.configure(background=self.__cor_indigo)
        self.__tela_inf_pessoais.resizable(width=False, height=False)

        label_nome = Label(self.__tela_inf_pessoais, text='Nome completo:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        label_cpf = Label(self.__tela_inf_pessoais, text='CPF:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)


        label_obs_cpf = Label(self.__tela_inf_pessoais, text='OBS: O formato do cpf deve ser 000.000.000-00', font=('Ivy 8'), bg=self.__cor_indigo, fg=self.__cor_branco )

        input_nome = Entry(self.__tela_inf_pessoais)

        input_cpf = Entry(self.__tela_inf_pessoais)

        btn_proximo = Button(self.__tela_inf_pessoais, text='Próximo', font=('Ivy 11'), command=lambda: self.__validar_informacoes_pessoais(input_nome.get(), input_cpf.get()))

        label_nome.grid(row=1, sticky=W)
        input_nome.grid(row=2, sticky=W)
        label_cpf.grid(row=3, sticky=W)
        label_obs_cpf.grid(row=4, sticky=W)
        input_cpf.grid(row=5, sticky=W)
        btn_proximo.grid(row=6)

       
    def __validar_informacoes_pessoais(self,nome, cpf): 
        sentenca_nome = self.__conta.setNome(nome)
        sentenca_cpf = self.__conta.setCpf(cpf)

        if sentenca_cpf == False:
            messagebox.showinfo("Atenção","CPF inválido!")
            self.__tela_inf_pessoais.destroy()
            self.__adicionar_informacoes_pessoais()
        else:
            # self.__tela_inf_pessoais.destroy()
            self.__adicionar_endereco()
    
    def __adicionar_endereco(self):
        self.__tela_endereco = Tk()
        self.__tela_endereco.title("Endereço")
        self.__tela_endereco.geometry("250x270+610+153")
        self.__tela_endereco.configure(background=self.__cor_indigo)
        self.__tela_endereco.resizable(width=False, height=False)

        label_estado = Label(self.__tela_endereco, text='Estado:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        label_cidade = Label(self.__tela_endereco, text='Cidade:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        label_bairro = Label(self.__tela_endereco, text='Bairro:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        label_rua = Label(self.__tela_endereco, text='Rua:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)

        label_numero = Label(self.__tela_endereco, text='Numero:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)


        input_estado = Entry(self.__tela_endereco)

        input_cidade = Entry(self.__tela_endereco)

        input_bairro = Entry(self.__tela_endereco)

        input_rua = Entry(self.__tela_endereco)

        input_numero = Entry(self.__tela_endereco)

        btn_proximo = Button(self.__tela_endereco, text='Próximo', font=('Ivy 11'), command=lambda: self.__validar_endereco(input_estado.get(), input_cidade.get(), input_bairro.get(), input_rua.get(), input_numero.get()))

        label_estado.grid(row=1, sticky=W)
        input_estado.grid(row=2, sticky=W)
        label_cidade.grid(row=3, sticky=W)
        input_cidade.grid(row=4, sticky=W)
        label_bairro.grid(row=5, sticky=W)
        input_bairro.grid(row=6, sticky=W)
        label_rua.grid(row=7, sticky=W)
        input_rua.grid(row=8, sticky=W)
        label_numero.grid(row=9, sticky=W)
        input_numero.grid(row=10, sticky=W)
        btn_proximo.grid(row=11)

    def __validar_endereco(self, estado, cidade, bairro, rua, numero):
        endereco = Endereco(estado, cidade, bairro, rua, numero)
        self.__conta.setEndereco(endereco)
        # self.__tela_endereco.destroy()
        self.__adicionar_senha()
        # print(self.__conta.getEndereco.getEstado)
        # print(self.__conta.getEndereco.getCidade)
        # print(self.__conta.getEndereco.getBairro)
        # print(self.__conta.getEndereco.getRua)
        # print(self.__conta.getEndereco.getNumero)
    
    def __adicionar_senha(self):
        self.__tela_senha = Tk()
        self.__tela_senha.title("Senha")
        self.__tela_senha.geometry("250x270+610+153")
        self.__tela_senha.configure(background=self.__cor_indigo)
        self.__tela_senha.resizable(width=False, height=False)

        label_senha = Label(self.__tela_senha, text='Senha:*', font=('Ivy 11'), bg=self.__cor_indigo, fg=self.__cor_branco)


        label_obs_senha = Label(self.__tela_senha, text='OBS: A senha deve conter 8 caractecres', font=('Ivy 8'), bg=self.__cor_indigo, fg=self.__cor_branco )

        input_senha = Entry(self.__tela_inf_pessoais)

        btn_proximo = Button(self.__tela_endereco, text='Próximo', font=('Ivy 11'))

        label_senha.grid(row=0, sticky=W)
        label_obs_senha.grid(row=1, sticky=W)
        input_senha.grid(row=2, sticky=W)
        btn_proximo.grid(row=3)

        

app = App()

app.menu_inicial()