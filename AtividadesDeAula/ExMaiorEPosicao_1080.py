lista_valores = []

for i in range(1,101):
    valor = int(input())
    lista_valores.append(valor)

maior = max(lista_valores)
indice = lista_valores.index(maior) + 1
print(maior)
print(indice)

