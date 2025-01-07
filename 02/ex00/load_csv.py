import pandas as pd

def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return its contents as a Pandas DataFrame.

    :param path: Path to the CSV file.
    :return: Pandas DataFrame containing the dataset, or None if an error occurs.
    """
    try:
        # Check if the path is a string
        if not isinstance(path, str):
            raise TypeError(f"Expected 'path' to be a string, but got {type(path).__name__}")
        
        # Load the CSV file using pandas
        df = pd.read_csv(path, dtype=str)  # dtype=str ensures everything is read as string

        # Handle cases where the CSV might be empty or malformed
        if df.empty:
            print("Warning: Loaded an empty DataFrame.")
            return None

        # If the DataFrame has no rows (only header), log a warning and return it
        if df.shape[0] == 0:
            print("Warning: Loaded a DataFrame with only a header (no data).")
            return df  # Return the empty DataFrame


        # Print the dimensions (rows, columns)
        print(f"Loading dataset of dimensions {df.shape}")  # This will print something like (num_rows, num_columns)
        
        return df
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        return None
    except TypeError as te:
        print(f"Type Error: {te}")
        return None
    except pd.errors.ParserError as pe:
        print(f"CSV Parsing Error: {pe}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

