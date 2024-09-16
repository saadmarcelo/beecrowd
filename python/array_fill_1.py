'''
Read a number and make a program which puts this number in the first position of an array N[10]. In each subsequent position, put the double of the previous position. For example, if the input number is 1, the array numbers ​​must be 1,2,4,8, and so on.

Input

The input contains an integer number V (V < 50).

Output

Print the stored number of each array position, in the form "N[i] = X", where i is the position of the array and x is the stored number at the position i. The first number for X is V.

Input Sample	Output Sample
1
                    N[0] = 1
                    N[1] = 2
                    N[2] = 4
...
'''
X = []
value=int(input())
for i in range(10):
    X.insert(i,value)
    value= value*2
for i in range(10):
    print('N[{0}] = {1}'.format(i,X[i]))