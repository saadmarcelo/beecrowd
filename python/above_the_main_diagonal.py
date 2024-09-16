'''
Read an uppercase character that indicates an operation that will be performed in an array M[12][12]. Then, calculate and print the sum or average considering only that numbers that are above the main diagonal of the array, like shown in the following figure (green area).




Input

The first line of the input contains a single uppercase character O ('S' or 'M'), indicating the operation Sum or Average (Média in portuguese) to be performed with the elements of the array. Follow 144 floating-point numbers of the array.

Output

Print the calculated result (sum or average), with one digit after the decimal point.

Input Sample	Output Sample
S
5.0
0.0
-3.5
2.5
4.1
...
                12.6
'''

o=input()
m = []

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

if o == 'S':
    s = 0
    c = 1
    for i in range(0,11):
        for j in range(c,12):
            #print('m[{}][{}]'.format(i,j))
            s = s + m[i][j]
        c = c + 1
    print('{:.1f}'.format(s))

if o == 'M':
    s = 0
    c = 1
    c2=0
    for i in range(0,11):
        for j in range(c,12):
            #print('m[{}][{}]'.format(i,j))
            s = s + m[i][j]
            c2= c2 + 1
        c = c + 1

    m=s/(c2)
    print('{:.1f}'.format(m))