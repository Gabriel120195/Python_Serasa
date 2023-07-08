num = input().split()
A = int(num[0])
B = int(num[1])
C = int(num[2])
D = int(num[3])
somaCeD = C + D
somaAeB = A + B
if(B > C and D > A and somaCeD > somaAeB and C > 0 and D > 0 and A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
