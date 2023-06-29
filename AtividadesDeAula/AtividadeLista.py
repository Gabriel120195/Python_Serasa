lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

#iniciando as variaveis
maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
ocorrenciaItem1 = 0
mediaValores = 0
somaNegativos = 0

#iniciando nosso loop
for i in range(0,len(lista)):

    #maioValor
    if maiorValor < lista[i]:
        maiorValor = lista[i]

    #menorValor
    if menorValor > lista[i]:
        menorValor = lista[i]

    #numerosPares
    if lista[i] % 2 == 0:
        listaPares.append(lista[i])

    #numeroOcorrencias
    if lista[i] == lista[0]:
        ocorrenciaItem1 += 1

    #somaNegativos
    if lista[i] < 0:
        somaNegativos = somaNegativos + lista[i]

    #mediaValores
    mediaValores = mediaValores + lista[i]

mediaValores = mediaValores / len(lista)

print("MAIOR VALOR = ", maiorValor)
print("MENOR VALOR = ", menorValor)
print("NUMEROS PARES = ", listaPares)
print("OCORRENCIAS = ", ocorrenciaItem1)
print("SOMA NEGATIVOS = ", somaNegativos)
print("MEDIA VALORES = ", mediaValores)