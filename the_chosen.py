'''
Everyone is talking about the Jatoba Teacher classes. The MEC representatives came to the UNIME of Lauro de Freitas to know more details about this new way of teaching algorithms. In addition, they wanted to select one student to participate in the OBI-Tec (Olympiad Informatics Technical Level) and represent Kroton in the competition, because they know that there are the best. To select the best, they have available a list of the registration number of each student and their respective notes in the discipline. Your task is to help the Ministry of Education staff to find students better able to represent the institution and who knows guarantee your place. If the highest score is not greater than or equal to 8, you should print "Minimum note not reached" .

Input

The file first contains the number of students (3 <= n <= 100) and then the n students bearing the registration number (0 < m < 1000000) each, followed by the note (0 <= note <= 10.0, with 1 decimal place).

Obs .: the notes will not be repeated. In other words, has no chance to have two students with the same note.

Output

You must print the student's registration number with the highest score or "Minimum note not reached" (without quotes) if no student has taken greater note than or equal to 8.

Input Sample	Output Sample
3
1000 5
1001 10
1002 6
                1001
4
900775 5.7
201553 7.9
5032 6.2
2088 2.1
                Minimum note not reached
4
900775 9.4
999999 9.9
10022 9.7
441002 9.8
                999999
'''
def quant_alunos():
    n = int(input())
    return n
n = quant_alunos()
m = 0.0
al = 0
while(n > 0):
    n -= 1
    a, b = input().split()
    if float(b) > m:
        m = float(b)
        al = int(a)
if m >= 8:
    print(al)
else:
    print("Minimum note not reached")