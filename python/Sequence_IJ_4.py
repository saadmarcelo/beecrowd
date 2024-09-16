'''
Make a program that prints the sequence like the following example.

Input

This problem doesn't have input.

Output

Print the sequence like the example below.

Input Sample	Output Sample
                    I=0 J=1
                    I=0 J=2
                    I=0 J=3
                    I=0.2 J=1.2
                    I=0.2 J=2.2
                    I=0.2 J=3.2
                    .....
                    I=2 J=?
                    I=2 J=?
                    I=2 J=?
'''

i=0
x=3
indice = 0
while i<=2:
    count = 1
    j=1+indice
    while count <= 3:
        print("I={:g} J={:g}".format(i, j))
        count += 1
        j += 1
    indice += 0.2
    i += 0.2

