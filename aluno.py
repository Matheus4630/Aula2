import endereco
import curso
import disciplina
import main


class Aluno():
    def __init__(self, nome):
        self.__nome = nome
        self.__idade = 0
        self.__sexo = ""
        self.__endereco = type(endereco.Endereco)
        self.__matricula = 0
        self.__curso = type(curso.Curso)
        self.__discilinas = []
        self.__email = ""

    def estudar(self):
        disciplinaTemp = disciplina.Diciplina.procurarDisciplina()
        self.__discilinas.append(disciplinaTemp)
        disciplina.Diciplina.receberAlunos(self.procurarAluno())

    def receberMatricula(self, matricula):
        self.__matricula = matricula


    def getAluno(self, num):
        if num == 0:
            return [self.__nome, self.__idade, self.__sexo, self.__matricula, self.__curso, self.__email]
        elif num == 1:
            return self.__nome
        elif num == 2:
            return self.__matricula
        else:
            return [self.__nome, self.__idade, self.__sexo, self.__endereco, self.__matricula, self.__curso, self.__discilinas, self.__email]

    def setAluno(self, list=None):
        if list == None:
            self.__nome = input("Nome: ")
            self.__idade = int(input("Idade: "))
            self.__sexo = input("Sexo: ")
            self.__endereco = endereco.Endereco.receberEndereco()
            self.__curso = curso.Curso.procurarCursos()
            self.__discilinas.append(disciplina.Diciplina.procurarDisciplina())
            self.__email = input("Email: ")
        else:
            self.__idade = list[0]
            self.__sexo = list[1]
            self.__endereco = endereco.Endereco(None, None, None, None, None, None).receberEndereco()
            self.receberMatricula(curso.Curso(None).emitirMatricula())
            self.__curso = curso.Curso(None).procurarCursos()
            self.__discilinas.append(disciplina.Diciplina(None, None, None, None).procurarDisciplina())
            self.__email = list[2]

    def cadastroAlunos(self):
        alunoTemp = []
        nome = str(input("Nome do novo aluno: "))
        newAluno = Aluno(nome)
        alunoTemp.append(str(input("Idade do novo aluno: ")))
        alunoTemp.append(str(input("Sexo do novo aluno: ")))
        alunoTemp.append(str(input("E-mail do novo aluno")))
        newAluno.setAluno(alunoTemp)

    def procurarAluno(self):
        self.listaAlunos()
        aluno = self.selecionarAluno()
        return aluno

    def selecionarAluno(self):
        index = -1 + int(input("qual o numero do Aluno que deseja selecionar? "))
        return main.alunos[index]

    def listaAlunos(self):
        count = 0
        print(f"{"-" * 10} Lista de Alunos {"-" * 10}")
        for alu in main.alunos:
            count += 1
            print(f"{count} - Nome: {alu.getAluno(1)}, Matricula: {alu.getAluno(2)}")


    def menuAlunos(self):
        print(f"{"*" * 10} Alunos {"*" * 10}\n"
              "1 - Novo Aluno\n"
              "2 - Editar Aluno\n"
              "3 - Sair do Aluno\n\n")

    def operacaoAlunos(self):
        while True:
            self.menuAlunos()
            opcao = input("Qual opção deseja fazer? ")
            if opcao == "1":
                self.cadastroAlunos()
            elif opcao == "2":
                alunoTemp = self.procurarAluno()
                alunoTemp.setAluno()
            elif opcao == "3":
                print("voltando ao menu inicial")
                break
            else:
                print("escolha uma opção válida")
