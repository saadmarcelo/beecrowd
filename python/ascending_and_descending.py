'''
Read an undetermined number of pairs of integer values. Write a message for each pair indicating if this two numbers are in ascending or descending order.

Input

The input file contains several test cases. Each test case contains two integer numbers X and Y. The input will finished when X = Y.

Output

For each test case print “Crescente”, if the values X and Y are in ascending order, otherwise print “Decrescente”.

Input Sample	Output Sample
5 4                 Decrescente
7 2                 Decrescente
3 8                 crescente
2 2

'''
X=1
Y=1
while X>0 and Y>0:
    X,Y= map(int,input().split())
    if X==Y:
        break
    else:
        if X<Y:
            print("Crescente")
        else:
            print('Decrescente')