'''
Write a program that read an integer number N (0 ≤ N ≤ 100) that correspont to the order of a Bidimentional array of integers, and build the Array according to the above example.

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

                1   2
                2   1

                1   2   3
                2   1   2
                3   2   1

                1   2   3   4
                2   1   2   3
                3   2   1   2
                4   3   2   1

                1   2   3   4   5
                2   1   2   3   4
                3   2   1   2   3
                4   3   2   1   2
                5   4   3   2   1
'''
while True:
    N = int(input())

    if (N == 0):
        break

    resultado =  []

    for i in range(1,(N+1)):
        tmp = []
        count = i
        for j in range(N):
            tmp.append(abs(count))
            if(count == 1):
                count -= 3
            else:
                count -= 1
        resultado.append(tmp)

    for i in range(N):
        tx = ''
        for j in range(N):
            tx += " %3d" %resultado[i][j]
        print(tx[1:])
    print("")
