class Pessoa:

    def __init__(self):
        self.__Nome = None
        self.__Escolaridade = None
        self.__estadoNaturalidade = None
        self.__Cidade = None

    def setNome(self, Nome):
        self.__Nome = Nome

    def getNome(self):
        return self.__Nome
    
    def setEscolaridade(self, Escolaridade):
        self.__Escolaridade = Escolaridade

    def getEscolaridade(self):
        return self.__Escolaridade
    
    def setEstadoNaturalidade(self, EstadoNaturalidade):
        self.__estadoNaturalidade = EstadoNaturalidade

    def getEstadoNaturalidade(self):
        return self.__estadoNaturalidade
    
    def setCidade(self, Cidade):
        self.__Cidade = Cidade

    def getCidade(self):
        return self.__Cidade