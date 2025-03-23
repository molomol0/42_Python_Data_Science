def count_in_list(lst, str):
    number = 0
    for element in lst:
        if element == str:
            number += 1
    return number
