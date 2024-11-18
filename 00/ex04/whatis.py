import sys


def isEven(number: int) -> bool:
    return number % 2 == 0


def isInt(number: float) -> bool:
    try:
        num_int = int(number)
        return True
    except ValueError:
        return False


def main():
    print("main")
    if len(sys.argv) == 1:
        return
    assert len(sys.argv) == 2, "more than one argument is provided"

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
