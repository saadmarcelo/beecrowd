'''
Write a program to read the coordinates (X, Y) of an indeterminate number of points in Cartesian system. For each point write the quadrant to which it belongs. The program finish when at least one of two coordinates is NULL (in this situation without writing any message).

Input

The input contains several tests cases. Each test case contains two integer numbers.

Output

For each test case, print the corresponding quadrant which these coordinates belong, as in the example.

Input Sample	Output Sample
2 2                 primeiro
3 -2                quarto
-8 -1               terceiro
-7 1                segundo
0 2
'''
i =1
while i==1:
    X,Y= map(int,input().split())
    if X==0 or Y==0:
        break
    else:
        if X>0 and Y>0:
            print("primeiro")
        elif X>0 and Y<0:
            print('quarto')
        elif X<0 and Y<0:
            print('terceiro')
        elif X<0 and Y>0:
            print('segundo')