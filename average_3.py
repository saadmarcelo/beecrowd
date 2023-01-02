'''
Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal point, corresponding to 4 scores obtained by a student. Calculate the average with weights 2, 3, 4 e 1 respectively, for these 4 scores and print the message "Media: " (Average), followed by the calculated result. If the average was 7.0 or more, print the message "Aluno aprovado." (Approved Student). If the average was less than 5.0, print the message: "Aluno reprovado." (Reproved Student). If the average was between 5.0 and 6.9, including these, the program must print the message "Aluno em exame." (In exam student).

In case of exam, read one more score. Print the message "Nota do exame: " (Exam score) followed by the typed score. Recalculate the average (sum the exam score with the previous calculated average and divide by 2) and print the message “Aluno aprovado.” (Approved student) in case of average 5.0 or more) or "Aluno reprovado." (Reproved student) in case of average 4.9 or less. For these 2 cases (approved or reproved after the exam) print the message "Media final: " (Final average) followed by the final average for this student in the last line.

Input

The input contains four floating point numbers that represent the students' grades.

Output

Print all the answers with one digit after the decimal point.

Input Sample	    Output Sample
2.0 4.0 7.5 8.0
6.4
                    Media: 5.4
                    Aluno em exame.
                    Nota do exame: 6.4
                    Aluno aprovado.
                    Media final: 5.9
2.0 6.5 4.0 9.0
                    Media: 4.8
                    Aluno reprovado.
9.0 4.0 8.5 9.0
                    Media: 7.3
                    Aluno aprovado.
'''
n1,n2,n3,n4 = map(float,input().split())

media =(2*n1 + 3*n2 + 4*n3 + 1*n4)/10
print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame: %.1f" % n5)
    mediafinal = (media + n5)/2
    if mediafinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % mediafinal)