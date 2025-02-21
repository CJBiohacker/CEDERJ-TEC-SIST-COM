k = int(input('Digite o tamanho do conjunto de caracteres (k): '))
n = int(input('Digite o nº de repetições do conjunto(n): '))
s = input('Digite a sequência de DNA: ')

def list_most_repeated_sequency(string_size: int, sequence: str):
    dna_letter_code = ("A", "C", "G", "T", "a", "c", "g", "t")
    substrings = dict()
    if string_size <= 0:
        return print("Tamanho do conjunto(k) inválido.")
    elif len(sequence) == 0:
        return print("Sequência inválida")
    else:
        for i in range(len(sequence)):
            if sequence[i] not in dna_letter_code:
                return print("Sequência inválida")
            if (i + string_size) > len(sequence):
                break
            else:
                for j in range(i, i + string_size, string_size):
                    current_substring = substrings.get(f"{sequence[j:j + string_size]}")
                    if current_substring == None:
                        substrings.update({f"{sequence[j:j + string_size]}": 1})
                    elif current_substring > 0:
                        substrings.update({f"{sequence[j:j + string_size]}": current_substring + 1})

    count = 0
    for key, value in substrings.items():
        if value == string_size:
            print(key.upper())
            count += 1
        else:
            continue

    if count == 0: return print("Sequência inválida")

list_most_repeated_sequency(k, s)
