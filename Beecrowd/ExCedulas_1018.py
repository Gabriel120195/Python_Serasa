N = int(input())
valor = N
cedulas = [100, 50, 20, 10, 5, 2, 1]
cont = 0
print(valor)
for i in range(len(cedulas)):
    cont = N // cedulas[i]
    N %= cedulas[i]
    print('{} nota(s) de R$ {},00'.format(cont, cedulas[i]))

