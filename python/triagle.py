A,B,C = map(float, input().split())

if abs(B - C) < A and A < (B + C):
    if abs(A - C) < B and B < (A + C):
        if abs(A - B) < C and C < (A + B):
            perimetro = (A + B + C)
            print("Perimetro = %.1f" % perimetro)
        else:
            Area = ((A + B)/2)* C
            print("Area = %.1f" % Area)
    else:
        Area = ((A + B)/2)* C
        print("Area = %.1f" % Area)
else:
    Area = ((A + B)/2)* C
    print("Area = %.1f" % Area)



