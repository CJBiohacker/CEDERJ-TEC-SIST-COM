# Sequência, Estruturas de Seleção e Repetição - Aula 3 Exercícios 1

print("*********** Problema A ***********\n")

print("Considere a tabela abaixo para a entrada de variáveis:\n")
print("+--------------+-------------+------------+")
print("|   SUBFILO    |   CLASSE    |    DIETA   |")
print("+--------------+-------------+------------+")
print("|              |             |  carnívoro |")
print("|              |     ave     +------------+")
print("|              |             |   onívoro  |")
print("+  vertebrado  +-------------+------------+")
print("|              |             |   onívoro  |")
print("|              |   mamífero  +------------+")
print("|              |             |  herbívoro |")
print("+--------------+-------------+------------+")
print("|              |             | hematófago |")
print("|              |   inseto    +------------+")
print("|              |             |  herbívoro |")
print("+ invertebrado +-------------+------------+")
print("|              |             | hematófago |")
print("|              |   anelídeo  +------------+")
print("|              |             |   onívoro  |")
print("+--------------+-------------+------------+")

subfilo = input("Insira o valor do seu\033[1m subfilo \033[0m: ")
classe = input("Insira o valor da sua\033[1m classe \033[0m: ")
dieta = input("Insira o valor da sua\033[1m dieta \033[0m: ")

print("Processando valores...")

if subfilo == "vertebrado":
    if classe == "ave":
        if dieta == "carnívoro" or dieta == "carnivoro":
            print("Animal = Águia")
        elif dieta == "onívoro" or dieta == "onivoro":
            print("Animal = Pombo")
        else:
            print("Dieta inválida. Reinicie o programa e tente novamente.")
    elif classe == "mamífero" or classe == "mamifero":
        if dieta == "onívoro" or dieta == "onivoro":
            print("Animal = Humano")
        elif dieta == "herbívoro" or dieta == "herbivoro":
            print("Animal = Vaca")
        else:
            print("Dieta inválida. Reinicie o programa e tente novamente.")
    else:
        print("Classe inválida. Reinicie o programa e tente novamente.")
elif subfilo == "invertebrado":
    if classe == "inseto":
        if dieta == "hematófago" or dieta == "hematofago":
            print("Animal = Pulga")
        elif dieta == "herbívoro" or dieta == "herbivoro":
            print("Animal = Lagarta")
    elif classe == "anelídeo" or classe == "anelideo":
        if dieta == "hematófago" or dieta == "hematofago":
            print("Animal = Sanguessuga")
        elif dieta == "onívoro" or dieta == "onivoro":
            print("Animal = Minhoca")
    else:
        print("Classe inválida. Reinicie o programa e tente novamente.")
else:
    print("Subfilo inválido. Reinicie o programa e tente novamente.")

print("**********************************\n")
print("*********** Problema B ***********\n")

print("Considere a tabela abaixo para a entrada de variáveis:\n")
print("+-------+-----------------+")
print("| {:<5} | {:<15} |".format("DDD", "Destino"))
print("| {:<5} | {:<15} |".format("61", "Brasilia"))
print("| {:<5} | {:<15} |".format("71", "Salvador"))
print("| {:<5} | {:<15} |".format("11", "Sao Paulo"))
print("| {:<5} | {:<15} |".format("21", "Rio de Janeiro"))
print("| {:<5} | {:<15} |".format("32", "Juiz de Fora"))
print("| {:<5} | {:<15} |".format("19", "Campinas"))
print("| {:<5} | {:<15} |".format("27", "Vitoria"))
print("| {:<5} | {:<15} |".format("31", "Belo Horizonte"))
print("+-------+-----------------+")

dddValue = input("Insira o seu\033[1m DDD \033[0m: ")

if dddValue == "61": print("Destino = Brasilia")
elif dddValue == "71": print("Destino = Salvador")
elif dddValue == "11": print("Destino = Sao Paulo")
elif dddValue == "21": print("Destino = Rio de Janeiro")
elif dddValue == "32": print("Destino = Juiz de Fora")
elif dddValue == "19": print("Destino = Campinas")
elif dddValue == "27": print("Destino = Vitoria")
elif dddValue == "31": print("Destino = Belo Horizonte")
else: print("DDD não cadastrado")

print("**********************************\n")
print("*********** Problema C ***********\n")

print("Classic use of While statement")
i = 0
while i <= 100:
    print(f"{i}")
    i += 2
print("-----------------------------------------")

print("While statement using break and conditional")
if i != 0: i = 0;
while True:
    print(f"{i}")
    if i >= 100: break
    i += 2
print("-----------------------------------------")

print("For statement with Range function")
if i != 0: i = 0;
for i in range(0, 101, 2):
    print(f"Nº = {i}")
print("-----------------------------------------")

print("**********************************\n")
print("*********** Problema D ***********\n")

i = 0
totalPositives = 0
sum = 0
while i < 6:
    num = float(input("Enter the number: "))
    if num > 0: totalPositives += 1
    sum += num
    i += 1
print(f"{totalPositives} positive values")
print(f"Average = {sum / i:.2f}")

print("**********************************\n")
print("*********** Problema E ***********\n")

insideRange = 0
outsideRange = 0
totalValues = int(input("How much numbers do you want to enter? "))
TOTAL_VALUES_THRESHOLD = 10000
VALUE_THRESHOLD = 10**7

if totalValues > TOTAL_VALUES_THRESHOLD:
    print("The program will not run due to the total number of values entered being greater than 10000.")
    exit()

for i in range(0, totalValues):
    currentValue = float(input("Enter the value: "))
    if -VALUE_THRESHOLD <= currentValue >= VALUE_THRESHOLD:
        print("Value out of specified range. Restart the program and enter a value between -10^7 and 10^7.")
        break
    else:
        if 10 <= currentValue <= 20: insideRange += 1
        else: outsideRange += 1

print(f"Values inside the range: {insideRange}")
print(f"Values outside the range: {outsideRange}")

print("**********************************\n")
print("*********** Problema F ***********\n")

CORRECT_PASSWORD = 2002
password = ""
while password != CORRECT_PASSWORD:
    password = int(input("Enter the password: "))
    if password == CORRECT_PASSWORD:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.\n")

print("**********************************\n")

