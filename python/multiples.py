'''
Read two nteger values (A and B). After, the program should print the message "Sao Multiplos" (are multiples) or "Nao sao Multiplos" (aren’t multiples), corresponding to the read values.

Input

The input has two integer numbers.

Output

Print the relative message to the input as stated above.

Input Sample	Output Sample
6 24
                Sao Multiplos
6 25
                Nao sao Multiplos
'''
a,b = map(int,input().split())

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a == b:
    print('Sao Multiplos')