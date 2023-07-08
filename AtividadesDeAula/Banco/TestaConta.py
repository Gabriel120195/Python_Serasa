from conta import Conta
from Cliente import Cliente

# ==== Clientes ====
Cliente1 = Cliente("Carlos", "Santos", "111222333-45")
Cliente2 = Cliente("Laura", "Pina", "123345678-25")
Cliente3 = Cliente("Gabriel", "Silva", "999888777-66")

# ==== Contas ====
conta1 = Conta('111', Cliente1, 2500, 250000)
conta2 = Conta('222',Cliente2, 4000,400000)
conta3 = Conta('333',Cliente3, 6500,650000)

# ==== Depositos ====
conta1.depositar(250)
conta2.depositar(430)
conta3.depositar(1000)

# ==== Saques ====
conta1.sacar(300)
conta2.sacar(100)
conta3.sacar(2000)

# ==== Transferencias ====
conta1.transferir(conta3, 870)
conta3.transferir(conta2, 1000)
conta2.transferir(conta1, 500)

# print("===== Extratos =====")
# print("=== Conta1 ===")
# print(conta1.extrato())
# print("===============")
# print("=== Conta2 ===")
# print(conta2.extrato())
# print("===============")
# print("=== Conta3 ===")
# print(conta3.extrato())
# print("===============")
print(conta1.historico.transacoes)

