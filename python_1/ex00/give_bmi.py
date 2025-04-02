def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Assert if arguments are valid
    Create a list that calculate BMI
    Return the list
    """
    try:
        assert len(height) == len(weight), "list are not the same size"
        assert all(isinstance(element, int | float) for element in weight), \
            "list should only contain int or float"
        assert all(isinstance(element, int | float) for element in height), \
            "list should only contain int or float"

        results = [w / (h * h) for w, h in zip(weight, height)]

        return (results)

    except AssertionError as e:
        print(f"AssertionError : {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Assert if arguments are valid
    Create a list that check if the list elements are above the limit
    Return the list
    """
    try:
        assert all(isinstance(element, int | float) for element in bmi), \
            "list should only contain int or float"

        results = [element > limit for element in bmi]

        return (results)

    except AssertionError as e:
        print(f"AssertionError : {e}")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
