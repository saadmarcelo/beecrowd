'''
Make a program that reads five integer values. Count how many of these values ​​are even and  print this information like the following example.

Input

The input will be 5 integer values.

Output

Print a message like the following example with all letters in lowercase, indicating how many even numbers were typed.

Input Sample	Output Sample
7
-5
6
-4
12
                3 valores pares
'''

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())

# lista = [num1,num2,num3,num4,num5]

count = 0
for _ in range(5):
    Value = int(input())
    if Value%2 == 0:
        count += 1

print("%d valores pares" % count)