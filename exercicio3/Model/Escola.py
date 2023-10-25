class Escola:


    def __init__(self):
        self.__Id = ""
        self.__nomeDiretor = ""
        self.__Professores = []
        self.__Cidade = ""
        self.__EscolaridadeDiretor = ""
        self.__Cursos = []
    
    def setId(self, Id):
        self.__Id = Id
    
    def getId(self):
        return self.__Id

    def setEscolaridadeDiretor(self, EscolaridadeDiretor):
        self.__EscolaridadeDiretor = EscolaridadeDiretor

    def getEscolaridadeDiretor(self):
        return self.__EscolaridadeDiretor
    
    def setNomeDiretor(self, nomeDiretor):
        self.__nomeDiretor = nomeDiretor

    def getNomeDiretor(self):
        return self.__nomeDiretor
    
    def setProfessor(self, Professor):
        self.__Professores = Professor

    def addProfessor(self, Professor):
        self.__Professores.append(Professor)

    def removeProfessor(self, Professor):
        self.__Professores.remove(Professor)
    
    def getProfessor(self):
        return self.__Professores
    
    def setCidade(self, Cidade):
        self.__Cidade = Cidade

    def getCidade(self):
        return self.__Cidade
    
    def setCurso(self, Curso):
        self.__Cursos = Curso

    def addCurso(self, Curso):
        self.__Cursos.append(Curso)

    def removeCurso(self, Curso):
        self.__Cursos.remove(Curso)
    
    def getCurso(self):
        return self.__Cursos