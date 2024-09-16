'''
Maria has just started as graduate student in a medical school and she's needing your help to organize a laboratory experiment which she is responsible about. She wants to know, at the end of the year, how many animals were used in this laboratory and the percentage of each type of animal is used at all.

This laboratory uses in particular three types of animals: frogs, rats and rabbits. To obtain this information, it knows exactly the number of experiments that were performed, the type and quantity of each animal is used in each experiment.

Input

The first line of input contains an integer N indicating the number of test cases that follows. Each test case contains an integer Amount (1 ≤ Amount ≤ 15) which represents the amount of animal used and a character Type ('C', 'R' or 'S'), indicating the type of animal:
- C: Coelho (rabbit in portuguese)
- R: Rato (rat  in portuguese)
- S: Sapo (frog in portuguese)

Output

Print the total of animals used, the total of each type of animal and the percentual of each one in relation of the total of animals used. The percentual must be printed with 2 digits after the decimal point.

Input Sample	Output Sample
10
10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R
                    Total: 92 cobaias
                    Total de coelhos: 29
                    Total de ratos: 40
                    Total de sapos: 23
                    Percentual de coelhos: 31.52 %
                    Percentual de ratos: 43.48 %
                    Percentual de sapos: 25.00 %

'''

coelho = 0
rato = 0
sapo = 0
total = 0
percentual_coelho = 0
percentual_rato = 0
percentual_sapo = 0

n = int(input())
for _ in range(n):
    line_exp = input()
    exp = line_exp.split()
    quantidade = int(exp[0])
    tipo_animal = str(exp[1])

    total += quantidade
    if tipo_animal == 'C':
        coelho += quantidade
    elif tipo_animal == 'R':
        rato += quantidade
    elif tipo_animal == 'S':
        sapo += quantidade

percentual_coelho = (coelho * 100)/total
percentual_rato = (rato * 100)/total
percentual_sapo = (sapo * 100)/total



print('Total: %d cobaias'% total)
print('Total de coelhos: %d' % coelho)
print('Total de ratos: %d' % rato)
print('Total de sapos: %d' % sapo)
print('Percentual de coelhos: %.2f %%' % percentual_coelho)
print('Percentual de ratos: %.2f %%' % percentual_rato)
print('Percentual de sapos: %.2f %%' % percentual_sapo)
