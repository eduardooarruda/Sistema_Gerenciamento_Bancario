class Endereco:
    def __init__(self):
        self.__estado = None
        self.__cidade = None
        self.__bairro = None
        self.__rua = None
        self.__numero = None

    @property
    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        if estado == '':
            return False
        self.__estado = estado
        return True

    @property
    def getCidade(self):
        return self.__cidade

    def setCidade(self, cidade):
        if cidade == '':
            return False
        self.__cidade = cidade
        return True

    @property
    def getBairro(self):
        return self.__bairro

    def setBairro(self, bairro):
        if bairro == '':
            return False
        self.__bairro = bairro
        return True

    @property
    def getRua(self):
        return self.__rua

    def setRua(self, rua):
        if rua == '':
            return False
        self.__rua = rua
        return True

    @property
    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        if numero == '':
            return False
        self.__numero = numero
        return True
