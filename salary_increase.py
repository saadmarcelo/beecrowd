'''
The company ABC decided to give a salary increase to its employees, according to the following table:


Salary	                            Readjustment Rate
0 - 400.00                                    15%
400.01 - 800.00                               12%
800.01 - 1200.00                              10%
1200.01 - 2000.00                              7%
Above 2000.00                                  4%


Read the employee's salary, calculate and print the new employee's salary, as well the money earned and the increase percentual obtained by the employee, with corresponding messages in Portuguese, as the below example.
Input

The input contains only a floating-point number, with 2 digits after the decimal point.

Output

Print 3 messages followed by the corresponding numbers (see example) informing the new salary, the among of money earned (both must be shown with 2 decimal places) and the percentual obtained by the employee. Note:
Novo salario:  means "New Salary"
Reajuste ganho: means "Money earned"
Em percentual: means "In percentage"

Input Sample	Output Sample
400.00
                Novo salario: 460.00
                Reajuste ganho: 60.00
                Em percentual: 15 %
800.01
                Novo salario: 880.01
                Reajuste ganho: 80.00
                Em percentual: 10 %
2000.00
                Novo salario: 2140.00
                Reajuste ganho: 140.00
                Em percentual: 7 %
'''

salary = float(input())

if (salary >= 0) and (salary<=400):
    new_salary = (salary * 0.15) + salary
    percentual = 15
elif (salary > 400) and (salary<=800):
    new_salary = (salary * 0.12) + salary
    percentual = 12
elif (salary > 800) and (salary<=1200):
    new_salary = (salary * 0.1) + salary
    percentual = 10
elif (salary>1200) and (salary<=2000):
    new_salary = (salary * 0.07) + salary
    percentual = 7
elif (salary >2000):
    new_salary = (salary * 0.04) + salary
    percentual = 4


reajuste = new_salary - salary

print("Novo salario: %.2f" % new_salary)
print("Reajuste ganho: %.2f" % reajuste)
print('Em percentual: %d %%' % percentual)