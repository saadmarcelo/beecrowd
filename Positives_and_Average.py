'''
Read 6 values that can be floating point numbers. After, print how many of them were positive. In the next line, print the average of all positive values typed, with one digit after the decimal point.

Input

The input consist in 6 numbers that can be integer or floating point values. At least one number will be positive.

Output

The first output value is the amount of positive numbers. The next line should show the average of the positive values ​typed.

Input Sample	Output Sample
7
-5
6
-3.4
4.6
12
                4 valores positivos
                7.4
'''
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())

lista = [num1, num2, num3, num4, num5, num6]
lista1 = []
i = 0
count = 0
while i < len(lista):
    if lista[i]>0:
        count += 1
        lista1.append(lista[i])
    i += 1

media = 0
k = 0
while k < len(lista1):
    media = media + lista1[k]
    k += 1

media = media / len(lista1)
print("%d valores positivos" % count)
print("%.1f" % media)