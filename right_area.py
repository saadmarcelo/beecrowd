'''
Read an uppercase character that indicates an operation that will be performed in an array M[12][12]. Then, calculate and print the sum or average considering only that numbers that are included in the right area (green area) of this array, like shown in the following figure.




Input

The first line of the input contains a single uppercase character O ('S' or 'M'), indicating the operation Sum or Average (Média in portuguese) to be performed with the elements of the array. Follow 144 floating-point numbers of the array.

Output

Print the calculated result (sum or average), with one digit after the decimal point.

Input Sample	Output Sample
S
5.0
130.0
-3.5
2.5
4.1
...
                122.2
'''

m=[]
l = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

s = 0
cont = 0
col = 11
for i in range(1,11):
    for j in range(col,12):
        s += m[i][j]
        cont += 1
    if i < 5:
        col -= 1
    if i > 5:
        col += 1
med = s / cont
if l == "S":
    print('{:.1f}'.format(s))
else:
    print('{:.1f}'.format(med))