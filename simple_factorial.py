'''
Read a value N. Calculate and write its corresponding factorial. Factorial of N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Input

The input contains an integer value N (0 < N < 13).

Output

The output contains an integer value corresponding to the factorial of N.

Input Sample	Output Sample
4
                24

'''

n = int(input())
fatorial = 1
for i in range(1,n+1):
    fatorial = i * fatorial
print(fatorial)
