def PowerofTwo(num):
    if num == 0:
        return "False"
    while num != 1:
        if num % 2 != 0:
            return "False"
        else:
            num = num // 2
    return "True"

print(PowerofTwo(8))