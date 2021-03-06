from Endereco import Endereco
from ContaCorrente import ContaCorrente
from datetime import datetime
from abc import ABC, abstractmethod
from random import randrange

class Funcionario(ABC):
    def __init__(self):
        self.__nome = None
        self.__cargoAtual = None
        self._salario = None
        self.__jornada = None
        self._beneficios = None
        self.__dataAdmissao = self.__criarDataAdmissao()
        self.__numero_funcioanario = randrange(100000, 999999)
        self.__conta = ContaCorrente()


    
    @property
    def getJornada(self):
        return self.__jornada

    def setJornada(self, jornada):
        if jornada.replace(" ", "") == '':
            return False
        self.__jornada = jornada
        return True      

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
            if salario.replace(' ', '') == '':
                return False
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

    def __criarDataAdmissao(self):
        data_atual = datetime.today()
        return data_atual
    
    @property
    def getNumero(self):
        return self.__numero_funcioanario
    
