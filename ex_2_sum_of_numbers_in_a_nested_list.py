"""
PURPOSE:
Exercise 2: Sum of Numbers in a Nested List
Implement a recursive function called soma_lista_aninhada(lista) that calculates the sum of all numbers in a list, even if the numbers are inside sublists (nested lists).

Example Input:
sum_nested_list([1, [2, 3], [4, [5]]])

Expected Output:
15 # (1 + 2 + 3 + 4 + 5)

Tip: Check if the current element is a list or a number to decide whether to continue the recursion.
"""
#import ast

def sum_of_numbers_in_nested_list(actual_list: list) -> int:
    """Sum numbers of a nested list

    Using interation via for with enumerate, will check
    the type of each element of the list, if the element
    is an int, will sum this value in the summation variable,
    but if the element is a list, will iterate with it via
    recursion. At the end the function returns the sum of every
    integer elements in the nested list.

    Args:
        actual_list (list): Nested list whose values will be added together.

    Returns:
        int: Sum of all integers of the nested list.
    """
    sum = 0
    for i, element in enumerate(actual_list):
        if isinstance(element, int):
            sum += actual_list[i]
        elif isinstance(element, list):
            sum += sum_of_numbers_in_nested_list(element)
    return sum

#examples to use:
#user_input = input('\nInsert a list of nested lists:')
#nested_list = ast.literal_eval(user_input) #!!!

nested_list = [1, [2, [2, [1, 6, 2], 3], [[1, 4, 3], 3, 2], [4, [5, 11]]]]
sum = 0
print(f'\nThe sum of integers of the list of nested lists is: {sum_of_numbers_in_nested_list(nested_list)}')