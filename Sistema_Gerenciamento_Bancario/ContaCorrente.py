from Conta import Conta

class ContaCorrente(Conta):
    def __init__(self, nome, cpf, endereco, senha, checkEspecial):
        super().__init__(nome, cpf, endereco, senha, checkEspecial)