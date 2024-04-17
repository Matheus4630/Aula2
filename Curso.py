from Aluno import Aluno

Cursos = []

class Curso():

    def __init__(self, nome):
        self.nome = nome
        self.duração = 0
        self.tipo = ""
        self.turno = ""

    def aceitarAluno(self):
        Aluno.receberMatricula(Curso.emitirMatricula())

    def emitirMatricula(self):
        return "000001-0" #matricula que séria gerada de forma automatica
