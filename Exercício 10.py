peça_1 = input().split(' ')
a = int(peça_1[0])
b = int(peça_1[1])
c = float(peça_1[2])

peça_2 = input().split(' ')
x = int(peça_2[0])
y = int(peça_2[1])
z = float(peça_2[2])

valor_peça1 = b * c
valor_peça2 = y * z

valor_total = valor_peça1 + valor_peça2

print("VALOR A PAGAR: R$ %.2f" % valor_total)