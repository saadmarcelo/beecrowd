'''

Hopscotch is probably the game where townhouse's children more have fun, however the game has caused a good time for discussion and crying in children who practice it. The cause of the disorder is to decide who will be the next to jump, but recently Quico (The Genius!) had a great idea for to solve the problem. Basically the game can only to be played every two players in one turn and to choose the next player Quico indicated to use the traditional method even or odd, where both players report one number and if the sum these numbers is even, the player that choose PAR win or vice verse. However the use that method has left the Quico crazy, crazy, crazy... And for that reason he asked for your help, asked you a program that given the name of the players, their respective choices (PAR or IMPAR) and the numbers, tell who was the winner.

Input

The first line of input contains a single integer QT (1 ≤ QT ≤ 100), indicating the number of following test cases. Each test case contains two lines. In first line will be told the name of the player 1 followed by his choice, “PAR” or “IMPAR”, and after the name of the player 2 followed by his choice, “PAR” or “IMPAR”. In second line of test case, contains two integer number N (1 ≤ N ≤ 10⁹) and M (1 ≤ M ≤ 10⁹), representing respectively the numbers chosen by players 1 and player 2. It it garanteed that player 1 choice's (PAR or IMPAR) will be differ from choice of player 2 (PAR or IMPAR) and that the name of the players consist only of letters and will not exceed 100 characters.

Output

For each test case, print a single line containing the name of winner player.

Input Sample	                Output Sample
4
Quico PAR Chiquinha IMPAR
9 7
Dami PAR Marcus IMPAR
12 3
Dayran PAR Conrado IMPAR
3 1000000000
Popis PAR Chaves IMPAR
2 7
                                Quico
                                Marcus
                                Conrado
                                Chaves
'''
qt = int(input())
for _ in range(qt):
    line_data = input()
    data = line_data.split()
    player1 = str(data[0])
    player1_jogada = str(data[1])
    player2 = str(data[2])
    player2_jogada = str(data[3])
    line_data2 = input()
    data2 = line_data2.split()
    N = int(data2[0])
    M = int(data2[1])

    if (N+M)%2 == 0:
        result= 'PAR'
    else:
        result = 'IMPAR'

    if result == player1_jogada:
        print(player1)
    else:
        print(player2)