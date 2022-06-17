from datetime import datetime, timezone, timedelta
from abc import ABC, abstractmethod

class Emprestimo(ABC):
    def __init__(self):
        self.__data_emprestimo = self.__dataCriacao()
        self.__valor_emprestimo = None
        self._taxa_emprestimo = None
    
    def __dataCriacao(self):
        data_atual = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data = data_atual.astimezone(fuso_horario)
        data = data.strftime('%d/%m/%Y %H:%M:%S')
        data_atual = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')
        return data_atual
    
    def getData(self):
        return self.__data_emprestimo

    def setValor(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self.__valor_emprestimo = valor
                return True
            else:
                return False
        except ValueError:
            return False

    def getValor(self):
        return self.__valor_emprestimo

    @abstractmethod
    def setTaxaEmprestimo(self,tipoUsuario):
        pass
       

    def getTaxaEmprestimo(self):
        return self.__taxa_emprestimo
    
    