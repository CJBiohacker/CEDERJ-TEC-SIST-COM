# Operações e Variáveis - Aula 2 Exercícios 2

print("*********** Problema A ***********\n")

radius = float(input("Enter the value of the\033[1m radius(m) \033[0m: "))
sphereVol = (4/3) * 3.14159 * radius ** 3
print(f"Sphere Volume = \033[1m {sphereVol:.3f} \033[0m m³")

print("**********************************\n")
print("*********** Problema B ***********\n")

x = int(input("Enter the value of the\033[1m distance(km) \033[0m: "))
y = float(input("Enter the value of the\033[1m fuel consumption(l) \033[0m: "))
avgEffiency = x / y

print(f"Average Fuel Efficiency = \033[1m {avgEffiency:.3f} \033[0m km/l")

print("**********************************\n")
print("*********** Problema C ***********\n")

distance = float(input("Enter the value of the\033[1m distance(km) \033[0m: "))
timeCalc = int(2 * distance)

print(f"Time = \033[1m {timeCalc}\033[0m minutes")

print("**********************************\n")
print("*********** Problema D ***********\n")

fuelConsumption = 12
timeSpent = int(input("Enter the value of the\033[1m time spent(hours) in the trip \033[0m: "))
avgSpeed = int(input("Enter the value of the\033[1m average speed(km/h) \033[0m: "))

print(f"Time = \033[1m {timeCalc}\033[0m minutes")

print("**********************************\n")
print("*********** Problema E ***********\n")

timeInSeconds = int(input("Enter the value of the\033[1m time in seconds \033[0m: "))
calcHours = timeInSeconds / 3600
calcMinutes = (timeInSeconds % 3600) / 60
calcSeconds = timeInSeconds % 60

print(f"Current Time = \033[1m {calcHours:.0f}:{calcMinutes:.0f}:{calcSeconds:.0f}\033[0m")

print("**********************************\n")
print("*********** Problema F ***********\n")

ageInDays = int(input("Enter the value of the\033[1m age in days \033[0m: "))
calcYears = ageInDays // 365
calcMonths = (ageInDays % 365) // 30
calcDays =  (ageInDays % 365) % 30

print(f"Current Time = \033[1m {calcYears:.0f} year(s),\n{calcMonths:.0f} month(s) and\n{calcDays:.0f} days(s)\033[0m")

print("**********************************\n")