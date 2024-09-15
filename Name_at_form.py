'''
Filling forms is a simple task. But it is necessary to check if the reserved space for data is large enough.

Your task is, given a text line, to indicate if it fits in an 80 characters length form.

Input

Input is a text line L (1 ≤ |L| ≤ 500).

Output

The output is given in a single line. It must be "YES" (without quotes) if the text line L is up to 80 characters long. If L has more than 80 characters, the output must be "NO".

Input Samples	                                                                                                                                    Output Samples
Fulano de Tal
                                                                                                                                                    YES
Pedro de Alcantara Francisco Antonio Joao Carlos Xavier de Paula Miguel Rafael Joaquim Jose Gonzaga Pascoal Cipriano Serafim
                                                                                                                                                    NO

'''

l = str(input())

if len(l)<=80:
    print("YES")
else:
    print("NO")