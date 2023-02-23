'''
Sunday is market day. Early in the morning many people move to the Parangaba square where happens a fair, known to be the largest in the city. At the fair the Parangaba you can find everything.

Every Sunday, Bino make purchases at the fair. He always mark with his friend Cino, they met at the bus terminal of Parangaba at 8 am to go together to buy at the fair. But often Bino wake up too late and is late for the meeting with his friend.

Knowing that Bino takes 30-60 minutes to reach the terminal. Tell the maximum delay Bino.

Input

The input consists of multiple test cases. Each case contains a single line containing a time H (5:00 ≤ H ≤ 9:00) that Bino woken up. The input ends with the final file (EOF).

Output

For each test case, print "Atraso maximo: X" (without quotes), X indicates the maximum delay (in minutes) of Bino in the encounter with Cino.

Input Sample	Output Sample
7:10
5:00
                Atraso maximo: 10
                Atraso maximo: 0
'''
def minuto(n):
    tempo = 60 * n
    return tempo

while True:
    try:
        h = input()
        data = h.split(sep=":")
        n = int(data[0])
        m = int(data[1])
        tempo = minuto(n)

        valor = tempo+m+60
        horario = minuto(8)
        if horario>valor:
            print("Atraso maximo: 0")
        else:
            horario = horario - valor
            print("Atraso maximo: %d" % abs(horario))

    except EOFError:
        break