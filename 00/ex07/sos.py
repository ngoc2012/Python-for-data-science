import sys
from ft_filter import ft_filter


def main():
    """Main function of the program that take the string and the number as\
 argument and return a list of string that are longer than the number given"""
    m = {
        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
        '0': '----- ',
        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        ' ': ' / '
    }
    assert len(sys.argv) == 2, "the arguments are bad"
    assert any(c in s for c not in m.keys()), "the arguments are bad"
    
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append('? ')  # Handle unknown characters
    print(''.join(morse_code))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
