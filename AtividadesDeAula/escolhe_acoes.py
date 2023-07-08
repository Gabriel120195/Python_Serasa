def StockPicker(arr):
    lucro_maximo = 0
    valor_minimo = arr[0]

    for i in range(0, len(arr)):
        valor_minimo = min(valor_minimo, arr[i])
        lucro = arr[i] - valor_minimo
        lucro_maximo = max(lucro_maximo, lucro)
    if lucro_maximo > 0:
        return lucro_maximo
    else:
        return -1

print(StockPicker([10,9,8,2]))