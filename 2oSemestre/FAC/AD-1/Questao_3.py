s = input('Digite uma sequencia de DNA: ')

def iterate_dna(sequence: str):
    """
        Processa uma sequência de DNA e retorna seu complemento reverso.

        Esta função recebe uma sequência, garante que todos caracteres são bases nucleotidas
        válidas e processa a sequência complementar reversa.
        Este complemento reverso  é calculado usando a seguinte lógica:
            - 'A' or 'a' -> 'T'
            - 'C' or 'c' -> 'G'
            - 'G' or 'g' -> 'C'
            - 'T' or 't' -> 'A'

        Se a entrada conter qualquer caractere inválido, uma mensagem de erro é impressa.

        Parâmetros:
            sequence (str): Uma string contendo a sequência de DNA.
                            Deve possuir somente as letras 'A', 'C', 'G', 'T' (case-insensitive).
        """
    dna_letter_code = ("A", "C", "G", "T", "a", "c", "g", "t")
    comp_a, comp_t, comp_g, comp_c = 'T', 'A', 'C', 'G'
    reverse_complement = ""
    for i in range(len(sequence)):
        if sequence[i] not in dna_letter_code:
            print("Sequência inválida")
            break
        else:
            if sequence[i] == "A" or sequence[i] == "a":
                reverse_complement+=comp_a
            elif sequence[i] == "C" or sequence[i] == "c":
                reverse_complement+=comp_c
            elif sequence[i] == "G" or sequence[i] == "g":
                reverse_complement+=comp_g
            elif sequence[i] == "T" or sequence[i] == "t":
                reverse_complement+=comp_t

        if i == len(sequence)-1:
            print(f"Dada a sequência {s.upper()}, seu reverso complementar é: {reverse_complement}")

iterate_dna(s)