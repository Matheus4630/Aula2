import sala
import main

class Diciplina():

    def __init__(self, nome, professor, turno, duracao):
        self.nome = nome
        self.professor = professor
        self.alunos = []
        self.turno = turno
        self.duracao = duracao

    def receberAlunos(self, Aluno):
        self.alunos.append(Aluno.getAluno(0))


    def definirSala(self):
        sala.Sala.receberDiciplinas([self.nome, self.professor, self.turno, self.duracao])
        return True

    def novaDisciplina(self, nome, professor, turno, duracao):
        disciplinaTemp = Diciplina(nome, professor, turno, duracao)
        main.disciplinas.append(disciplinaTemp)
        return disciplinaTemp

    def procurarDisciplina(self):
        self.listaDisciplinas()
        disciplina = self.selecionaDisciplina()
        return disciplina

    def selecionaDisciplina(self):
        index = -1 + int(input("qual o numero do curso que deseja selecionar? "))
        return main.disciplinas[index]

    def listaDisciplinas(self):
        count = 0
        print(f"{"-" * 10} Disciplinas Disponivéis {"-" * 10}")
        for dis in main.disciplinas:
            count += 1
            print(f"{count} - {dis.nome}")

    def menuDisciplina(self):
        print(f"{"=" * 10} Disciplinas {"=" * 10}\n"
              "1 - Nova Disciplinas\n"
              "2 - Lista Disciplinas\n"
              "3 - Sair\n")

    def operacaoDisciplinas(self):
        while True:
            self.menuDisciplina()
            opcao = input("Qual opção deseja fazer? ")
            if opcao == "1":
                self.novaDisciplina(input("nome"), input("professor"), input("turno"), input("duracao"))
            elif opcao == "2":
                disciplinaTemp = self.procurarDisciplina()
                disciplinaTemp.setAluno()
            elif opcao == "3":
                print("voltando ao menu inicial")
                break
            else:
                print("escolha uma opção válida")
