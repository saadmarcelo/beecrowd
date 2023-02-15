'''
Ana and her friends are making a geometry work to school, they need to create various triangles on a chart, with a few sticks of different lengths. Soon they realized that you can not form triangles with three rods of any lengths: if one of the rods is too large relative to the other two, you can't form a triangle.

In this issue, you have to help Ana and her friends to determine if, given the lengths of four rods, it is or not possible to select three rods, among the four, and form a triangle.

Input

The entry consists of one line containing four integers A, B, C and D (1 ≤ A, B, C, D ≤ 100).

Output

Your program should only produce a line containing only one character, which must be 'S' if it is possible to form the triangle or 'N' if you can not form a triangle.

Input Example	    Output Example
6 9 22 15
                    S
14 40 12 60
                    N
'''


A,B,C,D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if A < B + C and B < A + C and C < A + B:
    print('S')
elif A < B + D and B < A + D and D < A + B:
    print('S')
elif A < C + D and C < A + D and D < A + C:
    print('S')
elif B < C + D and C < B + D and D < B + C:
    print('S')
else:
    print('N')