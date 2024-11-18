import sys
import string


def count(s: str):
    print(f"The text contains {len(s)} characters:")
    n_upper = sum([1 for c in s if c.isupper()])
    print(f"{n_upper} upper letters")
    n_lower = sum([1 for c in s if c.islower()])
    print(f"{n_lower} lower letters")
    n_punctuation = sum([1 for c in s if c in string.punctuation])
    print(f"{n_punctuation} punctuation marks")
    n_space = sum([1 for c in s if c.isspace()])
    print(f"{n_space} spaces")
    n_digit = sum([1 for c in s if c.isdigit()])
    print(f"{n_digit} digits")


def main():
    if len(sys.argv) == 1:
        try:
            count(input("What is the text to count?\n") + "\n")
        except EOFError:
            return
        except KeyboardInterrupt:
            print("")
            return
        return
    assert len(sys.argv) == 2, "more than one argument is provided"
    s = sys.argv[1]
    count(s)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
