'''
Make a program that prints the sequence like the following example.

Input

This problem doesn't have input.

Output

Print the sequence like the example below.

Input Sample	Output Sample
I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0

'''

i=1
j=60

while j>=0:
    print("I=%d J=%d"% (i,j))
    i += 3
    j -= 5