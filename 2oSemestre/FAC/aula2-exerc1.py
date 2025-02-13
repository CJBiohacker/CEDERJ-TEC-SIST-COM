# Operações e Variáveis - Aula 2 Exercícios 1

print("*********** Problema A ***********\n")

a = int(input("Enter a value for\033[1m a \033[0m: "))
b = int(input("Enter a value for\033[1m b \033[0m: "))
x = a + b

# formatted string style (f-string-literals)
print(f"SUM = {x}")
#  classic style
# print("(classic style)\nThe sum of \033[1m a \033[0m and \033[1m b \033[0m is:", x, "\n")

print("**********************************")
print("*********** Problema B ***********\n")

pi = 3.14159
r = float(input("Enter a value for radius in m²: "))
# area = pi * r ** 2
area = pi * r * r

print(f"Considering, π = 3.14159. Area = {area:.2f}m²\n")

print("**********************************\n")
print("*********** Problema C ***********\n")

a = float(input("Enter a value for\033[1m a \033[0m: "))
b = float(input("Enter a value for\033[1m b \033[0m: "))
c = float(input("Enter a value for\033[1m c \033[0m: "))

weightAverage = (a*2 + b*3 + c*5) / (2 + 3 + 5)

print(f"W.Avg = \033[1m {weightAverage:.2f} \033[0m")

print("**********************************\n")
print("*********** Problema D ***********\n")

A = int(input("Enter a value for\033[1m A \033[0m: "))
B = int(input("Enter a value for\033[1m B \033[0m: "))
C = int(input("Enter a value for\033[1m C \033[0m: "))
D = int(input("Enter a value for\033[1m D \033[0m: "))

diff = (A * B - C * D)

print(f"DIFF = \033[1m {diff} \033[0m")

print("**********************************\n")
print("*********** Problema E ***********\n")

workerID = input("Enter the worker ID number: ")
workHours = float(input("Enter your monthly work hours: "))
salaryPerHour = float(input("Enter your salary per hour: "))
salary = workHours * salaryPerHour

print(f"WORKER ID = \033[1m {workerID} \033[0m")
print(f"MONTHLY SALARY = CNY \033[1m {salary:.2f} \033[0m")

print("**********************************\n")
print("*********** Problema F ***********\n")

salespersonName = input("Enter the Salesperson Name: ")
totalSales = float(input("Enter your monthly sales: "))
comission = totalSales * 0.15

print(f"VENDOR = \033[1m {salespersonName} \033[0m")
print(f"COMISSION = CNY \033[1m {comission:.2f} \033[0m")

print("**********************************\n")