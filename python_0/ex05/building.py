import sys
import string
import re


def countAll(string_msg: str):
    """ Take the string, count everything then print it"""

    length = len(string_msg)
    upper = len(re.findall("[A-Z]", string_msg))
    lower = len(re.findall("[a-z]", string_msg))
    punctuation = len(re.findall("[" + string.punctuation + "]", string_msg))
    spaces = len(re.findall("[" + string.whitespace + "]", string_msg))
    digits = len(re.findall("[0-9]", string_msg))

    print(
        "The text contains", length, "characters:\n",
        upper, "upper letters\n",
        lower, "lower letters\n",
        punctuation, "punctuation marks\n",
        spaces, "spaces\n",
        digits, "digits\n"
    )


def main(argv):
    """
    Check if the number of arguments is right
    If the arg is empty ask for a string
    Then call the counting function
    """
    try:
        assert len(argv) <= 2, \
            "Too many arguments"
        if len(argv) == 1:
            print('What is the text to count?')
            string = sys.stdin.read()
        else:
            string = argv[1]
        countAll(string)

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

    except (EOFError, KeyboardInterrupt):
        print("No data provided to input function")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
