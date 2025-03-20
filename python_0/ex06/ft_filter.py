def ft_filter(func, iterable):
    """
    Take a function and an iterator
    Add the element to the result if the function return true
    Return the new iterator
    """
    newIte = [x for x in iterable if func(x)]

    return (newIte)


# def even(number):
#     return number % 2


# def main():
#     ite = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(ft_filter(even, ite))
#     result = filter(even, ite)
#     print(list(result))


# if __name__ == "__main__":
#     main()
