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
        
        estado1.addCidade(cidade1.getNomeCidade())
        
        escola1.setCidade(cidade1.getNomeCidade())
        escola1.setId('09547')
        escola1.setNomeDiretor('José')
        escola1.setEscolaridadeDiretor('Ensino Superior')
        
        professor1.setNome('Arnaldo')
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
        
        escola1.setCurso(curso1.getId())
        
        professor1.setCurso(curso1.getId())
        professor1.setEscolaridade('Superior')
        
        aluno1.setNome('Zlatan')
        aluno1.setEscolaridade('Médio')
        aluno1.setEstadoEstuda(estado1.getSiglaEstado())
        aluno1.setCoordenadorCurso(curso1.getNomeCoordenador())
        aluno1.setCurso(curso1.getId())

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

        