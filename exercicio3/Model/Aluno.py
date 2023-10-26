from Model.Pessoa import Pessoa

class Aluno(Pessoa):
    
    def __init__(self):
        self.__estadoEstuda = None
        self.__coordenadorCurso = None
        self.__Curso = None
        super().__init__()
    
    def setEstadoEstuda(self, EstadoEstuda):
        self.__estadoEstuda = EstadoEstuda

    def getEstadoEstuda(self):
        return self.__estadoEstuda
    
    def setCoordenadorCurso(self, CoordenadorCurso):
        self.__coordenadorCurso = CoordenadorCurso

    def getCoordenadorCurso(self):
        return self.__coordenadorCurso
    
    def setCurso(self, Curso):
        self.__Curso = Curso

    def getCurso(self):
        return self.__Curso