from Endereco import Endereco
from ContaCorrente import ContaCorrente
from datetime import datetime, timezone, timedelta
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self):
        self.__nome = None
        self.__cargoAtual = None
        self._salario = None
        self.__horario = None
        self.__beneficios = None
        self.__dataAdmissao = self.__setDataAdmissao()
        self.__numero = '1234'
        self.__conta = ContaCorrente()
        self.__endereco = Endereco()

    
    @property
    def getHorario(self):
        return self.__horario

    def setHorario(self, horario):
        self.__horario = horario      

    @property
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        if nome.replace(" ", "") == '':
            return False
        self.__nome = nome
        return True
    
    @property
    def getCargoAtual(self):
        return self.__cargoAtual

    def setCargoAtual(self, cargoAtual):
        if cargoAtual.replace(' ', '') == '':
            return False
        self.__cargoAtual = cargoAtual
        return True

    @abstractmethod
    def getSalario(self):
        pass

    def setSalario(self, salario):
        try:
            self._salario = float(salario)
            return True
        except ValueError:
            return False 

    @abstractmethod
    def setBeneficios(self):
        pass

    @property
    def getBeneficios(self):
        return self._beneficios
            

    @property
    def getDataAdimissao(self):
        return self.__dataAdmissao

    def __setDataAdmissao(self):
        data_atual = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data = data_atual.astimezone(fuso_horario)
        data = data.strftime('%d/%m/%Y %H:%M:%S')
        data_atual = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')
        return data_atual
    
