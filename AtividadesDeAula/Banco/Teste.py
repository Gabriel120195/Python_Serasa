def criaConta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

print(criaConta("1234", "Gabriel silva", 1000.0, 10500.0))

conta1 = criaConta("1234", "Gabriel silva", 1000.0, 10500.0)
print(conta1['titular'])

def depositar(conta, valor):
    conta['saldo'] += valor
def sacar(conta, valor):
    conta['saldo'] -= valor