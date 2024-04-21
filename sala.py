import main

class Sala():
    def __init__(self, bloco, numero, tipo):
        self.bloco = bloco
        self.numero = numero
        self.tipo = tipo
        self.disciplinaSala = []

    def receberDiciplinas(self, disciplina):
        self.disciplinaSala.append(disciplina)
        return True

    def listaSalas(self):
        count = 0
        for sala in main.salas:
            print(f"{count + 1} - {sala}")
            count += 1

    def novaSala(self):
        salaTemp = Sala(input("Bloco: "), input("Numero: "), input("Tipo: "))
        main.salas.append(salaTemp)
        return salaTemp

    def procurarSala(self):
        self.listaSalas()
        sala = self.selecionaSala()
        return sala

    def selecionaSala(self):
        index = -1 + int(input("qual o numero da sala que deseja selecionar? "))
        return main.salas[index]

    def listaSalas(self):
        count = 0
        print(f"{"-" * 10} Salas {"-" * 10}")
        for sal in main.salas:
            count += 1
            print(f"{count} - {sal.nome}")