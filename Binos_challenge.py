'''
Bino and Cino are close friends. Bino likes to create mathematical challenges to Cino. This time, Bino created a list of numbers and asked to Cino: How many numbers are multiples of 2, 3, 4 and 5?

This challenge looks simple, but when the list contains many numbers, Cino makes some miscalculations. To help Cino, make a program to solve the Bino's Challenge.

Input

The first line of input consists of an integer N (1 ≤ N ≤1000), representing the amount of numbers in the Bino's list.

The second line contains N integers Li (1 ≤ Li ≤ 100), representing the numbers of the Bino's list.

Output

Print the amount of multiples of 2, 3, 4 and 5 in the list. Note the formatting of the output in the output sample, because it must be followed strictly. "Multiplo(s)" means "Multiple(s)" in English, but you must print the message in Portuguese.

Input Sample	Output Sample
5
2 5 4 20 10
                4 Multiplo(s) de 2
                0 Multiplo(s) de 3
                2 Multiplo(s) de 4
                3 Multiplo(s) de 5
'''

N = int(input())

mult_two = 0
mult_three = 0
mult_for = 0
mult_five = 0

values = input().split(' ')
values_correctly = values[:N]
for i in range(N):
    values_correctly[i] = int(values_correctly[i])
    if(values_correctly[i] % 2 ==0):
        mult_two+=1
    if(values_correctly[i] % 3 ==0):
        mult_three+=1
    if(values_correctly[i] % 4 ==0):
        mult_for+=1
    if(values_correctly[i] % 5 ==0):
        mult_five+=1

print('{0} Multiplo(s) de 2'.format(mult_two))
print('{0} Multiplo(s) de 3'.format(mult_three))
print('{0} Multiplo(s) de 4'.format(mult_for))
print('{0} Multiplo(s) de 5'.format(mult_five))