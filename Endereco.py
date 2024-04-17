Enderecos = []

class Endereco():

    def __init__(self, estado, cidade, bairro, rua, numero, complemento):
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento

    def getEndereco(self):
        return [self.__estado, self.__cidade, self.__cidade, self.__bairro, self.__rua, self.__numero, self.__complemento]

    def setEndereco(self, estado, cidade, bairro, rua, numero, complemento):
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento
        return True

