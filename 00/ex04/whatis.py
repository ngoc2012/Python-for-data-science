import sys


def isEven(number: int) -> bool:
    """ Checks if a number is even. """
    return number % 2 == 0


def isInt(number: float) -> bool:
    """ Checks if a number is an integer. """
    try:
        int(number)
        return True
    except ValueError:
        return False


def main():
    """ Main function of a program that checks if a number is odd or even. """
    if len(sys.argv) == 1:
        return
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert isInt(sys.argv[1]), "argument is not an integer"
    if isEven(int(sys.argv[1])):
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
