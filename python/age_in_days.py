age = int(input())

ano = 0
mes = 0
dia = 0

while age >= 365:
    age -= 365
    ano += 1
while age >= 30:
    age -= 30
    mes += 1

dia = age

print("%d ano(s)" % ano)
print("%d mes(es)" % mes)
print("%d dia(s)" % dia)
