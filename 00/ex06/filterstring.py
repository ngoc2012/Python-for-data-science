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
    """Main function of the program that take the string and the number as\
 argument and return a list of string that are longer than the number given"""
    assert len(sys.argv) == 3 and isInt(sys.argv[2]), "the arguments are bad"
    a = sys.argv[1].split()
    assert len([x for x in a if x.isalnum()]) == len(a), "the arguments are bad"
    print(ft_filter(lambda x: len(x) > int(sys.argv[2]), a))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
