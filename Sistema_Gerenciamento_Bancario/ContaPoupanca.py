import datetime
from Conta import Conta
from Emprestimo import Emprestimo

class ContaPoupanca(Conta, Emprestimo):
    def __init__(self):
        Conta.__init__(self)
        # A taxa corresponde a 0,017% por dia
        self._taxa = 0.00017

    def getTaxa(self):
        return self._taxa

    def atualizarSaldo(self):
        # Data da criação da Conta
        dataCriacao = datetime.date(2022, 4, 13)
        dataAtual = datetime.date.today()
        diferencaEmDias = (dataAtual - dataCriacao).days
        return self.getSaldo + self.getTaxa() * diferencaEmDias * self.getSaldo

    def agencia(self, agencia = '039'):
        self._agencia = agencia

    def setTaxaEmprestimo(self, tipo_usuario):
        if tipo_usuario == 'cliente':
            self._taxa_emprestimo == 0.20
            return True
        return False 