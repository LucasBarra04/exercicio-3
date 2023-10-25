

class TipoEnsino:
    def __init__(self):
        self.__TipoEnsino = ""
        self.__Cursos = []


    def setTipoEnsino(self,TipoEnsino):
        self.__TipoEnsino = TipoEnsino

    def getTipoEnsino(self):
        return self.__TipoEnsino
    
    def setCurso(self, Curso):
        self.__Cursos = Curso

    def addCurso(self, Curso):
        self.__Cursos.append(Curso)

    def removeCurso(self, Curso):
        self.__Cursos.remove(Curso)
    
    def getCurso(self):
        return self.__Cursos