class Cidade:
    
    def __init__(self):
        self.__NomeCidade = ""
        self.__Estado = ""
        self.__Escolas = []

    def setNomeCidade(self,NomeCidade):
        self.__NomeCidade = NomeCidade

    def getNomeCidade(self):
        return self.__NomeCidade
    
    def setEstado(self, Estado):
        self.__Estado = Estado

    def getEstado(self):
        return self.__Estado
    
    def setEscola(self, Escola):
        self.__Escolas = Escola

    def addEscola(self, Escola):
        self.__Escolas.append(Escola)

    def removeEscola(self, Escola):
        self.__Escolas.remove(Escola)

    def getEscola(self):
        return self.__Escolas