def slice_me(family: list, start: int, end: int) -> list:
    """
    Assert if arguments are valid
    Print the before/after shape of the input array
    Return the sliced array
    """
    try:
        assert all(isinstance(lst, list) for lst in family), \
            "array must contain only list"
        list_length = len(family[0])
        assert all(len(lst) == list_length for lst in family), \
            "list must be the same list_length"
        list_number = len(family)

        print(f"My shape is : ({list_number}, {list_length})")
        new_slice = slice(start, end)
        print(f"My new shape is : ({len(family[new_slice])}, {list_length})")
        return (family[new_slice])

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
