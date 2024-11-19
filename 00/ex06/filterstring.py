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
    assert len(sys.argv) == 3 and isInt(sys.argv[2]), "the argument are bad"
    s = sys.argv[1]
    count(s)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
