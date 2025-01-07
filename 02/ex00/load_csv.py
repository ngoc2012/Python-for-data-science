import numpy as np

def load(path: str) -> np.object_:
    """
    Load a CSV file and return its contents as a NumPy object array.

    :param path: Path to the CSV file.
    :return: NumPy array containing the dataset.
    """
    try:
        # Load the CSV file into a NumPy array, skipping the header row
        data = np.genfromtxt(path, delimiter=',', dtype=None, encoding='utf-8', skip_header=1)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
