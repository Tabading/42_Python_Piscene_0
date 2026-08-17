import sys


def convert_to_morse(text: str):
    ''' Convert Alphanumeric Text to Morse Code. Space is accepted. '''
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
    }
    new = ""
    for c in text:
        new += NESTED_MORSE[c]
    print(new)


def main():
    try:
        assert len(sys.argv) == 2
        for c in sys.argv[1]:
            if not c.isalnum() and not c.isspace():
                raise AssertionError
        print(convert_to_morse.__doc__)
        convert_to_morse(sys.argv[1].upper())
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
