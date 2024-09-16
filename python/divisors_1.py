'''
Read an integer N and compute all its divisors.

Input

The input file contains an integer value.

Output

Write all positive divisors of N, one value per line.

Input Sample	Output Sample
6
                    1
                    2
                    3
                    6
'''
i=1
n = int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i)
