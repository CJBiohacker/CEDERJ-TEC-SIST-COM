dna_letter_code = ("A", "C", "G", "T", "a", "c", "g", "t")
s = input('Digite uma sequencia de DNA: ')
nonDnaPosition: list[int] = []
a,c,g,t = 0,0,0,0

for i in range(len(s)):
    if s[i] not in dna_letter_code: nonDnaPosition.append(i)
    else:
        if s[i] == "A" or s[i] == "a": a+=1
        elif s[i] == "C" or s[i] == "c": c+=1
        elif s[i] == "G" or s[i] == "g": g+=1
        elif s[i] == "T" or s[i] == "t": t+=1

if len(nonDnaPosition) == 1: print(f"Sequência inválida, pois na posição {nonDnaPosition} o elemento não possui valor esperado" )
elif len(nonDnaPosition) > 1: print(f"Sequência inválida, pois na posição {nonDnaPosition} os elementos não possuem valores esperados.")
else : print(f"Sequência válida. Além disso, a contagem de cada base nitrogenada é: A:{a} C:{c} G:{g} T:{t}")