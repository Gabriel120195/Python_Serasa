n = int(input())

for i in range(0,n):
    lista_notas = input().split()
    nota1 = float(lista_notas[0])
    nota2 = float(lista_notas[1])
    nota3 = float(lista_notas[2])
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

    print("{:.1f}".format(media))
