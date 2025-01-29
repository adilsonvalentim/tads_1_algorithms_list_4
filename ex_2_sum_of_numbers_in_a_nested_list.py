"""
Exercício 2: Soma de Números em uma Lista Aninhada
Implemente uma função recursiva chamada soma_lista_aninhada(lista) que calcula a
soma de todos os números em uma lista, mesmo que os números estejam dentro de
sublistas (listas aninhadas).
Exemplo de Entrada:
soma_lista_aninhada([1, [2, 3], [4, [5]]])
Saída Esperada:
15 # (1 + 2 + 3 + 4 + 5)
Dica: Verifique se o elemento atual é uma lista ou um número para decidir se deve
continuar a recursão.
"""
import ast

def sum_of_numbers_in_nested_list2(actual_list: list):
    sum = 0
    for i, element in enumerate(actual_list):
        if isinstance(element, int):
            sum += actual_list[i]
        elif isinstance(element, list):
            sum += sum_of_numbers_in_nested_list2(element)
    return sum
    
"""
examples to use:
[1, [2, 3], [4, [5, 10]]]
[1, [2, [2, [1, 6, 2], 3], [[1, 4, 3], 3, 2], [4, [5, 10]]]]

"""
user_input = input('\nInsert a small text, so that it can be reversed:')
nested_list = ast.literal_eval(user_input) #!!!

sum = 0
print(f'\nThe sum of integers of the list of nested lists is: {sum_of_numbers_in_nested_list2(nested_list)}')