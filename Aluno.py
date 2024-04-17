Alunos = []

class Aluno():
    def __init__(self, nome):
        self.__nome = nome
        self.__idade = 0
        self.__sexo = ""
        self.__endereco = ""#class: Endereço
        self.__matricula = ""
        self.__curso = ""
        self.__discilinas = []
        self.__email = ""

    def estudar(self, diciplina):
        self.__discilinas.append(diciplina)

    def receberMatricula(self, matricula):
        self.__matricula = matricula


    def getAluno(self):
        return [self.__nome, self.__idade, self.__sexo, self.__endereco, self.__matricula, self.__curso, self.__discilinas, self.__email]

    def setAluno(self):
        self.__nome = input("Nome: ")
        self.__idade = int(input("Idade: "))
        self.__sexo = input("Sexo: ")
        self.__endereco = input("Endereco: ")
        self.__matricula = input("Matricula: ")
        self.__curso = input("Curso: ")
        self.__discilinas = input("Discilinas: ")
        self.__email = input("Email: ")