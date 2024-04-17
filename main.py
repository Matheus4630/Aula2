
#MENU

def menu():
    listaMenu()
    while True:
        try:
            opcao = int(input("O que deseja fazer?"))
        except TypeError:
            print("digite um numero inteiro valido")
            continue
        if 0 > opcao > 6:
            print("Opcao invalida")
            continue
        else:
            break
    match opcao:
        case 0:
            print("Até Mais!")
            return
        case 1:
            ""
        case 2:
            ""
        case 3:
            ""
        case 4:
            ""
        case 5:
            ""
        case 6:
            ""



def listaMenu():
    print(f"{"=" * 15} MENU {"=" * 15}\n"
          " Selecione a área do sistema\n\n"
          " 1- Alunos \n"
          " 2- Professor \n"
          " 3- Cursos \n"
          " 4- Endereços \n"
          " 5- Salas \n"
          " 6- Disciplinas \n"
          " 0- Sair \n"
          )


def controleBancoDeDados():
    ""


menu()
