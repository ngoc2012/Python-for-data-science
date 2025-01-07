import csv
import numpy as np

def load(path: str) -> np.object_:
    """
    Load a CSV file and return its contents as a NumPy object array.

    :param path: Path to the CSV file.
    :return: NumPy array containing the dataset, or None if an error occurs.
    """
    try:
        # Check if the path is a string
        if not isinstance(path, str):
            raise TypeError(f"Expected 'path' to be a string, but got {type(path).__name__}")
        
        # Read CSV with csv.reader to handle quoted fields
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Convert to NumPy array
        header = data[0]  # Optional: Extract header if needed
        rows = data[1:]   # Data rows
        return np.array(rows, dtype=object)
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        return None
    except TypeError as te:
        print(f"Type Error: {te}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

