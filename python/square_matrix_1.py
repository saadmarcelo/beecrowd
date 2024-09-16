'''
Write a program that read an integer number N (0 ≤ N ≤ 100) that correspond to the order of a Bidimentional array of integers, and build the Array according to the above example.

Input

The input consists of several integers numbers, one per line, corresponding to orders from arrays to be built. The end of input is indicated by zero (0).

Output

For each integer number of input, print the corresponding array according to the example. (the values ​​of the arrays must be formatted in a field of size 3 right justified and separated by a space. None space must be printed after the last character of each row of the array. A blank line must be printed after each array.

Sample Input	Sample Output
1
2
3
4
5
0
                    1

                    1   1
                    1   1

                    1   1   1
                    1   2   1
                    1   1   1

                    1   1   1   1
                    1   2   2   1
                    1   2   2   1
                    1   1   1   1

                    1   1   1   1   1
                    1   2   2   2   1
                    1   2   3   2   1
                    1   2   2   2   1
                    1   1   1   1   1
'''
while True:
    N = int(input())

    if (N == 0):
        break

    resultado =  []

    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(1)
        resultado.append(tmp)

    valor = 1
    cima = 0
    esq = 0
    baixo = N - 1
    direita = N - 1

    if (N % 2 == 0):
        meio = N / 2

    else:
        meio = (N + 1) / 2


    while (valor <= meio):
        i = esq
        while (i <= direita):
            resultado[cima][i] = valor
            resultado[baixo][i] = valor
            i+=1

        i = (cima + 1)
        while ( i < baixo):
            resultado[i][esq] = valor
            resultado[i][direita] = valor
            i+=1

        valor+=1
        cima+=1
        baixo-=1
        esq+=1
        direita-=1

    for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" %resultado[i][j]
        print(tx[1:])
    print("")
