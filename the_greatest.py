line_data = input()
data = line_data.split()

A = int(data[0])
B = int(data[1])
C = int(data[2])

MaiorAB = ((A+B)+abs(A-B))/2
MaiorBC = ((MaiorAB+C)+abs(MaiorAB-C))/2
print("%.f eh o maior" % MaiorBC)