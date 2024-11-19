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
    assert len(sys.argv) == 3, "the argument are bad"
    assert isInt(sys.argv[2]), "argument is not an integer"
    s = sys.argv[1]
    count(s)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
