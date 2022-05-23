from sqlalchemy import true
from Endereco import Endereco
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from criarBanco import session, ContaCorrente as ContaCorrenteDB, ExtratoContaCorrente as ExtratoContaCorrenteDB, ContaPoupanca as ContaPoupancaDB, ExtratoContaPoupanca as ExtratoContaPoupancaDB

# from sqlalchemy.orm import sessionmaker
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
    
    def tela_senha_chequeEspecial(self):
        self.layout = [
            [sg.Text('Senha:*')],
            [sg.Text('OBS: A senha deve conter pelo menos 8 caracteres')],
            [sg.Input(key='senha', password_char='*')],
            [sg.Text('Cheque Especial:*')],
            [sg.Radio('Sim', 'cheque especial', key='sim_cheque_especial'), sg.Radio('Não', 'cheque especial', key='nao_cheque_especial')],
            [sg.Button('Finalizar')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()
    
    def tela_login(self):
        self.layout = [
            [sg.Text('Faça o login')],
            [sg.Text('CPF:')],
            [sg.Input(key='cpf')],
            [sg.Text('Senha:')],
            [sg.Input(key='senha', password_char='*')],
            [sg.Button('Entrar')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()
    
    def tela_operacoes_conta(self):
        self.layout = [
            [sg.Text('Escolha dentre as operações')],
            [sg.Button('Sacar'), sg.Button('Depositar'), sg.Button('Extrato')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_sacar(self):
        self.layout = [
            [sg.Text('Digite o valor a ser sacado:*')],
            [sg.Input(key='saque')],
            [sg.Button('Sacar')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()


class App:
    def __init__(self):
        self.tela = AppTela()
        self.conta = None
        self.usuarioLogado = None

    def criar_conta(self, tipo):
        if tipo == 'Corrente':
            self.conta = ContaCorrente()
            try:
                ultimo_registro_conta_corrente = session.query(ContaCorrenteDB).order_by(ContaCorrenteDB.id.desc()).first()
                # print('CONSULTA',ultimo_registro_conta_corrente.id, type(ultimo_registro_conta_corrente.id))
                self.conta.setNumero(ultimo_registro_conta_corrente.id)
            except:
                self.conta.setNumero(0)

        elif tipo == 'Poupança':
            self.conta = ContaPoupanca()
            try:
                ultimo_registro_conta_poupanca = session.query(ContaPoupancaDB).order_by(ContaPoupancaDB.id.desc()).first()
                self.conta.setNumero(ultimo_registro_conta_poupanca.id)
            except:
                self.conta.setNumero(0)


    def validar_dados_pessoais(self, nome, cpf):
        sentenca_nome = self.conta.setNome(nome)
        sentenca_cpf = self.conta.setCpf(cpf)

        if session.query(ContaCorrenteDB).filter_by(cpf=cpf).first() and isinstance(self.conta, ContaCorrente) or  session.query(ContaPoupancaDB).filter_by(cpf=cpf).first() and isinstance(self.conta, ContaPoupanca):
            sg.Popup('Este CPF já foi cadastrado')
            return False

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
        sentenca_rua = self.conta.getEndereco.setRua(rua)
        sentenca_numero = self.conta.getEndereco.setNumero(numero)
       

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
    
    def validar_senha(self, senha):
        sentenca_senha = self.conta.setSenha(senha)
        
        if sentenca_senha == False:
            sg.Popup('Senha inválida!')
            return False

        return True

    def validar_login(self, cpf, senha):
        if cpf == '' or senha == '':
            sg.Popup('ERRO: CPF ou Senha inválida!')
            return False
        
        if isinstance(self.conta, ContaCorrente):
            usuario = session.query(ContaCorrenteDB).filter_by(cpf=cpf).first()
        elif isinstance(self.conta, ContaPoupanca):
            usuario = session.query(ContaPoupancaDB).filter_by(cpf=cpf).first()
        
        if not usuario:
            sg.Popup('ERRO: CPF inválido!')
            return False
        
        if usuario.senha != senha:
            sg.Popup('ERRO: Senha inválida!')
            return False

        self.usuarioLogado = usuario
        print('SALDO DO USUARIO LOGADO', self.usuarioLogado.saldo)
        return True
    
    def validar_saque(self,  valor):
        # sentenca_senha = self.conta.setSenha(senha)
        valor = float(valor)

        if valor < 0:
            sg.Popup('Valor inválido!')
            return False
        
        NovoSaldo = self.usuarioLogado.saldo - valor
        chequeEspecial = self.usuarioLogado.valorChequeEspecial

        if NovoSaldo < 0:
            diferenca = chequeEspecial - abs(NovoSaldo)
            if chequeEspecial != 0.0 and (diferenca >= 0):
                self.usuarioLogado.valorChequeEspecial = diferenca 
                self.usuarioLogado.saldo = 0.0
                session.commit()
                return True
            else:
                sg.Popup('Você não possui saldo suficiente para fazer esta operação')
                return False
    
            
        self.usuarioLogado.saldo -= valor
        session.commit()

        return True
        


    def run(self):
        event, values = self.tela.tela_inicial()
        self.tela.window.Close()
        
        if event == 'Criar uma conta':
            event, values = self.tela.tela_tipo_conta()
            self.tela.window.Close()

            if event == sg.WIN_CLOSED or event == 'Exit':
                quit()

            self.criar_conta(event)

            while True:
                event, values = self.tela.tela_dados_pessoais()
                self.tela.window.Close()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                sentenca = self.validar_dados_pessoais(values['nome'], values['cpf'])

                if sentenca == True:
                    break
            
            while True:
                event, values = self.tela.tela_endereco()
                self.tela.window.Close()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                sentenca = self.validar_endereco(values['estado'], values['cidade'], values['bairro'], values['rua'], values['numero'])

                if sentenca == True:
                    break
            
            while True:
                event, values = self.tela.tela_senha_chequeEspecial()
                self.tela.window.Close()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                sentenca = self.validar_senha(values['senha'])

                if sentenca == True:
                    if values['sim_cheque_especial'] == True:
                        self.conta.setValorChequeEspecial(500)
                    
                    
                    #Gravar no Banco
                    
                    if isinstance(self.conta, ContaCorrente):
                        gravarConta = ContaCorrenteDB(
                            numeroConta = self.conta.getNumero,
                            saldo = self.conta.getSaldo,
                            agencia = self.conta.getAgencia,
                            valorChequeEspecial = self.conta.getValorChequeEspecial, 
                            nome = self.conta.getNome,
                            cpf = self.conta.getCpf,
                            senha = self.conta.getSenha,
                            estado = self.conta.getEndereco.getEstado,
                            cidade = self.conta.getEndereco.getCidade,
                            bairro = self.conta.getEndereco.getBairro,
                            rua = self.conta.getEndereco.getRua,
                            numeroEndereco = self.conta.getEndereco.getNumero,
                            data_criacao = self.conta.getDataCriacao,
                        )

                    elif isinstance(self.conta, ContaPoupanca):
                        gravarConta = ContaPoupancaDB(
                            numeroConta = self.conta.getNumero,
                            saldo = self.conta.getSaldo,
                            agencia = self.conta.getAgencia,
                            valorChequeEspecial = self.conta.getValorChequeEspecial, 
                            nome = self.conta.getNome,
                            cpf = self.conta.getCpf,
                            senha = self.conta.getSenha,
                            estado = self.conta.getEndereco.getEstado,
                            cidade = self.conta.getEndereco.getCidade,
                            bairro = self.conta.getEndereco.getBairro,
                            rua = self.conta.getEndereco.getRua,
                            numeroEndereco = self.conta.getEndereco.getNumero,
                            data_criacao = self.conta.getDataCriacao,
                            data_atualizacao_rendimento_poupanca = self.conta.getDataCriacao
                        )

                    

                    # print(f'self.conta.getNumero: {self.conta.getNumero}')
                    # print(f'self.conta.getSaldo : {self.conta.getSaldo}')
                    # print(f'self.conta.getAgencia : {self.conta.getAgencia}')
                    # print(f'self.conta.getValorChequeEspecial : {self.conta.getValorChequeEspecial}')
                    # print(f'self.conta.getNome : {self.conta.getNome}')
                    # print(f'self.conta.getCpf : {self.conta.getCpf}')
                    # print(f'self.conta.getSenha : {self.conta.getSenha}')
                    # print(f'self.conta.getEndereco.getEstado : {self.conta.getEndereco.getEstado}')
                    # print(f'self.conta.getEndereco.getCidade : {self.conta.getEndereco.getCidade}')
                    # print(f'self.conta.getEndereco.getBairro : {self.conta.getEndereco.getBairro}')
                    # print(f'self.conta.getEndereco.getRua : {self.conta.getEndereco.getRua}')
                    # print(f'self.conta.getEndereco.getNumero: {self.conta.getEndereco.getNumero}')
                    # print(f'self.conta.getDataCriacao : {self.conta.getDataCriacao}')
                    
                    session.add(gravarConta)
                    session.commit()

                    #     sg.Popup('Dados foram gravados')
                    # except:
                    #     sg.Popup('Error')

                   
                    self.run()

                    break
        elif event == 'Acessar Conta':
            event, values = self.tela.tela_tipo_conta()
            self.tela.window.Close()

            if event == sg.WIN_CLOSED or event == 'Exit':
                quit()

            self.criar_conta(event)

            while True:
                event, values = self.tela.tela_login()
                self.tela.window.Close()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                sentenca = self.validar_login(values['cpf'], values['senha'])

                if sentenca == True:
                    break

            event, values = self.tela.tela_operacoes_conta()
            self.tela.window.Close()

            if event == 'Sacar':
                while True:
                    event, values = self.tela.tela_sacar()
                    self.tela.window.Close()

                    if event == sg.WIN_CLOSED or event == 'Exit':
                        quit()
                    
                    sentenca = self.validar_saque(values['saque'])

                    if sentenca == True:
                        break





            


app = App()

app.run()
