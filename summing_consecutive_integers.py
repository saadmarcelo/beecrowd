
'''
Write an algorithm to read a value A and a value N. Print the sum of N numbers from A (inclusive). While N is negative or ZERO, a new N (only N) must be read. All input values are in the same line.

Input

The input contains only integer values, ​​can be positive or negative.

Output

The output contains only an integer value.

Input Sample	Output Sample
3 2
                    7
3 -1 0 -2 2
                    7
'''

x = list(map(int, input().split()))
i = 1
s = 0

while x[i] <= 0:
    if x[i] <=0:
        i = i + 1
    if x[i] > 0:
        break

for c in range(0,x[i]):
    s = s + x[0] + c

print(s)