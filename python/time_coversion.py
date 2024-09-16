tempo = int(input())

hora = 0
minuto = 0
segundo = 0



while tempo >= 3600:
    tempo -= 3600
    hora += 1
while tempo >= 60:
    tempo -= 60
    minuto += 1

segundo = tempo


print("%d:%d:%d" % (hora, minuto ,segundo) )