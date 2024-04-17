from Aluno import Aluno
from Sala import Sala

Disciplinas = []

class Diciplina():

    def __init__(self, nome, professor, sala, turno, duracao):
        self.nome = nome
        self.professor = professor
        self.alunos = []
        self.sala = sala
        self.turno = turno
        self.duracao = duracao

    def receberAlunos(self):
        Disciplinas.append(Aluno.getAluno(0))
        return True

    def definirSala(self):
        self.sala = Sala.Sala()
        Sala.receberDiciplinas([self.nome, self.turno, self.duracao])
        return True
