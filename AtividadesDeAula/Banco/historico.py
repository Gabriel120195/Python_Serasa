import datetime
class Historico:
    def __init__(self):
        self.dataAbertura = datetime.date.today()
        self.transacoes = []

    def imprime(self):
        print("Data de abertura: {}".format(self.dataAbertura))
        print("Transações: ")
        for i in self.transacoes:
            print('-', i)