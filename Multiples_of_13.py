'''
Write a program that reads two integer numbers X and Y and calculate the sum of all number not divisible by 13 between them, including both.

Input

The input file contains 2 integer numbers X and Y without any order.

Output

Print the sum of all numbers between X and Y not divisible by 13, including them if it is the case.

Input Sample	Output Sample
100
200
                13954
'''

x = int(input())
y = int(input())

start = min(x,y)
end = max(x,y)
soma=0

for _ in range(start, end+1):
    if _%13!=0:
        soma += _

print(soma)