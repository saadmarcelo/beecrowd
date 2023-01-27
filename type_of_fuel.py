'''
A gas station wants to determine which of their products is the preference of their customers. Write a program to read the type of fuel supplied (coded as follows: 1. Alcohol 2. Gasoline 3. Diesel 4. End). If you enter an invalid code (outside the range of 1 to 4) a new code must be requested. The program will end when the inserted code is the number 4.

Input

The input contains only integer and positive values.

Output

It should be written the message: "MUITO OBRIGADO" and the amount of customers who fueled each fuel type, as an example.

Input Sample	Output Sample
8
1
7
2
2
4
                MUITO OBRIGADO
                Alcool: 1
                Gasolina: 2
                Diesel: 0
'''

alcool = 0
gasolina = 0
diesel = 0
menu = 1
produto=0
while menu>0 and menu<4:

    if produto==1:
        alcool += 1
    elif produto==2:
        gasolina += 1
    elif produto==3:
        diesel +=1
    elif produto==4:
        break
    produto = int(input())
    menu == produto
    while not (produto==1 or produto==2 or produto==3 or produto==4):
        produto = int(input())

print("MUITO OBRIGADO")
print("Alcool: %d"%alcool)
print("Gasolina: %d"%gasolina)
print("Diesel: %d"%diesel)