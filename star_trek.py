'''
After buying many adjacent farms at the west region of Santa Catarina, the Star family built a single road which passes by all farms in sequence. The first farm of the sequence was named Star 1, the second Star 2, and so on. However, the brother who lives in Star 1 has got mad and decided to make a Star Trek in order to steal sheep from the proprieties of his siblings. But he is definitely crazy. When passes by the farm Star i, he steals only one sheep (if there is any) from that farm and moves on either to Star i + 1 or Star i - 1, depending on whether the number of sheep in Star i was, respectively, odd or even. If there is not the Star to which he wants to go, he halts his trek. The mad brother starts his Star Trek in Star 1, stealing a sheep from his own farm.

Input

The first input line consists of a single integer N (1 ≤ N ≤ 106), which represents the number of Stars. The second input line consists of N integers, such that the ith integer, Xi (1 ≤ Xi ≤ 106), represents the initial number of sheep in Star i.

Output

Output a line containing two integers, so that the first represents the number of Stars attacked by the mad brother and the second represents the total number of non-stolen sheep.

Exemplo de Entrada	    Exemplo de Saída
8
1 3 5 7 11 13 17 19
                        8 68
8
1 3 5 7 11 13 16 19
                        7 63
'''
n = int(input())  # número de fazendas
x = list(map(int, input().split()))  # quantidade inicial de ovelhas em cada fazenda

# variáveis de controle
attacked = 0  # número de fazendas atacadas
stolen = 0  # quantidade total de ovelhas roubadas

i = 0  # índice da fazenda atual
while i < n:
    if x[i] > 0:  # se há ovelhas para serem roubadas
        attacked += 1  # incrementa o número de fazendas atacadas
        stolen += 1  # incrementa o número de ovelhas roubadas
        if x[i] % 2 == 0:  # se a quantidade de ovelhas é par, avança para a fazenda seguinte
            i += 1
        else:  # se a quantidade de ovelhas é ímpar, volta para a fazenda anterior
            i -= 1
    else:  # se não há ovelhas para serem roubadas, interrompe o Star Trek
        break

print(attacked, stolen)
