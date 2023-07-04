class Pessoa:
    __slots__ = ['_idade']
    _total_de_pessoas = 0

    def __init__(self,idade):
        self.idade = idade
        Pessoa._total_de_pessoas += 1


    #privado
    # def __init__(self,idade):
    #     self.__idade = idade

    #protegido
    # def __init__(self,idade):
    #     self._idade = idade

    # def get_idade(self):
    #     return self._idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self,idade):
        self._idade = idade

    @staticmethod
    def get_total_de_pessoas():
        return Pessoa._total_de_pessoas


pessoa = Pessoa(30)
pessoa2 = Pessoa(17)

print(pessoa._total_de_pessoas)
# print("private = ", pessoa._Pessoa__idade)
print("protegido = ", pessoa.get_idade())