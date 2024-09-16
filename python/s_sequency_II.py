'''
Write an algorithm to calculate and write the value of S, S being given by:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

Input

There is no input in this problem.

Output

The output contains a value corresponding to the value of S.
The value should be printed with two digits after the decimal point.

Input Sample	Output Sample
'''

s = 0
sup=1
inf=1
for _ in range(1,40,2):
    s=_/inf + s
    inf=inf*2
print("%.2f"%s)


# s=0
# j = 1
# for i in range(1,40,2):
#     s = float(s + i / j)
#     j = j * 2
# print('{:.2f}'.format(s))