class Endereco:
    def __init__(self, estado, cidade, bairro, rua, numero, logradouro='Nenhum'):
        self._estado = estado
        self._cidade = cidade
        self._bairro = bairro
        self._rua = rua
        self._logradouro = logradouro
        self._numero = numero
     
    @property
    def getEstado(self):
        return self._estado
    
    @property
    def getCidade(self):
        return self._cidade
    
    @property       
    def getBairro(self):
        return self._bairro
    
    @property 
    def getRua(self):
        return self._rua
     
    @property
    def getLogradouro(self):
        return self._logradouro
    
    @property
    def getNumero(self):
        return self._numero