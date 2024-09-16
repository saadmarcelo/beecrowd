'''
Read an integer N that is the number of test cases that follows. Each test case contains two integers X and Y. Print one output line for each test case that is the sum of Y odd numbers from X including it if is the case. For example:
for the input 4 5, the output must be 45, that is: 5 + 7 + 9 + 11 + 13
for the input 7 4, the output must be 40, that is: 7 + 9 + 11 + 13

Input

The first line of the input is an integer N that is the number of test cases that follow. Each test case is a line containing two integer X and Y.

Output

Print the sum of all consecutive odd numbers from X.

Input Sample	Output Sample
2                   21
4 3                 24
11 2
'''
n = int(input())
for i in range(0,n):
    x,y=map(int,input().split())
    soma = 0
    j = 1
    while j <= y:
        if x % 2 != 0:
            soma = soma + x
            x = x + 1
            j = j + 1
        if x % 2 == 0:
            x = x + 1
    print(soma)