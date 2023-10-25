class Escolaridade:
    
    def __init__(self):
        self.__tipoEscolaridade = None
        self.__Pessoa = []

    def setTipoEscolaridade(self, tipoEscolaridade):
        self.__tipoEscolaridade = tipoEscolaridade

    def getTipoEscolaridade(self):
        return self.__tipoEscolaridade

    def setPessoa(self, Pessoa):
        self.__Pessoa = Pessoa

    def addPessoa(self, Pessoa):
        self.__Pessoa.append(Pessoa)

    def removePessoa(self, Pessoa):
        self.__Pessoa.remove(Pessoa)
    
    def getPessoa(self):
        return self.__Pessoa
    
    