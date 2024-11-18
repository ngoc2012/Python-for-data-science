import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) == 1:
        count(input("What is the text to count?\n") + "\n")
        return
    assert len(sys.argv) == 2, "more than one argument is provided"
    s = sys.argv[1]
    count(s)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
