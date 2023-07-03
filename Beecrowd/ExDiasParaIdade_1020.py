n = int(input())
ano = n // 365
n = n - ano * 365
meses = n // 30
n = n - meses * 30
dias = n
print("{} ano(s)".format(ano))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))