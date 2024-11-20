import sys


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
    s = sys.argv[1].upper()
    assert any(c not in m.keys() for c in s), "the arguments are bad"
    
    print(sys.argv[1].upper())
    print('$' in m.keys())
    print([c not in m.keys() for c in sys.argv[1].upper()])
    morse_code = []
    for char in sys.argv[1].upper():
        if char in m:
            morse_code.append(m[char])
        else:
            morse_code.append('? ')
    print(''.join(morse_code)[:-1])


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
