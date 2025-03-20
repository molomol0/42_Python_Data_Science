import sys


def filter(func, strings):
    """
    Filter the words and print them
    """
    result = [x for x in strings if func(x)]
    print(result)


def filterstring(argv):
    """
    Parse the arguments
    Then call the filter function
    """
    strings = argv[1].split(" ")
    limit = argv[2]

    filter(lambda x: len(str(x)) > int(limit), strings)


def main(argv):
    """
    Check if the arguments are valid
    Then call filterstring()
    """
    try:
        assert len(argv) == 3, "the arguments are bad"
        assert argv[1].isascii(), "the arguments are bad"
        assert argv[2].isnumeric(), "the arguments are bad"

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    filterstring(argv)


if __name__ == "__main__":
    main(sys.argv)
