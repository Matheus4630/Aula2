import aluno
import professor
import curso
import disciplina
import sala

alunos = []
professores = []
cursos = []
salas = []
disciplinas = []


#MENU

def listaMenu():
    print(f"{"=" * 15} MENU {"=" * 15}\n"
          " Selecione a área do sistema\n\n"
          " 1- Alunos \n"
          " 2- Professor \n"
          " 3- Cursos \n"
          " 4- Salas \n"
          " 5- Disciplinas \n"
          " 0- Sair \n"
          )


def menu(NONE=None):
    if NONE != None:
        return
    listaMenu()
    while True:
        try:
            opcao = int(input("O que deseja fazer? "))
        except ValueError:
            print("digite um numero inteiro valido")
            continue
        if 0 > opcao or opcao > 6:
            print("Opcao invalida")
            continue
        else:
            break
    match opcao:
        case 0:
            print("Até Mais!")
        case 1:
            aluno.Aluno(None).operacaoAlunos()
            menu()
        case 2:
            professor.Professor(None).operacaoProfessores()
            menu()
        case 3:
            curso.Curso(None).operacaoCursos()
            menu()
        case 4:
            sala.Sala(None, None, None).listaSalas()
            menu()
        case 5:
            disciplina.Diciplina(None, None, None, None).operacaoDisciplinas()
            menu()

#escolher 0(zero) da 1° vez antes de tentar utilizar e utilizar na 2° execução de menu
menu()
