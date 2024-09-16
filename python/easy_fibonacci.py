'''
The following sequence of numbers 0 1 1 2 3 5 8 13 21 ... is known as the Fibonacci Sequence. Thereafter, each number after the first 2 is equal to the sum of the previous two numbers. Write an algorithm that reads an integer N (N < 46) and that print the first N numbers of this sequence.

Input

The input file contains an integer number N (0 < N < 46).

Output

The numbers ​​should be printed on the same line, separated by a blank space. There is no space after the last number.

Input Sample	Output Sample
5
                0 1 1 2 3
'''

n = int(input())

u_1 = 1
u_2 = 1
count = 0

lista = [0,1,1]

for _ in range(n-3):
    count = u_1 + u_2
    u_1 = count
    u_2 = (count - u_2)
    lista.append(count)

print(*lista, sep=' ')