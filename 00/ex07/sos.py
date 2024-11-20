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
    # Dictionary to map alphanumeric characters to Morse code with a space at the end
    morse_code_dict = {
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
    
    def alphanumeric_to_morse(text):
        morse_code = []
        for char in text.upper():
            if char in morse_code_dict:
                morse_code.append(morse_code_dict[char])
            else:
                morse_code.append('? ')  # Handle unknown characters
        return ''.join(morse_code)
    
    # Example usage
    input_text = "HELLO WORLD"
    morse_code_output = alphanumeric_to_morse(input_text)
    print(morse_code_output)

    print(ft_filter(lambda x: len(x) > int(sys.argv[2]), sys.argv[1].split()))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
