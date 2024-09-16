'''
Make a program that prints the sequence like the following example.

Input

This problem doesn't have input.

Output

Print the sequence like the example below.

Input Sample	Output Sample
                    I=1 J=7
                    I=1 J=6
                    I=1 J=5
                    I=3 J=9
                    I=3 J=8
                    I=3 J=7
                    ...
                    I=9 J=15
                    I=9 J=14
                    I=9 J=13
'''

i=1
x=3
indice = 2
while i<=9:
    count = 1
    indice += 2
    j=indice+x
    while count <= 3:
        print("I=%d J=%d"% (i,j))
        count += 1
        j -= 1
    i += 2