'''
Read 3 floating-point numbers. After, print the roots of bhaskara’s formula. If it's impossible to calculate the roots because a division by zero or a square root of a negative number, presents the message “Impossivel calcular”.

Input

Read 3 floating-point numbers (double) A, B and C.

Output

Print the result with 5 digits after the decimal point or the message if it is impossible to calculate.

Input Samples	Output Samples
10.0 20.1 5.1
                R1 = -0.29788
                R2 = -1.71212
0.0 20.0 5.0
                Impossivel calcular
10.3 203.0 5.0
                R1 = -0.02466
                R2 = -19.68408
10.0 3.0 5.0
                Impossivel calcular

'''

line_data = input()
data = line_data.split()
possivel = True

A = float(data[0])
B = float(data[1])
C = float(data[2])


delta = (B ** 2) - (4 * A * C)

x1 = (-B + (delta ** 0.5))
x2 = (-B - (delta ** 0.5))

if delta <= 0:
    possivel = False
    print("Impossivel calcular")
elif  x1 == 0 or x2 == 0:
    possivel = False
    print("Impossivel calcular")
else:
    R1 = (-B + (delta ** 0.5)) / (2 * A)
    R2 = (-B - (delta ** 0.5)) / (2 * A)

if possivel == True:
    print("R1 = %.5f" % R1)
    print("R2 = %.5f" % R2)

