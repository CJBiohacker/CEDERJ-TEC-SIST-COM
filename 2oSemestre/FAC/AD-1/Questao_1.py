dna_letter_code = ("A", "C", "G", "T", "a", "c", "g", "t")
s = input('Digite uma sequencia de DNA: ')
nonDnaPosition: list[int] = []

for i in range(len(s)):
    if s[i] not in dna_letter_code: nonDnaPosition.append(i)

if len(nonDnaPosition) == 1: print(f"Sequência inválida, pois na posição {nonDnaPosition} o elemento não possui valor esperado" )
elif len(nonDnaPosition) > 1: print(f"Sequência inválida, pois na posição {nonDnaPosition} os elementos não possuem valores esperados.")
else : print("Sequência válida")

