num = input().split()
A = float(num[0])
B = float(num[1])
C = float(num[2])
delta = (B ** 2) - 4 * A * C
if(A == 0 and 0 > delta):
    print("Impossivel calcular")
else:
    x1 = (-B + delta ** (1 / 2)) / (2 * A)
    x2 = (-B - delta ** (1 / 2)) / (2 * A)
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))

#ou
v = input().split()
a, b, c = v

a = float(a)
b = float(b)
c = float(c)

if a == 0.0  or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))

