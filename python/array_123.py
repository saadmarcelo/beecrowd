'''
Read an integer N that is the size of a bidimentional array that must be printed like the given example.

Input

The input contains many test cases and ends with EOF. Each test case consist in a integer number N (3 ≤ N < 70), that indicates the size (lines and columns) of a bidimentional array that must be printed.

Output

For each N read, print the output according to the given example.

Sample Input	Sample Output
4
7
                1332
                3123
                3213
                2331
                1333332
                3133323
                3313233
                3332333
                3323133
                3233313
                2333331
'''
while True:
    try:
        N = int(input())

        resultado =  []

        col2 = N - 1
        for i in range(N):
            tmp = []
            for j in range(N):
                if(j==col2):
                    tmp.append(2)
                    col2 -= 1
                else:
                    if(i == j):
                        tmp.append(1)
                    else:
                        tmp.append(3)
            resultado.append(tmp)

        for i in range(N):
            tx = ''
            for j in range(N):
                tx += str(resultado[i][j])
            print(tx)
    except EOFError:
        break