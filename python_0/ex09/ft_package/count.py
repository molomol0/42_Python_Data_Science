def count_in_list(lst, str):
    """
    Take a list and a string
    Count de number de string similar to the argument in the list
    Return the result
    """
    number = 0
    for element in lst:
        if element == str:
            number += 1
    return number
