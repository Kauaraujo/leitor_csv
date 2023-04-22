class Pessoa:

    contador = 0

    def __init__(self, nome, sexo, idade, altura):
        self.__numero = Pessoa.contador + 1
        self.__nome = nome
        self.__sexo = sexo
        self.__idade = idade
        self.__altura = altura
        Pessoa.contador = self.__numero

    
    @property
    def numero(self: object) -> int:
        return self.__numero
    
    @property
    def nome(self: object) -> str:
        return self.__nome
    
    @property
    def sexo(self: object) -> str:
        return self.__sexo
    
    @property
    def idade(self: object) -> int:
        return self.__idade
    
    @property
    def altura(self: object) -> int:
        return self.__altura
    
    def __str__(self: object) -> str:
        return f'Id: {self.numero}\nNome: {self.nome} \nSexo: {self.sexo} \nIdade: {self.idade} ' \
               f'\nAltura(cm): {self.altura}'
