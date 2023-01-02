'''
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1. Print the read value and the list of banknotes.

Input

The input file contains an integer value N (0 < N < 1000000).

Output

Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.

Input Sample	Output Sample
576
                576
                5 nota(s) de R$ 100,00
                1 nota(s) de R$ 50,00
                1 nota(s) de R$ 20,00
                0 nota(s) de R$ 10,00
                1 nota(s) de R$ 5,00
                0 nota(s) de R$ 2,00
                1 nota(s) de R$ 1,00
11257
                11257
                112 nota(s) de R$ 100,00
                1 nota(s) de R$ 50,00
                0 nota(s) de R$ 20,00
                0 nota(s) de R$ 10,00
                1 nota(s) de R$ 5,00
                1 nota(s) de R$ 2,00
                0 nota(s) de R$ 1,00
503
                503
                5 nota(s) de R$ 100,00
                0 nota(s) de R$ 50,00
                0 nota(s) de R$ 20,00
                0 nota(s) de R$ 10,00
                0 nota(s) de R$ 5,00
                1 nota(s) de R$ 2,00
                1 nota(s) de R$ 1,00

'''

saque = int(input())
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

print(saque)
while saque >0:
    while saque >= 100:
        saque -= 100
        nota_100 += 1
    while saque >= 50:
        saque -= 50
        nota_50 += 1
    while saque >= 20:
        saque -= 20
        nota_20 += 1
    while saque >= 10:
        saque -= 10
        nota_10 += 1
    while saque >= 5:
        saque -= 5
        nota_5 += 1
    while saque >= 2:
        saque -= 2
        nota_2 += 1
    while saque >= 1:
        saque -= 1
        nota_1 += 1

print("%i nota(s) de R$ 100,00" % nota_100)
print("%i nota(s) de R$ 50,00" % nota_50)
print("%i nota(s) de R$ 20,00" % nota_20)
print("%i nota(s) de R$ 10,00" % nota_10)
print("%i nota(s) de R$ 5,00" % nota_5)
print("%i nota(s) de R$ 2,00" % nota_2)
print("%i nota(s) de R$ 1,00" % nota_1)