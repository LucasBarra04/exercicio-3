
class Estado:

    def __init__(self):
        self.__siglaEstado = ""
        self.__Cidades = []

    def setSiglaEstado(self, siglaEstado):
        self.__siglaEstado = siglaEstado

    def getSiglaEstado(self):
        return self.__siglaEstado
    
    def setCidade(self, Cidade):
        self.__Cidades = Cidade

    def addCidade(self, Cidade):
        self.__Cidades.append(Cidade)
    
    def removeCidade(self, Cidade):
        self.__Cidades.remove(Cidade)

    def getCidade(self):
        return self.__Cidades