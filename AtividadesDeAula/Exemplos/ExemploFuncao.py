def velocidade(espaco, tempo):
    v = espaco / tempo
    print("Velocidade: {} m/s".format(format(v)))

velocidade(100,20)

print("====================================")

def dados(nome, idade=None):
    print("Nome:{}".format(nome))
    if idade is not None:
        print("Idade:{}".format(idade))
    else:
        print("Idade não informada")
dados("gabriel",28)

print("====================================")

def dadosRet(nome, idade=None):
    if idade is not None:
        return("Nome: {} \nIdade:{}".format(nome,idade))
    else:
        return("nome: {}\nIdade não informada".format(nome))
print(dadosRet("Gabriel",28))

print("====================================")

def teste(arg, *args):
    print("Argumento normal: {}".format(arg))
    for arg in args:
        print("Outro argumento: {}".format(arg))

teste("Python","é Melhor que", "Java")

print("====================================")

def funcao(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key,value))

dicionario = {"nome":"Gabriel", "idade":28}
funcao(**dicionario)