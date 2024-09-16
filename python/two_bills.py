'''
Gilberto is a famous sfiha vendor. However, although everyone likes his sfihas, he can only give the change with two different bills, i.e., it's not always possible to get the right change. In order to make Gil's life easier, write a program for him to check whether it's possible to give the exact change using two different bills.

Available bills: 2, 5, 10, 20, 50 and 100.

Input

The input contains an integer N representing the buy price and then an integer M representing the price paid by the costumer (N < M ≤ 104). Read input until N = M = 0.

Output

Print "possible" if it's possible to give the exact change or "impossible" if it's not.

Input Sample	Output Sample
11 23
500 650
100 600
9948 9963
1 2
2 4
0 0
                possible
                possible
                impossible
                possible
                impossible
                impossible
'''
notas = [2, 5, 10, 20, 50, 100]
while True:
    n, m = input().split()
    if(n == '0' and m == '0'):
        break
    n = int(n)
    m = int(m)
    m -= n
    total = 0
    for i in notas:
        if(m == i*2):
            print('possible')
            total = 2
            break
    if total == 0:
        for i in range(len(notas)-1, -1, -1):
            if total == 3:
                break
            if m - notas[i] >= 0:
                m -= notas[i]
                total += 1
        if (m == 0 and total == 2):
            print('possible')
        else:
            print('impossible')