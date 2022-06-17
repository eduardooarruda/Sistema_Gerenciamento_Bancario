from sqlalchemy import Float, true
from Endereco import Endereco
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from Gerente import Gerente
from Diretor import Diretor
from Caixa import Caixa
from Secretario import Secretario
from criarBanco import session, ContaCorrente as ContaCorrenteDB, ExtratoContaCorrente as ExtratoContaCorrenteDB, ContaPoupanca as ContaPoupancaDB, ExtratoContaPoupanca as ExtratoContaPoupancaDB, Funcionario as FuncionarioDB, Beneficios as BeneficiosDB, EmprestimoContaPoupanca as EmprestimoContaPoupancaDB, EmprestimoContaCorrente as EmprestimoContaCorrenteDB
from datetime import datetime, timezone, timedelta
import PySimpleGUI as sg
sg.theme('DarkAmber')


class AppTela:
    def __init__(self):
        self.layout = None
        self.window = None

    def tela_inicial(self):
        self.layout = [
            [sg.Text('Escolhar uma opção:', font=("Helvetica", 15))],
            [sg.Button('Criar uma conta'), sg.Button('Acessar Conta')],
            [sg.Button('Funcionário', size=(25,))]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout, element_justification='c')
        return self.window.Read()

    def tela_tipo_conta(self):
        self.layout = [
            [sg.Text('Escolhar o tipo da conta:', font=("Helvetica", 15))],
            [sg.Button('Corrente'), sg.Button('Poupança')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_dados_pessoais(self):
        self.layout = [
            [sg.Text('Nome completo:*', font=("Helvetica", 13))],
            [sg.Input(key='nome')],
            [sg.Text('CPF:*',  font=("Helvetica", 13))],
            [sg.Text('OBS: O CPF deve está no seguinte formato 000.000.000-00')],
            [sg.Input(key='cpf')],
            [sg.Button('Próximo')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_endereco(self):
        self.layout = [
            [sg.Text('Estado:*',  font=("Helvetica", 13))],
            [sg.Input(key='estado')],
            [sg.Text('Cidade:*',  font=("Helvetica", 13))],
            [sg.Input(key='cidade')],
            [sg.Text('Bairro:*', font=("Helvetica", 13))],
            [sg.Input(key='bairro')],
            [sg.Text('Rua:*',  font=("Helvetica", 13))],
            [sg.Input(key='rua')],
            [sg.Text('Número:*',  font=("Helvetica", 13))],
            [sg.Input(key='numero')],
            [sg.Button('Próximo')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_senha_chequeEspecial(self):
        self.layout = [
            [sg.Text('Senha:*', font=("Helvetica", 13))],
            [sg.Text('OBS: A senha deve conter pelo menos 8 caracteres')],
            [sg.Input(key='senha', password_char='*')],
            [sg.Text('Cheque Especial:*', font=("Helvetica", 13))],
            [sg.Radio('Sim', 'cheque especial', key='sim_cheque_especial'), sg.Radio(
                'Não', 'cheque especial', key='nao_cheque_especial')],
            [sg.Button('Finalizar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_login(self):
        self.layout = [
            [sg.Text('Faça o login', font=("Helvetica", 15))],
            [sg.Text('CPF:', font=("Helvetica", 13))],
            [sg.Input(key='cpf')],
            [sg.Text('Senha:', font=("Helvetica", 13))],
            [sg.Input(key='senha', password_char='*')],
            [sg.Button('Entrar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_operacoes_conta(self, usuario):
        self.layout = [
            [sg.Image(filename='imagens\\user.png')],
            [sg.Text(f'Seja bem-vindo, {usuario.nome}',font=("Helvetica", 25))],
            [sg.Text(f'Saldo: {usuario.saldo}',font=("Helvetica", 20))],
            [sg.Text('Escolha dentre as operações', font=("Helvetica", 13))],
            [sg.Button('Sacar'), sg.Button('Depositar'),
             sg.Button('Extrato'), sg.Button('Voltar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout, element_justification='c')
        return self.window.Read()

    def tela_sacar(self):
        self.layout = [
            [sg.Text('Digite o valor a ser sacado:*', font=("Helvetica", 13))],
            [sg.Input(key='saque')],
            [sg.Button('Sacar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_depositar(self):
        self.layout = [
            [sg.Text('Digite o valor a ser depositado:*', font=("Helvetica", 13))],
            [sg.Input(key='deposito')],
            [sg.Button('Depositar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_extrato(self, conta, usuario):
        tipo_conta = None
        extrato = None

        try:
            if isinstance(conta, ContaCorrente):
                tipo_conta = 'Corrente'
                extrato = session.query(ExtratoContaCorrenteDB).filter_by(
                    idConta=usuario.id).all()
            elif isinstance(conta, ContaPoupanca):
                tipo_conta = 'Poupança'
                extrato = session.query(ExtratoContaPoupancaDB).filter_by(
                    idConta=usuario.id).all()
        finally:

            layout_esquerda = [
                [sg.Text('Extrato')],
                [sg.Text(f'Agência: {usuario.agencia}')],
                [sg.Text(f'Número da conta: {usuario.numeroConta}')],
                [sg.Text(f'Nome: {usuario.nome}')],
                [sg.Text(f'tipo da conta: {tipo_conta}')]
            ]

            layout_direita = [

            ]

            if extrato:
                cabecalho = ['Data', 'Tipo de operação', 'valor', 'Saldo Novo', 'Cheque_especial']

                valores = []

                for operacao in extrato:
                    valores.append([f'{operacao.data}', f'{operacao.tipo_operacao}',f'{abs(operacao.saldo_anterior-operacao.saldo_novo)}', f'{operacao.saldo_novo}', f'{usuario.valorChequeEspecial}'])
                    

                layout_direita.append([sg.Table(
                    values=valores,
                    headings=cabecalho,
                    max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    
                )])

            layout_direita.append([sg.Button('OK')])

            layout = [
                [sg.Column(layout_esquerda), sg.VSeparator(),
                sg.Column(layout_direita)]
            ]

            self.window = sg.Window(
                'Sistema de Gerenciamento Bancário', layout = layout)

            
            return self.window.Read()
        
    def tipo_funcionario(self):
        self.layout = [
            [sg.Text('Escolhar uma opção:')],
            [sg.Button('Diretor'), sg.Button('Gerente')],
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout, element_justification='c')
        return self.window.Read()
    
    def tela_login_diretor_gerente(self):
        self.layout = [
            [sg.Text('Faça o login')],
            [sg.Text('Número:')],
            [sg.Input(key='numero')],
            [sg.Text('Senha:')],
            [sg.Input(key='senha', password_char='*')],
            [sg.Button('Entrar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()

    def tela_funcoes_gerente(self):
        self.layout = [
            [sg.Button('Emprestimo', size=(25,))],
            [sg.Button('Criar Conta', size=(25,))],
            [sg.Button('Visualizar contas', size=(25,))]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout, element_justification='c')
        return self.window.Read()
    
    def tela_funcoes_diretor(self):
        self.layout = [
            [sg.Button('Emprestimo', size=(25,))],
            [sg.Button('Visualizar contas', size=(25,))],
            [sg.Button('Visualizar funcionários', size=(25,))],
            [sg.Button('Cadastrar funcionários', size=(25,))]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout, element_justification='c')
        return self.window.Read()
    
    def tela_tipo_funcionario(self):
        self.layout = [
            [sg.Button('Caixa', size=(25,))],
            [sg.Button('Direito', size=(25,))],
            [sg.Button('Gerente', size=(25,))],
            [sg.Button('Secretários', size=(25,))],
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout, element_justification='c')
        return self.window.Read()
    
    def tela_cadastrar_funcionario(self):
        self.layout = [
            [sg.Text('Nome:*',  font=("Helvetica", 13))],
            [sg.Input(key='nome')],
            [sg.Text('Salário:*', font=("Helvetica", 13))],
            [sg.Input(key='salario')],
            [sg.Text('Jornada de trabalho :*',  font=("Helvetica", 13))],
            [sg.Input(key='jornada')],
            [sg.Text('Número da conta corrente:*',  font=("Helvetica", 13))],
            [sg.Input(key='numeroConta')],
            [sg.Button('Cadastrar')]
        ]
        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', self.layout)
        return self.window.Read()
    
    def tela_visualizar_funcionarios(self):
        
    
        layout = [

        ]

        todososfuncionarios = session.query(FuncionarioDB).all()

        cabecalho = ['Nome', 'Cargo atual', 'Salário', 'Número', 'Data de admissão']

        valores = []

        for funcionario in todososfuncionarios:
            valores.append([f'{funcionario.nome}', f'{funcionario.cargo_atual}', f'{funcionario.salario}', f'{funcionario.numero}', f'{funcionario.data_adimissao}'])
            

        layout.append([sg.Table(
            values=valores,
            headings=cabecalho,
            max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            
        )])

        layout.append([sg.Button('OK')])

        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', layout = layout)

        
        return self.window.Read()

    def tela_visualizar_contas_gerente(self): 

        layout_esquerda = [

        ]

        layout_direita = [

        ]

        todas_contas_corrente = session.query(ContaCorrenteDB).all()
        todas_contas_poupanca = session.query(ContaPoupancaDB).all()

        cabecalho = ['Nome', 'Número', 'Saldo', 'Cheque especial', 'Empréstimo']

        valores_conta_corrente = []
        valores_conta_poupanca = []

        for conta_coorente in todas_contas_corrente:
            emprestimo = str(session.query(EmprestimoContaCorrenteDB).filter_by(
                    id_conta_corrente=conta_coorente.id).all())
            emprestimo = str(emprestimo) if emprestimo != '[]' else ''
            valores_conta_corrente.append([f'{conta_coorente.nome}', f'{conta_coorente.numeroConta}', f'{conta_coorente.saldo}',f'{conta_coorente.valorChequeEspecial}', emprestimo])

        for conta_poupanca in todas_contas_poupanca:
            emprestimo = str(session.query(EmprestimoContaPoupancaDB).filter_by(id_conta_poupanca=conta_coorente.id).all())
            emprestimo = str(emprestimo) if emprestimo != '[]' else ''
            valores_conta_poupanca.append([f'{conta_poupanca.nome}', f'{conta_poupanca.numeroConta}', f'{conta_poupanca.saldo}',f'{conta_poupanca.valorChequeEspecial}', emprestimo])
            
        layout_esquerda.append([sg.Text('Conta Corrente',font=("Helvetica", 13))])
        layout_esquerda.append([sg.Table(
            values=valores_conta_corrente,
            headings=cabecalho,
            max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            
        )])

        layout_direita.append([sg.Text('Conta Poupança', font=("Helvetica", 13))])
        layout_direita.append([sg.Table(
            values=valores_conta_poupanca,
            headings=cabecalho,
            max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            
        )])

        layout = [
            [sg.Column(layout_esquerda), sg.VSeparator(),
            sg.Column(layout_direita)]
        ]

        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', layout = layout, element_justification='c')
        
        return self.window.Read()

    def tela_visualizar_contas_direitor(self): 

        layout_esquerda = [

        ]

        layout_direita = [

        ]

        todas_contas_corrente = session.query(ContaCorrenteDB).all()
        todas_contas_poupanca = session.query(ContaPoupancaDB).all()

        cabecalho = ['Nome', 'CPF', 'Número', 'Saldo', 'Empréstimo']

        valores_conta_corrente = []
        valores_conta_poupanca = []

        for conta_coorente in todas_contas_corrente:
            emprestimo = str(session.query(EmprestimoContaCorrenteDB).filter_by(
                    id_conta_corrente=conta_coorente.id).all())
            emprestimo = 'Sim' if emprestimo != '[]' else 'Não'
            valores_conta_corrente.append([f'{conta_coorente.nome}', f'{conta_coorente.cpf}', f'{conta_coorente.numeroConta}', f'{conta_coorente.saldo}', emprestimo])

        for conta_poupanca in todas_contas_poupanca:
            emprestimo = str(session.query(EmprestimoContaPoupancaDB).filter_by(
                    id_conta_poupanca=conta_coorente.id).all())
            emprestimo = 'Sim' if emprestimo != '[]' else 'Não'
            valores_conta_poupanca.append([f'{conta_poupanca.nome}', f'{conta_poupanca.cpf}', f'{conta_poupanca.numeroConta}', f'{conta_poupanca.saldo}', emprestimo])
            
        layout_esquerda.append([sg.Text('Conta Corrente', font=("Helvetica", 13))])
        layout_esquerda.append([sg.Table(
            values=valores_conta_corrente,
            headings=cabecalho,
            max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            
        )])

        layout_direita.append([sg.Text('Conta Poupança', font=("Helvetica", 13))])
        layout_direita.append([sg.Table(
            values=valores_conta_poupanca,
            headings=cabecalho,
            max_col_width=35,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='-TABLE-',
            row_height=35,
            
        )])

        layout = [
            [sg.Column(layout_esquerda), sg.VSeparator(),
            sg.Column(layout_direita)]
        ]

        self.window = sg.Window(
            'Sistema de Gerenciamento Bancário', layout = layout, element_justification='c')
        
        return self.window.Read()
        


        

    


class App:
    def __init__(self):
        self.tela = AppTela()
        self.conta = None
        self.usuarioLogado = None

    def criar_conta(self, tipo):
        if tipo == 'Corrente':
            self.conta = ContaCorrente()
            self.conta.agencia()
            try:
                ultimo_registro_conta_corrente = session.query(
                    ContaCorrenteDB).order_by(ContaCorrenteDB.id.desc()).first()
                self.conta.setNumero(ultimo_registro_conta_corrente.id)
            except:
                self.conta.setNumero(0)

        elif tipo == 'Poupança':
            self.conta = ContaPoupanca()
            self.conta.agencia()
            try:
                ultimo_registro_conta_poupanca = session.query(
                    ContaPoupancaDB).order_by(ContaPoupancaDB.id.desc()).first()
                self.conta.setNumero(ultimo_registro_conta_poupanca.id)
            except:
                self.conta.setNumero(0)

    def validar_dados_pessoais(self, nome, cpf):
        sentenca_nome = self.conta.setNome(nome)
        sentenca_cpf = self.conta.setCpf(cpf)

        if session.query(ContaCorrenteDB).filter_by(cpf=cpf).first() and isinstance(self.conta, ContaCorrente) or session.query(ContaPoupancaDB).filter_by(cpf=cpf).first() and isinstance(self.conta, ContaPoupanca):
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
     
        return True

    def validar_saque(self,  valor):
        extrato = None

        try:
            valor = float(valor)
        except ValueError:
            sg.Popup('Valor inválido!')
            return False

        if valor < 0:
            sg.Popup('Valor inválido!')
            return False

        data_atual = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data = data_atual.astimezone(fuso_horario)
        data = data.strftime('%d/%m/%Y %H:%M:%S')
        data_atual = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')

        NovoSaldo = self.usuarioLogado.saldo - valor
        chequeEspecial = self.usuarioLogado.valorChequeEspecial

        if isinstance(self.conta, ContaCorrente):
            extrato = ExtratoContaCorrenteDB()
        elif isinstance(self.conta, ContaPoupanca):
            extrato = ExtratoContaPoupancaDB()

        extrato.data = data_atual
        extrato.idConta = self.usuarioLogado.id
        extrato.tipo_operacao = 'Saque'
        extrato.saldo_anterior = self.usuarioLogado.saldo

        if NovoSaldo < 0:
            diferenca = chequeEspecial - abs(NovoSaldo)
            if chequeEspecial != 0.0 and (diferenca >= 0):

                self.usuarioLogado.valorChequeEspecial = diferenca
                self.usuarioLogado.saldo = 0.0
                session.commit()

                extrato.saldo_novo = self.usuarioLogado.saldo
                session.add(extrato)
                session.commit()
                return True
            else:
                sg.Popup(
                    'Você não possui saldo suficiente para fazer esta operação')
                return False

        self.usuarioLogado.saldo -= valor
        session.commit()

        extrato.saldo_novo = self.usuarioLogado.saldo
        session.add(extrato)
        session.commit()
        return True

    def validar_deposito(self, valor):
        extrato = None

        try:
            valor = float(valor)
        except ValueError:
            sg.Popup('Valor inválido!')
            return False

        if valor < 0:
            sg.Popup('Valor inválido!')
            return False

        if isinstance(self.conta, ContaCorrente):
            extrato = ExtratoContaCorrenteDB()
        elif isinstance(self.conta, ContaPoupanca):
            extrato = ExtratoContaPoupancaDB()

        data_atual = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data = data_atual.astimezone(fuso_horario)
        data = data.strftime('%d/%m/%Y %H:%M:%S')
        data_atual = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')

        self.usuarioLogado.saldo += valor
        session.commit()

        extrato.data = data_atual
        extrato.idConta = self.usuarioLogado.id
        extrato.tipo_operacao = 'Deposito'
        extrato.saldo_anterior = self.usuarioLogado.saldo - valor
        extrato.saldo_novo = self.usuarioLogado.saldo
        session.add(extrato)
        session.commit()

        return True
    
    def validar_login_funcionario(self, numero, senha):
        if numero == ''.replace(' ', '') == '' or senha.replace(' ', '') == '':
            sg.Popup('ERRO: Número ou Senha inválida!')
            return False
        
        return True

    def validar_cadastro_funcionario(w,nome, salario, jornada, numeroConta, funcionario):
        # print("Nome", nome)
        # print("Salario", salario)
        # print("Jornada", jornada)
        # print("Numero Conta", numeroConta)
        # print("FUNCIONARIO",funcionario)

        if not funcionario.setNome(nome):
            sg.Popup('Nome inválido!')
            return False

        if not funcionario.setSalario(salario):
            sg.Popup('Salário inválido!')
            return False

        
        if not funcionario.setJornada(jornada):
            sg.Popup('jornada inválida!')
            return False
        
        if numeroConta == ''.replace(' ', ''):
            sg.Popup('número da conta corrente inválido!')
            return False

        pesquisarNumero = session.query(ContaCorrenteDB).filter_by(numeroConta = numeroConta).first()

        if pesquisarNumero == None:
            sg.Popup('número da conta corrente inválido!')
            return False


       
        funcionarioDB = FuncionarioDB(
            nome = funcionario.getNome,
            cargo_atual = funcionario.getCargoAtual,
            salario = funcionario.getSalario,
            jornada = funcionario.getJornada,
            numeroContaCorrente = numeroConta,
            data_adimissao = funcionario.getDataAdimissao,
            numero = funcionario.getNumero
        )

        session.add(funcionarioDB)
        session.commit()

        return True
        
        

    def run(self):
        event, values = self.tela.tela_inicial()
        self.tela.window.Close()

        if event == sg.WIN_CLOSED or event == 'Exit':
            quit()

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

                sentenca = self.validar_dados_pessoais(
                    values['nome'], values['cpf'])

                if sentenca == True:
                    break

            while True:
                event, values = self.tela.tela_endereco()
                self.tela.window.Close()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                sentenca = self.validar_endereco(
                    values['estado'], values['cidade'], values['bairro'], values['rua'], values['numero'])

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
                        x = self.conta.setValorChequeEspecial(500)
                       
                    # Gravar no Banco

                    if isinstance(self.conta, ContaCorrente):
                        gravarConta = ContaCorrenteDB(
                            numeroConta=self.conta.getNumero,
                            saldo=self.conta.getSaldo,
                            agencia=self.conta.getAgencia,
                            valorChequeEspecial=self.conta.getValorChequeEspecial,
                            nome=self.conta.getNome,
                            cpf=self.conta.getCpf,
                            senha=self.conta.getSenha,
                            estado=self.conta.getEndereco.getEstado,
                            cidade=self.conta.getEndereco.getCidade,
                            bairro=self.conta.getEndereco.getBairro,
                            rua=self.conta.getEndereco.getRua,
                            numeroEndereco=self.conta.getEndereco.getNumero,
                            data_criacao=self.conta.getDataCriacao,
                        )

                    elif isinstance(self.conta, ContaPoupanca):
                        gravarConta = ContaPoupancaDB(
                            numeroConta=self.conta.getNumero,
                            saldo=self.conta.getSaldo,
                            agencia=self.conta.getAgencia,
                            valorChequeEspecial=self.conta.getValorChequeEspecial,
                            nome=self.conta.getNome,
                            cpf=self.conta.getCpf,
                            senha=self.conta.getSenha,
                            estado=self.conta.getEndereco.getEstado,
                            cidade=self.conta.getEndereco.getCidade,
                            bairro=self.conta.getEndereco.getBairro,
                            rua=self.conta.getEndereco.getRua,
                            numeroEndereco=self.conta.getEndereco.getNumero,
                            data_criacao=self.conta.getDataCriacao,
                            data_atualizacao_rendimento_poupanca=self.conta.getDataCriacao
                        )

                    session.add(gravarConta)
                    session.commit()

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
                print('sentença', sentenca)
                if sentenca == True:
                    break

            while True:
                event, values = self.tela.tela_operacoes_conta(self.usuarioLogado)
                self.tela.window.Close()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                if event == 'Voltar':
                    self.run()

                if event == 'Sacar':
                    while True:
                        event, values = self.tela.tela_sacar()
                        self.tela.window.Close()

                        if event == sg.WIN_CLOSED or event == 'Exit':
                            break

                        sentenca = self.validar_saque(values['saque'])

                        if sentenca == True:
                            break

                elif event == 'Depositar':
                    while True:
                        event, values = self.tela.tela_depositar()
                        self.tela.window.Close()

                        if event == sg.WIN_CLOSED or event == 'Exit':
                            break

                        sentenca = self.validar_deposito(values['deposito'])

                        if sentenca == True:
                            break

                elif event == 'Extrato':
                    event, values = self.tela.tela_extrato(
                        self.conta, self.usuarioLogado)
                    self.tela.window.Close()
        
        elif event == 'Funcionário':
            event, values = self.tela.tipo_funcionario()
            self.tela.window.Close()
            if event == sg.WIN_CLOSED or event == 'Exit':
                quit()
            
            if event == 'Diretor':
                self.usuarioLogado = Diretor()
            elif event == 'Gerente':
                self.usuarioLogado = Gerente()
            
            while True:
                event, values = self.tela.tela_login_diretor_gerente()
                self.tela.window.Close()

                if event == sg.WIN_CLOSED or event == 'Exit':
                    quit()

                sentenca = self.validar_login_funcionario(values['numero'], values['senha'])

                if sentenca == True:
                    break
            
            if isinstance(self.usuarioLogado, Gerente):
                while True:
                    
                    event, values = self.tela.tela_funcoes_gerente()
                    self.tela.window.Close()

                    if event == sg.WIN_CLOSED or event == 'Exit':
                        quit()

                    if event == 'Emprestimo':
                        pass
                    elif event == 'Criar Conta':
                        self.run()
                    elif event == 'Visualizar contas':
                        event, values = self.tela.tela_visualizar_contas_gerente()
                        self.tela.window.Close()
            elif isinstance(self.usuarioLogado, Diretor):
                
                while True:
                    event, values = self.tela.tela_funcoes_diretor()
                    self.tela.window.Close()

                    if event == sg.WIN_CLOSED or event == 'Exit':
                        quit()

                    if event == 'Emprestimo':
                        pass

                    elif event == 'Visualizar contas':
                        event, values = self.tela.tela_visualizar_contas_direitor()
                        self.tela.window.Close()

                    elif event == 'Cadastrar funcionários':
                        event, values = self.tela.tela_tipo_funcionario()
                        self.tela.window.Close()
                        funcionario = None
                        # if event == sg.WIN_CLOSED or event == 'Exit':
                        #     quit()
                        if event == 'Caixa':
                            funcionario = Caixa()
                            funcionario.setCargoAtual('Caixa')
                        elif event == 'Direito':
                            funcionario = Diretor()
                            funcionario.setCargoAtual('Diretor')
                        elif event == 'Gerente':
                            funcionario = Gerente()
                            funcionario.setCargoAtual('Gerente')
                        elif event == 'Secretários':
                            funcionario = Secretario()
                            funcionario.setCargoAtual('Secretário')
                        
                        if isinstance(funcionario, (Caixa, Diretor, Gerente, Secretario)):
                            while True:
                                funcionario.setBeneficios()
                                event, values = self.tela.tela_cadastrar_funcionario()
                                self.tela.window.Close()
                                
                                if event == sg.WIN_CLOSED or event == 'Exit':
                                   break
                                
                                sentenca = self.validar_cadastro_funcionario(values['nome'],values['salario'], values['jornada'], values['numeroConta'], funcionario)

                                if sentenca == True:
                                    break
                            
                        
                            

                    elif event == 'Visualizar funcionários':
                        event, values = self.tela.tela_visualizar_funcionarios()
                        self.tela.window.Close()

            
if __name__ == '__main__':
    app = App()
    app.run()
