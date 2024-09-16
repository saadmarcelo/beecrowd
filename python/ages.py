'''
Write an algorithm to read an undeterminated number of data, each containing an individual's age. The final data, which will not enter in the calculations, contains the value of a negative age. Calculate and print the average age of this group of individuals.

Input

The input contains an undetermined number of integers. The input will be stop when a negative value is read.

Output

The output contains a value corresponding to the average age of individuals.

The average should be printed with two digits after the decimal point.

Input Sample	Output Sample
34
56
44
23
-2
                39.25
'''

idade=1
media = 0
lista=[]
soma= 0
while idade>=0:
    idade = int(input())
    if idade<0:
        for _ in range(len(lista)):
            soma= lista[_]+ soma
        media = soma/len(lista)
        print("%.2f"%media)
        break
    else:
        lista.append(idade)
