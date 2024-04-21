import endereco
import main
import disciplina
import curso

class Professor():

    def __init__(self, nome):
        self.__nome = nome
        self.__idade = 0
        self.__sexo = ""
        self.__endereco = type(endereco.Endereco)
        self.__matricula = 0
        self.__disciplinas = []
        self.__email = ""


    def getProfessor(self):
        return [self.__nome, self.__idade, self.__sexo, self.__endereco, self.__matricula, self.__disciplinas, self.__email]

    def setProfessor(self, nome=None):
        if nome == None:
            self.__nome = input("Nome: ")
        else:
            self.__nome = nome
        self.__idade = int(input("Idade: "))
        self.__sexo = input("Sexo: ")
        self.__endereco = endereco.Endereco.receberEndereco()
        if self.__matricula == 0:
            self.__matricula = curso.Curso.emitirMatricula()
        self.__disciplinas.append(disciplina.Diciplina.procurarDisciplina())
        self.__email = input("Email: ")

    def novoProfessor(self, nome):
        newProfessor = Professor(nome)
        newProfessor.setProfessor(nome)
        main.professores.append(newProfessor)

    def selecionarProfessor(self):
        self.listarProfessores()
        opcao = int(input("Qual professor deseja selecionar? "))
        professorTemp = main.professores[opcao - 1]
        return professorTemp

    def listarProfessores(self):
        count = 0
        for prof in main.professores:
            count += 1
            print(f"{count} - {prof.getProfessor()}")

    def menuProfessores(self):
        print(f"{"_" * 10} Professor Menu {"_" * 10}"
              "\n1 - Novo Professor\n"
              "2 - Editar Professor\n"
              "3 - Sair do Professor\n")

    def operacaoProfessores(self):
        while True:
            self.menuProfessores()

            opcao = int(input("Escolha uma opcao: "))
            if opcao == 1:
                self.novoProfessor(input("Nome: "))
            elif opcao == 2:
                editar = self.selecionarProfessor()
                print("informe as novas informações do professor")
                editar.setProfessor()
            elif opcao == 3:
                print("voltando ao Menu Principal")
                break
            else:
                print("escolha uma opcao invalida")

