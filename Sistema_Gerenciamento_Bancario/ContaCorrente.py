from Conta import Conta
from Emprestimo import Emprestimo

class ContaCorrente(Conta, Emprestimo):
    def __init__(self):
        Conta.__init__(self)
    
    def agencia(self, agencia = '034'):
        self._agencia = agencia
