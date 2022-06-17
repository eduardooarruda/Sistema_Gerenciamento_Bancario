from Conta import Conta
from Emprestimo import Emprestimo

class ContaCorrente(Conta, Emprestimo):
    def __init__(self):
        Conta.__init__(self)
    
    def agencia(self, agencia = '034'):
        self._agencia = agencia
    
    def setTaxaEmprestimo(self, tipo_usuario):
        if tipo_usuario == 'cliente':
            self._taxa_emprestimo == 0.20
            return True
        elif tipo_usuario == 'funcionario':
            self._taxa_emprestimo == 0.15
            return True
        return False 
