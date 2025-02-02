"""
PURPOSE:
Exercise 1: Reverse the Characters of a String

Write a recursive function called reverter_caracteres(s) that takes a string s and returns the reversed string. Do not use loops (for or while).
"""

def reverser_chars(user_str: str) -> None:
    """Displays a string inverted.

    Using variable atribuition, array, print and recursion,
    displays a string as it is inverted.

    Args:
        user_str (str): String, inputed by user, that will be inverted.
    """
    if user_str:
        last_char = user_str[-1]
        new_str = user_str[:-1]
        print(last_char, end="")
        reverser_chars(new_str)
    else:
        return

user_str = input('\nInsert a small text, so that it is inverted: ')

reverser_chars(user_str)