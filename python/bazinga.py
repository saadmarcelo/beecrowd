'''
In the 8th episode of Big Bang Theory's second season, The Lizard-Spock Expansion, Sheldon and Raj are arguing about what is the best: the movie Saturn 3 or the TV show Deep Space 9. Raj suggests rock-paper-scissors to settle down the dispute. However, Sheldon says "Ooh, I don't think so. No, anectodal evidence suggests that in the game of rock-paper-scissors, players familiar with each other will tie 75 to 80% of the time due to the limited number of outcomes. I suggest rock-paper-scissors-lizard-Spock".

The rules of the game are:

scissors cuts paper;
paper covers rock;
rock crushes lizard;
lizard poisons Spock;
Spock smashes scissors;
scissors decapitates lizard;
lizard eats paper;
paper disproves Spock;
Spock vaporizes rock;
rock crushes scissors.
Both choosed Spock and the game tied. However, it isn't hard to realize what would happened if the game had continued. In the case of Sheldon's victory, he would've said: "Bazinga!"; if Raj had won, Sheldon would declare: "Raj trapaceou!" ("Raj cheated" in portuguese); in ties, he would request a new game: "De novo!" ("Again!", in portuguese). Given the options chosen by both, make a program that prints Sheldon reaction to the outcome.

Input

The first line contains an integer T (T ≤ 100) indicating the number of test cases. Each test case is described using one line. The line contains Sheldon and Raj options, separated by one blank space. The possible options are: pedra, papel, tesoura, lagarto e Spock (rock, paper, scissors, lizard and Spock).

Output

For each test case your program must output a single line with the following message: "Caso #t: R", where t is the test case number and R is Sheldon's reaction to the outcome: "Bazinga!", "Raj trapaceou!", or "De novo!".

Input Samples	                Output Samples
3
papel pedra
lagarto tesoura
Spock Spock
                                Caso #1: Bazinga!
                                Caso #2: Raj trapaceou!
                                Caso #3: De novo!
'''
def jogada():
    s, r = map(str,input().split())
    return s,r

def contagem(cont):
    cont += 1
    return cont

def winner(a,b,cont,play):
    w = 1
    if a == 'tesoura' and b == 'papel':
        w = a
    if a == 'papel' and b == 'pedra':
        w = a
    if a == 'pedra' and b == 'lagarto':
        w = a
    if a == 'lagarto' and b =='Spock':
        w = a
    if a == 'Spock' and b == 'tesoura':
        w = a
    if a == 'tesoura' and b == 'lagarto':
        w = a
    if a == 'lagarto' and b == 'papel':
        w = a
    if a == 'papel' and b == 'Spock':
        w = a
    if a == 'Spock' and b == 'pedra':
        w = a
    if a == 'pedra' and b == 'tesoura':
        w = a
    if w == a:
        if play == 'she':
            print('Caso #{}: Bazinga!'.format(cont))
        if play == 'raj':
            print('Caso #{}: Raj trapaceou!'.format(cont))
    return w

def main():
    n = int(input())
    cont = 1
    for i in range(n):
        s, r = jogada()
        w = winner(s,r,cont,'she')
        if w != 1:
            cont = contagem(cont)
            continue
        w = winner(r,s,cont,'raj')
        if w != 1:
            cont = contagem(cont)
            continue
        if w == 1:
            print('Caso #{}: De novo!'.format(cont))
        cont = contagem(cont)

main()