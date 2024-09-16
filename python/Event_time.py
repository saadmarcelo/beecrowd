'''
Peter is organizing an event in his University. The event will be in April month, beginning and finishing within April month. The problem is: Peter wants to calculate the event duration in seconds, knowing obviously the begin and the end time of the event.

You know that the event can take from few seconds to some days, so, you must help Peter to compute the total time corresponding to duration of the event.

Input

The first line of the input contains information about the beginning day of the event in the format: “Dia xx”. The next line contains the start time of the event in the format presented in the sample input. Follow 2 input lines with same format, corresponding to the end of the event.

Output

Your program must print the following output, one information by line, considering that if any information is null for example, the number 0 must be printed in place of W, X, Y or Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Consider that the event of the test case have the minimum duration of one minute. “dia” means day, “hora” means hour, “minuto” means minute and “Segundo” means second in Portuguese.

Input Sample	    Output Sample
Dia 5               3 dia(s)
08 : 12 : 23        22 hora(s)
Dia 9               1 minuto(s)
06 : 13 : 23        0 segundo(s)
'''
from datetime import timedelta


# data de inicio do evento
inicio_dia = input().split(' ')
inicio_time = input().split(':')


day1= int(inicio_dia[1])
hora_inicio = int(inicio_time[0])
min_inicio = int(inicio_time[1])
seg_inicio = int(inicio_time[2])



# data de final do evento
final_dia = input().split(' ')
final_time = input().split(':')


day2= int(final_dia[1])
hora_final = int(final_time[0])
min_final = int(final_time[1])
seg_final = int(final_time[2])

t1 = timedelta(days=day1, hours=hora_inicio, minutes=min_inicio, seconds= seg_inicio)
t2 = timedelta(days=day2, hours=hora_final, minutes=min_final, seconds=seg_final)

t3 = t2 - t1

hora = t3.seconds // 3600
seconds = t3.seconds % 3600
minutes = seconds //60

seconds = seconds % 60

print("%d dia(s)"% t3.days)
print("%d hora(s)" % hora)
print("%s minuto(s)" % minutes)
print("%s segundo(s)" % seconds)

# t4 = str(t3)


# resposta = t4.split(', ')

# dia = resposta[0]
# time = resposta[1]

# r1 = dia.split()
# r2 = time.split(':')

# print("%s dia(s)"% t3.days)
# print("%s hora(s)" % r2[0])
# print("%s minuto(s)" % r2[1])
# print("%s segundo(s)" % r2[2])

