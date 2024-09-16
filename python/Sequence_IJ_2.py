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
                I=3 J=7
                I=3 J=6
                I=3 J=5
                ...
                I=9 J=7
                I=9 J=6
                I=9 J=5
'''

i=1
j=7

while i<=9:
    j=7
    while j>=5:
        print("I=%d J=%d"% (i,j))
        j -= 1
    i += 2