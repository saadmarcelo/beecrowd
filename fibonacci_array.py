'''
Write a program that reads a number and print the Fibonacci number corresponding to this read number. Remember that the first elements of the Fibonacci series are 0 and 1 and each next term is the sum of the two preceding it. All the Fibonacci numbers calculated in this program must fit in a unsigned 64 bits number.

Input

The first line of the input contains a single integer T, indicating the number of test cases. Each test case contains a single integer N (0 ≤ N ≤ 60), corresponding to the N-th term of the Fibonacci series.

Output

For each test case in the input, print the message "Fib(N) = X", where X is the N-th term of the Fibonacci series.

Input Sample	Output Sample
3
0
4
2
                Fib(0) = 0
                Fib(4) = 3
                Fib(2) = 1
'''
t=int(input())

for _ in range(t):
    n = int(input())

    u_1 = 1
    u_2 = 1
    count = 0

    lista = [0,1,1]

    for _ in range(60):
        count = u_1 + u_2
        u_1 = count
        u_2 = (count - u_2)
        lista.append(count)
    print("Fib(%d) = %d"%(n,lista[n]))