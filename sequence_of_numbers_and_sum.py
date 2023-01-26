'''
Read an undetermined number of pairs values M and N (stop when any of these values is less or equal to zero). For each pair, print the sequence from the smallest to the biggest (including both) and the sum of consecutive integers between them (including both).

Input

The input file contains pairs of integer values M and N. The last line of the file contains a number zero or negative, or both.

Output

For each pair of numbers, print the sequence from the smallest to the biggest and the sum of these values, as shown below.

Input Sample	Output Sample
5 2
6 3
5 0
                2 3 4 5 Sum=14
                3 4 5 6 Sum=18

'''
X=1
Y=1
while X>0 and Y>0:
    X,Y= map(int,input().split())
    start = min(X,Y)
    end = max(X,Y)
    if X==0 or Y==0:
        break
    else:
        sum = 0
        lista =[]
        for i in range(start, end+1, 1):
            sum += i
            lista.append(i)

        print("%s Sum=%d" % (''.join(lista),sum))
