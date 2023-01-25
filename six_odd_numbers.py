'''
Read an integer value X and print the 6 consecutive odd numbers from X, a value per line, including X if it is the case.

Input

The input will be a positive integer value.

Output

The output will be a sequence of six odd numbers.

Input Sample	Output Sample
8
                    9
                    11
                    13
                    15
                    17
                    19

'''

n = int(input())
soma = 0
contador = 6
lista = []
while contador>0:
    if n %2 !=0:
        contador -= 1
        print(n)
        lista.append(n)
    n += 1

print(lista)