k = int(input('Digite o tamanho do conjunto de caracteres (k): '))
s = input('Digite a sequência de DNA: ')


def count_distinct_substrings(string_size: int, sequence: str):
    dna_letter_code = ("A", "C", "G", "T", "a", "c", "g", "t")
    substrings = set()
    if string_size <= 0: return print("Tamanho do conjunto(k) inválido.")
    elif len(sequence) == 0: return print("Sequência inválida")
    else:
        for i in range(len(sequence)):
            if sequence[i] not in dna_letter_code:
                return print("Sequência inválida")
            if (i + string_size) > len(sequence):
                break
            else:
                for j in range(i, i + string_size, string_size):
                    substrings.add(sequence[j:j + string_size].upper())
    return print(len(substrings))

count_distinct_substrings(k, s)