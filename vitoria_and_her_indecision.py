'''
There’s no one in the world more indecisive than Vitória. Despite the fact that she knows she’s a great programmer, like one of the that have a lot of projects in IT field published and many others being written, she’s not sure if she’s going to be a professional programmer. There are nights that she wants to study Computer Science (Ciência da Computação, in portuguese), there are days she wants to study some Engineering, some days she even talks about taking some Humanities course, what a sin! But you can help her do the right choice. Your task is simple, It’ll be given a list with the bachelor courses that Vitória is in doubt, the output should be the course she must choose.

Input

The first line of the input is an integer 1 ≤ n ≤ 2000, representing the number of courses that must be considered. Each of the next n lines, there is a course S, 1 ≤ |S| ≤ 100, the name of one of the courses Vitória is in the doubt.

Output

Print the name of the course Vitória must take in portuguese without accentuation.

Input Samples	        Output Samples
3
Ciencia da Computacao
Engenharia Eletrica
Matematica
                        Ciencia da Computacao
3
Sociologia
Filosofia
Fisica
                        Ciencia da Computacao
'''

n = int(input())

for _ in range(n):
    s = str(input())

print("Ciencia da Computacao")