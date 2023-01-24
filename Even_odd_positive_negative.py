'''
Make a program that reads five integer values. Count how many   of these values are even, odd, positive and negative. Print these information like following example.

Input

The input will be 5 integer values.

Output

Print a message like the following example with all letters in lowercase, indicating how many of these values ​​are even, odd, positive and negative.

Input Sample	Output Sample
-5
0
-3
-4
12
                    3 valor(es) par(es)
                    2 valor(es) impar(es)
                    1 valor(es) positivo(s)
                    3 valor(es) negativo(s)
'''

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

lista = [num1, num2, num3, num4, num5]
i = 0
par = 0
imp = 0
pos = 0
neg = 0
while i < len(lista):
    if lista[i]>0:
        pos += 1
    elif lista[i]<0:
        neg += 1

    if lista[i]%2 ==0:
        par += 1
    else:
        imp += 1
    i += 1

print("%d valor(es) par(es)" % par)
print('%d valor(es) impar(es)' % imp)
print('%d valor(es) positivo(s)' % pos)
print('%d valor(es) negativo(s)' % neg)