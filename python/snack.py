'''
Using the following table, write a program that reads a code and the amount of an item. After, print the value to pay. This is a very simple program with the only intention of practice of selection commands.




Input

The input file contains two integer numbers X and Y. X is the product code and Y is the quantity of this item according to the above table.

Output

The output must be a message "Total: R$ " followed by the total value to be paid, with 2 digits after the decimal point.

Input Sample	    Output Sample
3 2
                    Total: R$ 10.00
4 3
                    Total: R$ 6.00
2 3
                    Total: R$ 13.50

'''


code = [1,2,3,4,5]
price = [4, 4.5, 5, 2, 1.5]

line_data = input()
data = line_data.split()

indice = int(data[0])
quantidade = int(data[1])


total = quantidade * (price[indice - 1])

print("Total: R$ %.2f" % total)
