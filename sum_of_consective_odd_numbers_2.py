'''
Read an integer N that is the number of test cases. Each test case is a line containing two integer numbers X and Y. Print the sum of all odd values between them, not including X and Y.

Input

The first line of input is an integer N that is the number of test cases that follow. Each test case is a line containing two integer X and Y.

Output

Print the sum of all odd numbers between X and Y.

Input Sample	Output Sample
7
4 5
13 10
6 4
3 3
3 5
3 4
3 8
                        0
                        11
                        5
                        0
                        0
                        0
                        12
'''
n = int(input())

for _ in range(n):
    X,Y= map(int,input().split())
    start = min(X,Y)+1
    end = max(X,Y)
    if start % 2 == 0:
        start += 1

    sum = 0
    for i in range(start, end, 2):
        sum += i
    print(sum)
