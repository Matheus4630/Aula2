import random
import main
matriculas = []


#Manipulação Classe
class Curso():

    def __init__(self, nome):
        self.nome = nome
        self.duracao = 0
        self.tipo = ""
        self.turno = ""


    def emitirMatricula(self):
        matriculaTemp = None
        while not self.verificarMatricula(matriculaTemp):
            matriculaTemp = int(random.randint(100000000, 999999999))
        matriculas.append(matriculaTemp)
        return matriculaTemp #matricula que séria gerada de forma automatica

    def verificarMatricula(self, matricula, modo=None):
        if modo:
            for aluno in main.alunos:
                if aluno.getAluno(2) == matricula:
                    return aluno
        if matricula == None:
            return False
        elif type(matricula) == int:
            for m in matriculas:
                if m == matricula:
                    return False
            return True
        return False


    #Manipulação do banco de cursos
    def novosCursos(self):
        nome = str(input("Nome do Novo Curso: "))
        cursoTemp = Curso(nome)
        cursoTemp.duracao = int(input("quantos periodos há no Novo Curso: "))
        cursoTemp.tipo = str(input("qual o tipo do Novo Curso: "))
        cursoTemp.turno = str(input("Turno do Novo Curso: "))
        main.cursos.append(cursoTemp)


    def procurarCursos(self):
        self.listaCursos()
        curso = self.selecionarCurso()
        return curso

    def selecionarCurso(self):
        index = -1 + int(input("qual o numero do curso que deseja selecionar? "))
        return main.cursos[index]

    def listaCursos(self):
        count = 0
        print(f"{"-" * 10} Cursos Disponiveis {"-" * 10}")
        for curso in main.cursos:
            count += 1
            print(f"{count} - Curso: {curso.nome}")

    def menuCurso(self):
        print(f"{"~" * 15} Cursos {"~" * 15}"
              f"\n1 - Novo Curso\n"
              f"2 - Ver Cursos\n"
              f"3 - Sair")

    def operacaoCursos(self):
        while True:
            self.menuCurso()

            opcao = int(input("Escolha uma opcao: "))
            if opcao == 1:
                self.novosCursos()
            elif opcao == 2:
                ver = self.listaCursos()
            elif opcao == 3:
                print("voltando ao Menu Principal")
                break
            else:
                print("escolha uma opcao invalida")