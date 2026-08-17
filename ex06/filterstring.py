from ft_filter import ft_filter
import sys


def main():
    try:
        assert len(sys.argv) == 3
        assert sys.argv[2].isdigit()
        num = int(sys.argv[2])
        lst = sys.argv[1].split(' ')
        print(ft_filter.__doc__)
        print(ft_filter(lambda x: len(x) > num, lst))
        # test with original
        print(filter.__doc__)
        print(list(filter(lambda x: len(x) > num, lst)))
    except AssertionError:
        print("AssertionError: the arguments are bad")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
