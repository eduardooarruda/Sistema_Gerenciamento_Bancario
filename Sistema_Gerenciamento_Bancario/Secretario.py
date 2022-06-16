from Funcionario import Funcionario

class Secretario(Funcionario):
    def __init__(self):
        super().__init__()
    
    def setBeneficios(self):
        beneficios = {'Vale alimentação':500,
                      'Vale transporte':200,
                      'Auxílio educação': 600}
        self._beneficios = beneficios

    @property
    def getSalario(self):
        return self._salario + sum(self.getBeneficios.values())

