line_data = input()
data = line_data.split()

A = float(data[0])
B = float(data[1])
C = float(data[2])

pi = 3.14159

TRIANGULO = (A*C)/2
CIRCULO = pi * (C**2)
TRAPEZIO = ((A+B)/2)*C
QUADRADO = (B**2)
RETANGULO = (A*B)

print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)
