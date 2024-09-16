line_data = input()
data = line_data.split()

line_data2 = input()
data2 = line_data2.split()

CODE1 = int(data[0])
UNIT1 = int(data[1])
PRICE1 = float(data[2])

CODE2 = int(data2[0])
UNIT2 = int(data2[1])
PRICE2 = float(data2[2])


VALOR = ((UNIT1*PRICE1) + (UNIT2*PRICE2))

print("VALOR A PAGAR: R$ %.2f" % VALOR)