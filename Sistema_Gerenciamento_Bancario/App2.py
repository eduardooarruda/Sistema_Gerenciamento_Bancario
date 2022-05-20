from Endereco import Endereco
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente

import PySimpleGUI as sg
sg.theme('DarkAmber')

class AppTela:
    def __init__(self):
        self.layout = None
        self.window = None

    def tela_inicial(self):
        self.layout = [
            [sg.Text('Escolhar uma opção:')],
            [sg.Button('Criar uma conta'), sg.Button('Acessar Conta')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()
    
    def tela_tipo_conta(self):
        self.layout = [
            [sg.Text('Escolhar o tipo da conta:')],
            [sg.Button('Corrente'), sg.Button('Poupança')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_dados_pessoais(self):
        self.layout = [
            [sg.Text('Nome completo:*')],
            [sg.Input(key='nome')],
            [sg.Text('CPF:*')],
            [sg.Text('OBS: O CPF deve está no seguinte formato 000.000.000-00')],
            [sg.Input(key='cpf')],
            [sg.Button('Próximo')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()
    
    def tela_endereco(self):
        self.layout = [
            [sg.Text('Estado:*')],
            [sg.Input(key='estado')],
            [sg.Text('Cidade:*')],
            [sg.Input(key='cidade')],
            [sg.Text('Bairro:*')],
            [sg.Input(key='bairro')],
            [sg.Text('Rua:*')],
            [sg.Input(key='rua')],
            [sg.Text('Número:*')],
            [sg.Input(key='numero')],
            [sg.Button('Próximo')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

class App:
    def __init__(self):
        self.tela = AppTela()
        self.conta = None
    
    def criar_conta(self, tipo):
        if tipo == 'Corrente':
            self.conta = ContaCorrente()
        elif tipo == 'Poupança':
            self.conta = ContaPoupanca()
        # print(self.conta)

    def validar_dados_pessoais(self, nome, cpf):
        sentenca_nome = self.conta.setNome(nome)
        sentenca_cpf = self.conta.setCpf(cpf)

        if sentenca_nome == False:
            sg.Popup('Nome inválido!')
            return False

        if sentenca_cpf == False:
            sg.Popup('CPF inválido!')
            return False
    
        return True

    def validar_endereco(self, estado, bairro, cidade, rua, numero):
        sentenca_estado = self.conta.getEndereco.setEstado(estado)
        sentenca_bairro = self.conta.getEndereco.setBairro(bairro)
        sentenca_cidade = self.conta.getEndereco.setCidade(cidade)
        sentenca_rua = self.conta.getEndereco.setEstado(rua)
        sentenca_numero = self.conta.getEndereco.setEstado(numero)
       

        if sentenca_estado == False:
            sg.Popup('Estado inválido!')
            return False

        if sentenca_cidade == False:
            sg.Popup('Cidade inválida!')
            return False
        
        if sentenca_bairro == False:
            sg.Popup('bairro inválido!')
            return False
        
        if sentenca_rua == False:
            sg.Popup('Rua inválida!')
            return False

        if sentenca_numero == False:
            sg.Popup('Numéro inválido!')
            return False
        
        return True

    def run(self):
        event, values = self.tela.tela_inicial()
        self.tela.window.Close()
        
        if event == 'Criar uma conta':
            event, values = self.tela.tela_tipo_conta()
            self.tela.window.Close()

            self.criar_conta(event)

            while True:
                event, values = self.tela.tela_dados_pessoais()
                self.tela.window.Close()

                sentenca = self.validar_dados_pessoais(values['nome'], values['cpf'])

                if sentenca == True:
                    break
            
            while True:
                event, values = self.tela.tela_endereco()
                self.tela.window.Close()

                sentenca = self.validar_endereco(values['estado'], values['cidade'], values['bairro'], values['rua'], values['numero'])

                if sentenca == True:
                    break
            
            


app = App()

app.run()
# app = AppTela()
# conta = None

# button, values = app.tela_inicial()
# app.window.Close()

# if button == 'Criar uma conta':
#     event, values = app.tela_tipo_conta()

#     if event == 'Corrente':
#         conta = ContaCorrente()
#     elif event == 'Poupança':
#         conta = ContaPoupanca()
    
#     app.window.Close()

#     while True:
#         event, values = app.tela_dados_pessoais()
#         sentenca_nome = conta.setNome(values['nome'])
#         sentenca_cpf = conta.setCpf(values['cpf'])
#         app.window.Close()
        
#         if event == None:
#             break

#         if sentenca_nome == False:
#             sg.Popup('Nome inválido!')
#         if sentenca_cpf == False:
#             sg.Popup('CPF inválido!')
#         else:

            
#             event, values = app.tela_endereco()

#             break
            
# app.window.Close()