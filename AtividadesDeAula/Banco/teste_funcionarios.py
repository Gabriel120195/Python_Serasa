from gerente import Gerente
from funcionario import Funcionario
from controle_bonificacao import Controle_bonificacao
from gerente import Gerente

gerente = Gerente("Gabriel", "00000000", 50000.00,"1234", 0)

funcionario = Funcionario("Laura", "11111111", 2000.00)

gerente = Gerente("Nil", "222333444-55", 25000.00)


print("Bonificação Gerente R$ {}".format(gerente.get_bonificacao()))
print("Bonificação Funcionario R$ {}".format(funcionario.get_bonificacao()))

controle = Controle_bonificacao()
controle.registro(funcionario)
controle.registro(gerente)

print("Total = {}".format(controle.total_bonificacao))
