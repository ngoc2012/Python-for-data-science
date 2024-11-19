import sys
from ft_filter import ft_filter


def isInt(number: float) -> bool:
    """Check if a number is an integer"""
    try:
        int(number)
        return True
    except ValueError:
        return False


def main():
    """Main function of the program that take the string and the number as argument\
 and return a list of string that are longer than the number given"""
    assert len(sys.argv) == 3 and isInt(sys.argv[2]), "the argument are bad"
    print(ft_filter(lambda x: len(x) > int(sys.argv[2]), sys.argv[1].split()))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
