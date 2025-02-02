'''
PURPOSE:

Exercise 3: Count Characters in a String
Create a recursive function called contar_caracteres(s, c) that counts how many times the character c appears in the string s.

Example Input:
count_characters("banana", "a")

Expected Output:
3
'''

def count_characters(word: str, char: str, amount: int = 0) -> None:
    """Displays how many times a character appears in a string.

    Checks character by character in a string, via assignment
    to variable, array, addition in a summation variable and recursion.
    After checks every character, displays via print how many 
    times the selected character appears in the string.

    Args:
        word (str): String where the number of characters will be searched.
        char (str): Character that will be counted in the string.
        amount (int, optional): Summation variable that will stores the amount. Defaults to 0.
    """
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