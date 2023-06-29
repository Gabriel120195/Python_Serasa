n = int(input())

horas = n // (60 * 60)
segundos = n % (60 * 60)

minutos = segundos // 60
segundos = segundos % 60
print("{:.0f}:{:.0f}:{:.0f}".format(horas,minutos,segundos))