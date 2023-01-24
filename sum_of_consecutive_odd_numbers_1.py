'''
Read two integer values X and Y. Print the sum of all odd values between them.

Input

The input file contain two integer values.

Output

The program must print an integer number. This number is the sum off all odd values between both input values that must fit in an integer number.

Sample Input	Sample Output
6
-5
                5
15
12
                13
12
12
                0
'''

n = int(input())
k = int(input())

count = 0

if n > k:
    for c in range(k,n):
        if c%2 !=0:
            count += c
elif n < k:
    for c in range(n,k):
        if c%2 !=0:
            count += c

else:
    count = 0

print(count)