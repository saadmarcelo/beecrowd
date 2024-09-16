'''
Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order, so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make, based on the following cases always writing an appropriate message:

if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
Input

The input contains three double numbers, A (0 < A) , B (0 < B) and C (0 < C).

Output

Print all the classifications of the triangle presented in the input.

Input Samples	Output Samples
7.0 5.0 7.0
                TRIANGULO ACUTANGULO
                TRIANGULO ISOSCELES
6.0 6.0 10.0
                TRIANGULO OBTUSANGULO
                TRIANGULO ISOSCELES
6.0 6.0 6.0
                TRIANGULO ACUTANGULO
                TRIANGULO EQUILATERO
5.0 7.0 2.0
                NAO FORMA TRIANGULO
6.0 8.0 10.0
                TRIANGULO RETANGULO
'''
valores = input().split()
valores = list(map(float,valores))

A,B,C = sorted(valores, reverse=True)

continua = True

if(A >= B+C):
    print("NAO FORMA TRIANGULO")
    continua = False

if(A**2 == (B**2) + (C**2) and continua):
    print("TRIANGULO RETANGULO")

if(A**2 > (B**2) + (C**2) and continua):
    print("TRIANGULO OBTUSANGULO")

if(A**2 < (B**2) + (C**2) and continua):
    print("TRIANGULO ACUTANGULO")

if(A == B and B == C and continua):
    print("TRIANGULO EQUILATERO")

if((A == B or B == C) and not (A == B and B == C) and continua):
    print("TRIANGULO ISOSCELES")