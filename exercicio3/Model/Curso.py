class Curso:
    def __init__(self):
       self.__Id = ""
       self.__nomeCoordenador = ""
       self.__Escola = ""
       self.__Professores = []
       self.__escolaridadeCoordenador = ""
       self.__TipoEnsino = ""
       self.__Alunos = []

    def setId(self, Id):
        self.__Id = Id

    def getId(self):
        return self.__Id

    def setNomeCoordenador(self, nomeCoordenador):
        self.__nomeCoordenador = nomeCoordenador

    def getNomeCoordenador(self):
        return self.__nomeCoordenador
    
    def setProfessor(self, Professor):
        self.__Professores = Professor

    def addProfessor(self, Professor):
        self.__Professores.append(Professor)

    def removeProfessor(self, Professor):
        self.__Professores.remove(Professor)
    
    def getProfessor(self):
        return self.__Professores
    
    def setEscolaridadeCoordenador(self, escolaridadedoCoordenador):
        self.__escolaridadeCoordenador =  escolaridadedoCoordenador

    def getEscolaridadeCoordenador(self):
        return self.__escolaridadeCoordenador
       
    def setEscola(self, Escola):
        self.__Escola = Escola

    def getEscola(self):
        return self.__Escola
    
    def setTipoEnsino(self,TipoEnsino):
        self.__TipoEnsino = TipoEnsino

    def getTipoEnsino(self):
        return self.__TipoEnsino
    
    def setAlunos(self, Aluno):
        self.__Alunos = Aluno

    def addAluno(self, Aluno):
        self.__Alunos.append(Aluno)

    def removeAluno(self, Aluno):
        self.__Alunos.remove(Aluno)

    def getAluno(self):
        return self.__Alunos