'''
Read an uppercase character that indicates an operation that will be performed in an array M[12][12]. Then, calculate and print the sum or average considering only that numbers that are above the secundary diagonal of the array, like shown in the following figure (green area).




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
m=[]
letra = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)
c = 12
s = 0
cont = 0
for i in range(11):
    c -=1
    for j in range(c):
        s += m[i][j]
        cont += 1

if letra == 'S':
    print('{}'.format(s))

if letra == 'M':
    med = s / cont
    print('{:.1f}'.format(med))