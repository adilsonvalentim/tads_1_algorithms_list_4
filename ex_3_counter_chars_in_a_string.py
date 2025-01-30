'''
Exercício 3: Contar Caracteres em uma String
Crie uma função recursiva chamada contar_caracteres(s, c) que conta quantas vezes o
caractere c aparece na string s.
Exemplo de Entrada:
contar_caracteres("banana", "a")
Saída Esperada:
3
'''

def count_characters(word: str, char: str, amount: int = 0) -> None:
    if word:
        last_char = word[-1]
        word = word[:-1]
        if last_char == char:
            amount += 1
        count_characters(word, char, amount)
    else:
        print(
            f'\nThe word "{c}", appears {amount} times in "{s}" word.'
        )
        return

s = "banana"
c = "a"
count_characters(s, c)