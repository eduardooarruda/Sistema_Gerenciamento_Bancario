from random import randrange


class Conta:
    def __init__(self, nome, cpf, endereco, senha, chequeEspecial):
        self._numero = self._criarNumero()
        self._saldo = 0
        self._agencia = '039'
        self._valorChequeEspecial = 0
        self._nome = nome
        self._cpf = self.setCpf(cpf)
        self._endereco = endereco
        self._senha = self.setSenha(senha)
        self._chequeEspecial = chequeEspecial
        
    def _criarNumero(self):
         id = 5859
         dv = randrange(1,10)
         numero = '0' * (8 - len(str(id))) + str(id) + '-' + str(dv)
         return numero
    
    def setCpf(self, cpf):
         cpf = str(cpf)
        
         if  len(cpf) != 14:
             return 'CPF inválido'
                 
         elif cpf[3] != '.' and cpf[7] != '.' and cpf[11]  != '-':
                 return 'CPF inválido' 
         try:
             aux = cpf.replace('.', '')
             aux = aux.replace('-', '')
             int(aux)
         except:
             return 'CPF inválido'
         return cpf
    
    @property
    def getNumero(self):
        return self._numero
        
    @property    
    def getSaldo(self):
        return self._saldo
        
    @property  
    def getAgencia(self):
        return self._agencia
    
    @property 
    def getNome(self):
        return self._nome
        
    @property  
    def getCpf(self):
        return self._cpf
      
    @property     
    def getEndereco(self):
        return self._endereco  
    
    @property
    def getSenha(self):
        return self._senha

    @property
    def getChequeEscpecial(self):
        return self._checkEspecial
    
    @property
    def getValorChequeEspecial(self):
        return self._valorChequeEspecial

    def setSenha(self, senha):
        if len(str(senha)) < 8:
            return 'Senha muito curta'
        return senha

    def setValorCheckEspecial(self, valor):
        if valor < 0:
            return False
        
        self._valorChequeEspecial = valor
        return True

    def adicionarValor(self, valor):
        if valor < 0:
            return False

        self._saldo += valor
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
                
                
