import unittest as ut
import os
import pandas as pd
from load_csv import load  # Replace 'your_module' with the actual module name where `load` is defined.

class TestLoadFunction(ut.TestCase):
    def test_valid_file(self):
        """Test loading a valid CSV file."""
        test_file = "test_valid.csv"
        
        # Prepare a test CSV file
        with open(test_file, "w") as f:
            f.write("country,1800,1801,1802\n")
            f.write('"Congo, Dem. Rep.",28.2,28.2,28.2\n')
            f.write("Albania,29.2,29.3,29.4\n")
        
        # Call the function and verify results
        result = load(test_file)
        expected = pd.DataFrame({
            'country': ['Congo, Dem. Rep.', 'Albania'],
            '1800': ['28.2', '29.2'],
            '1801': ['28.2', '29.3'],
            '1802': ['28.2', '29.4']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_nonexistent_file(self):
        """Test handling of a nonexistent file."""
        result = load("nonexistent.csv")
        self.assertIsNone(result)

    def test_invalid_path_type(self):
        """Test handling of an invalid path type."""
        result = load(12345)  # Passing an integer instead of a string
        self.assertIsNone(result)

    def test_empty_file(self):
        """Test handling of an empty CSV file."""
        # Prepare an empty test file
        empty_file = "empty.csv"
        open(empty_file, "w").close()
        
        result = load(empty_file)
        self.assertIsNone(result)

    def test_file_with_only_header(self):
        """Test handling of a CSV file with only a header."""
        header_file = "header_only.csv"
        with open(header_file, "w") as f:
            f.write("country,1800,1801,1802\n")
        
        result = load(header_file)
        
        # Verify that the DataFrame is empty except for the column names
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)  # Empty DataFrame has no rows
        self.assertListEqual(list(result.columns), ["country", "1800", "1801", "1802"])

    def test_file_with_invalid_format(self):
        """Test handling of a CSV file with an invalid format."""
        # invalid_file = "invalid.csv"
        # with open(invalid_file, "w") as f:
        #     f.write("not,a,csv,file\n")
        
        result = load(invalid_file)
        self.assertIsNone(result)

    # def tearDown(self):
    #     """Clean up test files after each test."""
    #     test_files = ["test_valid.csv", "empty.csv", "header_only.csv", "invalid.csv"]
    #     for file in test_files:
    #         if os.path.exists(file):
    #             os.remove(file)

if __name__ == "__main__":
    ut.main()
