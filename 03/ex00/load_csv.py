import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return its contents as a Pandas DataFrame.

    :param path: Path to the CSV file.
    :return: Pandas DataFrame containing the dataset,
    or None if an error occurs.
    """
    try:
        if not isinstance(path, str):
            raise TypeError(f"Expected a string, got {type(path).__name__}")

        df = pd.read_csv(path, dtype=str)

        if df.empty and len(df.columns) == 0:
            print("Warning: Loaded an empty DataFrame (no columns, no data).")
            return None

        if df.shape[0] == 0:
            print("Warning: Loaded a DataFrame with only a header (no data).")
            return df

        if df.empty and len(df.columns) > 0:
            print("Warning: Loaded a malformed file with headers but no rows.")
            return None

        print(f"Loading dataset of dimensions {df.shape}")

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
