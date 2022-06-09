from Funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self):
        super().__init__()
    
    def setBeneficios(self):
        beneficios = {'Vale alimentação':500,
                      'Vale transporte':400,
                      'Auxílio creche': 300,
                      'Plano odontológico': 700,
                      'Auxílio educação': 600}
        self._beneficios = beneficios

    @property
    def getSalario(self):
        return self._salario + sum(self.getBeneficios.values())


