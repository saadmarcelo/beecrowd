'''
Write a program that reads two scores of a student. Calculate and print the average of these scores. Your program must accept just valid scores [0..10]. Each score must be validated separately.

Input

The input file contains many floating-point numbers​​, positive or negative. The program execution will be finished after the input of two valid scores.

Output

When an invalid score is read, you should print the message "nota invalida".
After the input of two valid scores, the message "media = " must be printed followed by the average of the student. The average must be printed with 2 numbers after the decimal point.

Input Sample	Output Sample
-3.5            nota invalida
3.5             nota invalida
11.0            media = 6.75
10.0
'''

nota = float(input())
lista =[]

if 0<=nota<=10:
    lista.append(nota)
    