from Pessoa import Pessoa

class Professor(Pessoa):
    
    def __init__(self):
        self.__Diretor = None
        self.__Coordenador = None
        self.__Curso = None
        self.__TipoEnsino = None
        self.__Escola = None
        super().__init__()

    def setDiretor(self, Diretor):
        self.__Diretor = Diretor

    def getDiretor(self):
        return self.__Diretor
    
    def setCoordenador(self, Coordenador):
        self.__Coordenador = Coordenador

    def getCoordenador(self):
        return self.__Coordenador
    
    def setCurso(self, Curso):
        self.__Curso = Curso

    def getCurso(self):
        return self.__Curso
    
    def setTipoEnsino(self, TipoEnsino):
        self.__TipoEnsino = TipoEnsino

    def getTipoEnsino(self):
        return self.__TipoEnsino
    
    def setEscola(self, Escola):
        self.__Escola = Escola

    def getEscola(self):
        return self.__Escola