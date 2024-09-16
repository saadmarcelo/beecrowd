'''
Read three integers and sort them in ascending order. After, print these values in ascending order, a blank line and then the values in the sequence as they were readed.

Input

The input contains three integer numbers.

Output

Present the output as requested above.

Input Sample	Output Sample
7 21 -14
                -14
                7
                21

                7
                21
                -14

-14 21 7
                -14
                7
                21

                -14
                21
                7
'''

n1,n2,n3 = map(int,input().split())

lista = [n1,n2,n3]
lista2 = sorted(lista)

for i in range(len(lista)):
    print(lista2[i])

print() #Espaço em branco

for i in range(len(lista2)):
    print(lista[i])

