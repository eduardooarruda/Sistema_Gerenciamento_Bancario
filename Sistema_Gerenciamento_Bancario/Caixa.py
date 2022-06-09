from Funcionario import Funcionario


class Caixa(Funcionario):
    def __init__(self):
        super().__init__()

    def setBeneficios(self):
        beneficios = {'Vale alimentação':400,
                      'Vale transporte':120,
                      'Auxílio educação': 600}
        self._beneficios = beneficios

    @property
    def getSalario(self):
        return self._salario + sum(self.getBeneficios.values())
    

