from Cliente import Cliente
from Historico import Historico
class Conta:
    def __init__(self, numero, Cliente, saldo, limite):
        self.numero = numero
        self.titular = Cliente.nome
        self.saldo = saldo
        self.limite = limite
        self.Historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.Historico.transacoes.append("Depósito de {} reais".format(valor))

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.Historico.transacoes.append("Saque de {} reais".format(valor))
            return True

    def extrato(self):
        print("Numero:{} \nTitular:{}\nSaldo:{}\nLimite:{}".format(self.numero, self.titular, self.saldo, self.limite))
        self.Historico.transacoes.append("Tirou o extrato - Saldo de {} reais".format(self.saldo))
    def transferir(self, destino, valor):
        retirada = self.sacar(valor)
        if (retirada == False):
            return False
        else:
            destino.depositar(valor)
            self.Historico.transacoes.append("Transferencia de {} reais para a conta {}".format(valor,destino.numero))
            return True