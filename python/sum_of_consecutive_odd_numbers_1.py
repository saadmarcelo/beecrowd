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

X = int(input())
Y = int(input())
start = min(X,Y)+1
end = max(X,Y)
if start % 2 == 0:
    start += 1

sum = 0
for i in range(start, end, 2):
    sum += i
print(sum)