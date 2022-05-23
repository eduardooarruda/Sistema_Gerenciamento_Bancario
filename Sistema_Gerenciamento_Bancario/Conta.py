from random import randrange
from Endereco import Endereco
from datetime import datetime, timezone, timedelta
# import datetime

class Conta:
    def __init__(self):
        self.__saldo = 0
        self.__agencia = '039'
        # self.__chequeEspecial = False
        self.__valorChequeEspecial = 0
        self.__endereco = Endereco()
        self.__data_criacao =  self.__setDataCriacao()
        self.__numero = None
        self.__nome = None
        self.__cpf = None
        self.__senha = None
        
    @property
    def getNumero(self):
        return self.__numero
    
    def setNumero(self, idBanco):
        idBanco = idBanco+1
        dv = randrange(1,10)
        numero = '0' * (8 - len(str(idBanco))) + str(idBanco) + '-' + str(dv)
        self.__numero = numero

    @property    
    def getSaldo(self):
        return self.__saldo

    def adicionarValor(self, valor):
        if valor < 0:
            return False

        self.__saldo += valor
        return  True
    
    def retirarValor(self, valor):
        if valor < 0:
            return False
        
        NovoSaldo = self.getSaldo - valor

        if NovoSaldo < 0:
            if self.getChequeEscpecial == True and (self.getValorChequeEspecial - abs(NovoSaldo) > 0):
                self.setValorCheckEspecial(abs(NovoSaldo))
                self._saldo = 0
                return True
            else:
                return False
        else:
            self._saldo -= valor

    @property  
    def getAgencia(self):
        return self.__agencia
    
    @property 
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        if nome == '':
            return False
        self.__nome = nome
        return True
        
    @property  
    def getCpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        cpf = str(cpf)
    
        if  len(cpf) != 14:
            return False
                
        elif cpf[3] != '.' and cpf[7] != '.' and cpf[11]  != '-':
                return False 
        try:
            aux = cpf.replace('.', '')
            aux = aux.replace('-', '')
            int(aux)
        except:
            return False
        self.__cpf = cpf
        return True
    
      
    @property     
    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco =  endereco
        return True
    
    @property
    def getSenha(self):
        return self.__senha
    
    def setSenha(self, senha):
        if len(str(senha)) < 8:
            return False
        self.__senha = senha
        return True

    # @property
    # def getChequeEscpecial(self):
    #     return self.__chequeEspecial

    # def setChequeEscpecial(self, sentenca):
    #     self.__chequeEspecial = sentenca
    
    @property
    def getValorChequeEspecial(self):
        return self.__valorChequeEspecial


    def setValorChequeEspecial(self, valor):
        if valor < 0 or type(valor) != int:
            return False
        
        self.__valorChequeEspecial = valor
        return True

    @property
    def getDataCriacao(self):
        return self.__data_criacao

    def __setDataCriacao(self):
        data_atual = datetime.now()
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)
        data = data_atual.astimezone(fuso_horario)
        data = data.strftime('%d/%m/%Y %H:%M:%S')
        data_atual = datetime.strptime(data,'%d/%m/%Y %H:%M:%S' )
        return data_atual
        
           
