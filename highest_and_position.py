'''
Read 100 integer numbers. Print the highest read value and the input position.

Input

The input file contains 100 distinct positive integer numbers.

Output

Print the highest number read and the input position of this value, according to the given example.

Input Sample	Output Sample
2
113
45
34565
6
...
8

                34565
                4
'''

lista=[]
for _ in range(100):
    n = int(input())
    lista.append(n)

max_value = max(lista)
max_index = lista.index(max_value)
print(max_value)
print(max_index+1)
