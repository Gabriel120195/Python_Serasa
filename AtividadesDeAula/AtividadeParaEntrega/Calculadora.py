
def soma(num1, num2):
    soma = num1 + num2
    return soma
def subtracao(num1, num2):
    sub = num1 - num2
    return sub

def multiplicacao(num1, num2):
    multi = num1 * num2
    return multi

def divisao(num1, num2):
    if(num2 != 0):
        divi = num1 / num2
        return divi
    else:
        return False

def calculadora():
    num1 = float(input("Digite o primeiro número:\n"))
    num2 = float(input("Digite o segundo número:\n"))
    operador = input("Digite a operação desejada\n1=(SOMA) / 2=(SUBTRAÇÃO) / 3=(MULTIPLICAÇÃO) / 4=(DIVISÃO): ")

    if(operador == "1"):
        print("{} + {} = {}".format(num1,num2,soma(num1,num2)))
    elif(operador == "2"):
        print("{} - {} = {}".format(num1, num2, subtracao(num1, num2)))
    elif (operador == "3"):
        print("{} x {} = {}".format(num1, num2, multiplicacao(num1, num2)))
    elif (operador == "4"):
        if(divisao(num1,num2) != False):
            print("{} / {} = {}".format(num1, num2, divisao(num1, num2)))
        else:
            print("Não é possivel dividir por zero")
    else:
        print("Operação inválida!")

    repetir()

def repetir():
    repetir = input("Deseja realizar outra operação?\n 1=SIM / 2=ENCERRAR: ")
    if repetir == "1":
        calculadora()
    else:
        print("Encerrado")

calculadora()