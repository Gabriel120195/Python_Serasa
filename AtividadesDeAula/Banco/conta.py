from Cliente import Cliente
from historico import Historico
class Conta:
    _total_de_contas = 1
    def __init__(self, numero, cliente, saldo, limite):
        print("Incializando conta!")
        self._numero = numero
        self._titular = cliente.nome
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()

        Conta._total_de_contas += 1

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
    @property
    def historico(self):
        return self._historico

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @staticmethod
    def get_total_de_contas():
        return Conta._total_de_contas

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de {} reais".format(valor))

    def sacar(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de {} reais".format(valor))
            return True

    def extrato(self):
        print("Numero:{} \nTitular:{}\nSaldo:{}\nLimite:{}".format(self.numero, self.titular, self.saldo, self.limite))
        self.historico.transacoes.append("Tirou o extrato - Saldo de {} reais".format(self.saldo))
    def transferir(self, destino, valor):
        retirada = self.sacar(valor)
        if (retirada == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Transferencia de {} reais para a conta {}".format(valor,destino.numero))
            return True