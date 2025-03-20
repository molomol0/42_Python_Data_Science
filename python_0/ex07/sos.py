import sys

NESTED_MORSE = {

    ' ': '/ ',
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
    '0': '----- ',
}


def morseIt(string):
    """
    Check if every arguments is printable
    Translate teh character in a result
    Print the result
    """
    morse = ""
    try:
        for x in string:
            assert str(x).isalnum(), "the arguments are bad"
            morse += NESTED_MORSE[str(x).upper()]
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    print(morse)


def main(argv):
    """
    Check the number of argument
    Then call the morse function
    """
    try:
        assert len(argv) == 2, "the arguments are bad"

    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

    morseIt(argv[1])


if __name__ == "__main__":
    main(sys.argv)
