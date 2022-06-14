from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self):
        super().__init__()
    
    def agencia(self, agencia = '034'):
        self._agencia = agencia
