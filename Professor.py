Professores = []

class Professor():

    def __init__(self, nome):
        self.__nome = nome
        self.__idade = 0
        self.__sexo = ""
        self.__endereco = ""#class endereco
        self.__matricula = ""
        self.__disciplinas = ""
        self.__email = ""

    def ensinar(self):
        print()

    def getProfessor(self):
        return [self.__nome, self.__idade, self.__sexo, self.__endereco, self.__matricula, self.__disciplinas, self.__email]

    def setProfessor(self):
        self.__nome = input("Nome: ")
        self.__idade = int(input("Idade: "))
        self.__sexo = input("Sexo: ")
        self.__endereco = input("Endereco: ")
        self.__matricula = input("Matricula: ")
        self.__disciplinas = input("Disciplinas: ")
        self.__email = input("Email: ")