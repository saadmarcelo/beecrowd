'''
Write a program that reads 6 numbers. These numbers will only be positive or negative (disregard null values). Print the total number of positive numbers.

Input

Six numbers, positive and/or negative.

Output

Print a message with the total number of positive numbers.
'''
'''
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())

lista = [num1, num2, num3, num4, num5, num6]
i = 0
count = 0
while i < len(lista):
    if lista[i]>0:
        count += 1
    i += 1
print("%d valores positivos" % count)
'''

cont=0
for _ in range(6):
    value = float(input())
    if value > 0 :
        cont+=1

print("%d valores positivos" % cont)