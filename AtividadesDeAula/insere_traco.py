def DashInsert(string):
    nova_string = ''
    ultimo_digito = string[len(string-1)]
    for i in range(0, len(string)-1):
        digito = int(string[i])
        proximo_digito = int(string[i + 1])

        if digito % 2 != 0 and proximo_digito % 2 != 0:
            nova_string = nova_string + str(digito) + '-'
        else:
            nova_string = nova_string + str(digito)
        return  nova_string  + ultimo_digito
print(DashInsert("11335547854"))