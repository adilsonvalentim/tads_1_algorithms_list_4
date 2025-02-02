'''
PURPOSE:

Write a recursive function called highest_element(list) that returns the index of the largest element in a list.

Example Input:
index_higher_element([1, 5, 3, 9, 2])

Expected Output:
3 # The largest element is 9, which is at index 3
'''

def highest_element(elements: list, high_elem: int = -999999, cache: int = 0, high_index: int = 0) -> None:
    """Find the highest element and its index in a list.

    Compares elements in a list via recursion, controls the index 
    using a progressive variable which add one to each recursion 
    and iterates the listusing array. When the list runs out, 
    prints the highest element and its index.

    Args:
        elements (list): Iterable list which contains the elements that will be compared
        high_elem (int, optional): Stores the so far highest element. Defaults to -999999.
        cache (int, optional): Stores a progressive int that references the index. Defaults to 0.
        high_index (int, optional): Stores the so far highest index. Defaults to 0.
    """
    if elements:
        if elements[0] > high_elem:
            high_elem = elements[0]
            high_index = cache
        elements = elements[1:]
        cache += 1
        highest_element(elements, high_elem, cache, high_index)
    else:
        print(
            f'\nThe highest element is {high_elem}, which is at index {high_index}.'
        )
        return

elements_list = [1, 5, 3, 9, 2, 20]
highest_element(elements_list)