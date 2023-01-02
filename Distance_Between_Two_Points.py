'''
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2) and calculate the distance between them, showing four decimal places after the comma, according to the formula:

Distance = /gallery/images/problems/UOJ_1015.png

Input

The input file contains two lines of data. The first one contains two double values: x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

Output

Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.

Input Sample	Output Sample
1.0 7.0         4.4721
5.0 9.0

-2.5 0.4        16.1484
12.1 7.3

2.5 -0.4        16.4575
-12.2 7.0

'''

line1_data = input()
data1 = line1_data.split()

line2_data = input()
data2 = line2_data.split()

x1 = float(data1[0])
y1 = float(data1[1])

x2 = float(data2[0])
y2 = float(data2[1])


distance = ((x2 - x1)**2) + ((y2 - y1)**2)
quadrado = (distance**0.5)

print("%.4f" % quadrado)



