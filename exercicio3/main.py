from Model.Pessoa import Pessoa
from Model.Aluno import Aluno
from Model.Professor import Professor
from Model.Curso import Curso
from Model.Escola import Escola
from Model.Tipoensino import TipoEnsino
from Model.Escolaridade import Escolaridade
from Model.Cidade import Cidade
from Model.Estado import Estado

if __name__ == "__main__":

        #Instanciação

        estado1 = Estado()
        cidade1 = Cidade()
        escolaridade1 = Escolaridade()
        tipoensino1 = TipoEnsino()
        escola1 = Escola()
        curso1 = Curso()
        professor1 = Professor()
        aluno1 = Aluno()
        estado2 = Estado()
        cidade2 = Cidade()



        estado1.setSiglaEstado('RJ')
        
        cidade1.setEstado(estado1.getSiglaEstado())
        cidade1.setNomeCidade('Resende')
        
        estado1.setCidade(cidade1.getNomeCidade())
        
        escola1.setCidade(cidade1.getNomeCidade())
        escola1.setId('09547')
        escola1.setNomeDiretor('José')
        escola1.setEscolaridadeDiretor('Ensino Superior')

        cidade1.setEscola(escola1.getId())
        
        professor1.setNome('Arnaldo')

        escola1.setProfessor(professor1.getNome())
        curso1.setProfessor(professor1.getNome())
        curso1.setEscolaridadeCoordenador('Superior')

        professor1.setEscola(escola1.getId())
        professor1.setCidade(cidade1.getNomeCidade())
        professor1.setDiretor(escola1.getNomeDiretor())
        professor1.setEstadoNaturalidade(estado1.getSiglaEstado())
        
        curso1.setId('402')
        curso1.setNomeCoordenador('Claudinei')
        
        professor1.setCoordenador(curso1.getNomeCoordenador())
        
        curso1.setEscola(escola1.getId())
        
        tipoensino1.setCurso(curso1.getId())
        tipoensino1.setTipoEnsino("Superior")
        
        curso1.setTipoEnsino(tipoensino1.getTipoEnsino())
        professor1.setTipoEnsino(curso1.getTipoEnsino())
        
        escola1.setCurso(curso1.getId())
        
        professor1.setCurso(curso1.getId())
        professor1.setEscolaridade('Superior')
        
        aluno1.setNome('Zlatan')
        aluno1.setEscolaridade('Médio')
        aluno1.setEstadoEstuda(estado1.getSiglaEstado())
        aluno1.setCoordenadorCurso(curso1.getNomeCoordenador())
        aluno1.setCurso(curso1.getId())

        curso1.setAlunos(aluno1.getNome())

        estado2.setSiglaEstado('PR')

        cidade2.setNomeCidade('Curitiba')
        cidade2.setEstado(estado2.getSiglaEstado())

        estado2.setCidade(cidade2.getNomeCidade())

        aluno1.setCidade(cidade2.getNomeCidade()) 
        aluno1.setEstadoNaturalidade(estado2.getSiglaEstado())

        print("---------------------------------------------------")
        print('ALUNO 1')
        print()
        print(f"Nome:", aluno1.getNome())
        print(f"Escolaridade:", aluno1.getEscolaridade())
        print(f"Estado de Naturalidade:", aluno1.getEstadoNaturalidade())
        print(f"Cidade:", aluno1.getCidade())
        print(f"Estado onde Estuda:", aluno1.getEstadoEstuda())
        print(f"Coordenador do Curso:", aluno1.getCoordenadorCurso())
        print(f"Curso:", aluno1.getCurso())
        print()
        
        print("---------------------------------------------------")
        print('PROFESSOR 1')
        print()
        print("Nome:", professor1.getNome())
        print("Escolaridade:", professor1.getEscolaridade())
        print("Estadoo de Naturalidade:", professor1.getEstadoNaturalidade())
        print("Cidade:", professor1.getCidade())
        print("Diretor:", professor1.getDiretor())
        print("Coordenador:", professor1.getCoordenador())
        print("Curso:", professor1.getCurso())
        print("Tipo Ensino:", professor1.getTipoEnsino())
        print("Escola:", professor1.getEscola())
        print()

        print("---------------------------------------------------")
        print('ESCOLA')
        print()
        print("Id:", escola1.getId())
        print("Nome do Diretor:", escola1.getNomeDiretor())
        print("Professor:", escola1.getProfessor())
        print("Cidade:", escola1.getCidade())
        print("Escolaridade do Diretor:", escola1.getEscolaridadeDiretor())
        print("Cursos:", escola1.getCurso())
        print()

        print("---------------------------------------------------")
        print('CURSO')
        print()
        print("Id:", curso1.getId())
        print("Nome do Coordenador:", curso1.getNomeCoordenador())
        print("Escola:", curso1.getEscola())
        print("Professor:", curso1.getProfessor())
        print("Escolaridade do Coordenador:", curso1.getEscolaridadeCoordenador())
        print("Tipo Ensino:", curso1.getTipoEnsino())
        print("Aluno:", curso1.getAluno())
        print()

        print("---------------------------------------------------")
        print('TIPO ENSINO')
        print()
        print("Tipo de Ensino:", tipoensino1.getTipoEnsino())
        print("Cursos:", tipoensino1.getCurso())
        print()

        print("---------------------------------------------------")
        print('CIDADE')
        print()
        print("Nome da Cidade:", cidade1.getNomeCidade())
        print("Estado:", cidade1.getEstado())
        print("Escolas:", cidade1.getEscola())
        print()

        print("---------------------------------------------------")
        print('ESTADO')
        print()
        print("Sigla do Estado:", estado1.getSiglaEstado())
        print("Cidades:", estado1.getCidade())
        print()

        print("---------------------------------------------------")