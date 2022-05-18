import datetime
from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, nome, cpf, endereco, senha, checkEspecial):
        super().__init__(nome, cpf, endereco, senha, checkEspecial)
        #A taxa corresponde a 0,017% por dia
        self._taxa = 0.00017
    
    def getTaxa(self):
        return self._taxa

    def atualizarSaldo(self):
        #Data da criação da Conta
        dataCriacao = datetime.date(2022, 4, 13)
        dataAtual = datetime.date.today()
        diferencaEmDias = (dataAtual - dataCriacao).days
        return self.getSaldo + self.getTaxa() * diferencaEmDias * self.getSaldo
        
    

