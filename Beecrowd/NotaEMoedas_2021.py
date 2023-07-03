valor = float(input())
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for ced in cedulas:
    quantidadeNotas = int(valor / ced)
    print('{} nota(s) de R$ {},00'.format(quantidadeNotas, ced))
    valor -= quantidadeNotas * ced
print("MOEDAS:")
for moe in moedas:
    quantidadeMoedas = int(round(valor,2) / moe)
    print('{} moeda(s) de R$ {:.2f}'.format(quantidadeMoedas, moe))
    valor -= quantidadeMoedas * moe
