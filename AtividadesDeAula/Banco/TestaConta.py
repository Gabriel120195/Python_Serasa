from Conta import Conta
from Cliente import Cliente

Cliente = Cliente("Carlos", "Silva", "11122233345")
Conta = Conta('233', Cliente, 2500, 250000)

Conta.depositar(250.00)
Conta.extrato()
Conta.sacar(100)
Conta.extrato()
Conta.transferir(Conta,75.00)
Conta.extrato()
Conta.Historico.imprime()