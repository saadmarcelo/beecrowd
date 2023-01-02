''' Read a value of floating point with two decimal places. This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.

Input

The input file contains a value of floating point N (0 ≤ N ≤ 576.73

Output

Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.

Input Sample	Output Sample
576.73
                                    NOTAS:
                                    5 nota(s) de R$ 100.00
                                    1 nota(s) de R$ 50.00
                                    1 nota(s) de R$ 20.00
                                    0 nota(s) de R$ 10.00
                                    1 nota(s) de R$ 5.00
                                    0 nota(s) de R$ 2.00
                                    MOEDAS:
                                    1 moeda(s) de R$ 1.00
                                    1 moeda(s) de R$ 0.50
                                    0 moeda(s) de R$ 0.25
                                    2 moeda(s) de R$ 0.10
                                    0 moeda(s) de R$ 0.05
                                    3 moeda(s) de R$ 0.01
'''

from decimal import *

saque = Decimal(input())


saque = Decimal(saque) * Decimal(100)



nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
moeda_1 = 0
moeda_05 = 0
moeda_025 = 0
moeda_010 = 0
moeda_005 = 0
moeda_001 = 0

while saque >= 10000:
    nota_100 += 1
    saque -= 10000
while saque >= 5000:
    nota_50 += 1
    saque -= 5000
while saque >= 2000:
    nota_20 += 1
    saque -= 2000
while saque >= 1000:
    nota_10 += 1
    saque -= 1000
while saque >= 500:
    nota_5 += 1
    saque -= 500
while saque >= 200:
    nota_2 += 1
    saque -= 200
while saque >= 100:
    moeda_1 += 1
    saque -= 100
while saque >= 50:
    moeda_05 += 1
    saque -= 50
while saque >= 25:
    moeda_025 += 1
    saque -= 25
while saque >= 10:
    moeda_010 += 1
    saque -= 10
while saque >= 5:
    moeda_005 += 1
    saque -= 5
while saque >= 1:
    moeda_001 += 1
    saque -= 1


print("NOTAS:")
print("%i nota(s) de R$ 100.00" % nota_100)
print("%i nota(s) de R$ 50.00" % nota_50)
print("%i nota(s) de R$ 20.00" % nota_20)
print("%i nota(s) de R$ 10.00" % nota_10)
print("%i nota(s) de R$ 5.00" % nota_5)
print("%i nota(s) de R$ 2.00" % nota_2)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % moeda_1)
print("%i moeda(s) de R$ 0.50" % moeda_05)
print("%i moeda(s) de R$ 0.25" % moeda_025)
print("%i moeda(s) de R$ 0.10" % moeda_010)
print("%i moeda(s) de R$ 0.05" % moeda_005)
print("%i moeda(s) de R$ 0.01" % moeda_001)