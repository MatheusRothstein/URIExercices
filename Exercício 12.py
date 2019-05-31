valores = input().split(' ')
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

area_triangulo = (A*C)/2
print("TRIANGULO: %.3f" % area_triangulo)

area_circulo = 3.14159 * (C * C)
print("CIRCULO: %.3f" % area_circulo)

area_trapezio = ((A + B)/2) * C
print("TRAPEZIO: %.3f" % area_trapezio)

area_quadrado = B * B
print("QUADRADO: %.3f" % area_quadrado)

area_retangulo = A * B
print("RETANGULO: %.3f" % area_retangulo)