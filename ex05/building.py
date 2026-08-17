import sys


def print_sums(text: str):
    ''' Takes a single string argument and displays the sums of \
    its upper-case characters, lower-case characters, punctuation \
    characters, digits, and spaces. '''
    print(f'The text contains {len(text)} characters:')
    print(f'{sum(c.isupper() for c in text)} upper letters')
    print(f'{sum(c.islower() for c in text)} lower letters')
    print(f'{sum(not c.isalnum() and not c.isspace() for c in text)} \
punctuation marks')
    print(f'{sum(c.isspace() for c in text)} spaces')
    print(f'{sum(c.isdigit() for c in text)} digits')


def main():
    try:
        assert len(sys.argv) <= 2
        if len(sys.argv) < 2:
            print("What is the text to count?")
            text = sys.stdin.readline()
            if text and not text.endswith("\n"):
                print()
            print_sums(text)
        else:
            print_sums(sys.argv[1])
    except AssertionError:
        print("AssertionError: more than one argument is provided")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Pressed CTRL-C")


if __name__ == "__main__":
    # print(print_sums.__doc__)
    main()
