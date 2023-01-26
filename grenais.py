'''
The Federação Gaúcha de Futebol invited you to write a program to present a statistical result of several GRENAIS. Write a program that read the number of goals scored by Inter and the number of goals scored by Gremio in a GRENAL. Write the message "Novo grenal (1-sim 2-nao)" and request a response. If the answer is 1, two new numbers must be read (another input case) asking the number of goals scored by the teams in a new departure, otherwise the program must be finished, printing:

- How many GRENAIS were part of the statistics.
- The number of victories of Inter.
- The number of victories of Gremio.
- The number of Draws.
- A message indicating the team that won the largest number of GRENAIS (or the message: "Não houve vencedor" if both team won the same quantity of GRENAIS).

Input

The input contains two integer values​​, corresponding to the goals scored by both teams. Then there is an integer (1 or 2), corresponding to the repetition of the algorithm.

Output

After each reading of the goals it must be printed the message "Novo grenal (1-sim 2-nao)". When the program is finished, the program must print the statistics as the example below.

Input Sample	Output Sample
3 2
1
2 3
1
3 1
2
                    Novo grenal (1-sim 2-nao)
                    Novo grenal (1-sim 2-nao)
                    Novo grenal (1-sim 2-nao)
                    3 grenais
                    Inter:2
                    Gremio:1
                    Empates:0
'''
menu = 1
vitoria_gremio = 0
vitoria_inter = 0
count =0
Empates = 0
while menu == 1:
    gol_inter,gol_gremio = map(int,input().split())
    if gol_gremio>gol_inter:
        vitoria_gremio +=1
        count +=1
    if gol_gremio<gol_inter:
        vitoria_inter +=1
        count +=1
    if gol_gremio==gol_inter:
        Empates += 1
        count +=1
    print('Novo grenal (1-sim 2-nao)')
    menu = int(input())
    while not (menu == 1 or menu == 2):
        menu = int(input('Novo grenal (1-sim 2-nao)\n'))
    if menu == 2:
        print("%d grenais" % count)
        print("Inter:%d" % vitoria_inter)
        print("Gremio:%d" % vitoria_gremio)
        print("Empates:%d" % Empates)
        if vitoria_gremio==vitoria_inter:
            print("Não houve vencedor")
        if vitoria_gremio>vitoria_inter:
            print("Gremio venceu mais")
        if vitoria_gremio<vitoria_inter:
            print("Inter venceu mais")