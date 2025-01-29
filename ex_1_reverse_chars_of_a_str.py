"""Exercício 1: Reverter os Caracteres de uma String
Escreva uma função recursiva chamada reverter_caracteres(s) que recebe uma
string s e devolve a string invertida. Não use laços (for ou while)."""

def reverter_chars(user_str: str):
    if user_str:
        last_char = user_str[-1]
        new_str = user_str[:-1]
        print(last_char, end="")
        reverter_chars(new_str)
    else:
        return

user_str = input('\nInsira um pequeno texto, para que possa ser revertido: ')

reverter_chars(user_str)