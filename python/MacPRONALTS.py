'''
The MacPRONALTS is with a super promotion, exclusive to the contestants of the first Selective MaratonaTEC. But they had a problem, all runners were trying to buy at the same time, so this generated a very long queue. The worst is that the cashier girl no have calculator or a program to help her to calculate more quickly. You are the person that will help the girl and the MacPRONALTS increase their sells. Bellow has a menu day, that contains the product number and its value.

1001 | R$ 1.50

1002 | R$ 2.50

1003 | R$ 3.50

1004 | R$ 4.50

1005 | R$ 5.50

Input

The first entry is reported the number of purchased products (1 <= p <= 5). For each product follows the quantity (1 <= q <= 500) that the customer purchased.

Obs .: the product number will not be repeated.

Output

You must print the purchase amount with two decimal places.

Input Sample	Output Sample
2
1001 2
1005 3
                19.50
1
1003 500
                1750.00
5
1001 500
1005 300
1003 23
1002 52
1004 44
                2808.50
'''
def quant_pedidos():
    n = int(input())
    return n

n = quant_pedidos()
conta = 0
while(n>0):
    n -=1
    a, b = map(int,input().split())
    if a==1001:
        conta = conta + (1.50*b)
    if a==1002:
        conta = conta + (2.50*b)
    if a==1003:
        conta = conta + (3.50*b)
    if a==1004:
        conta = conta + (4.50*b)
    if a==1005:
        conta = conta + (5.50*b)

print("%.2f" % conta)


