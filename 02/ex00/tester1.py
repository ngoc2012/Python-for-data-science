import unittest as ut
import numpy as np
from load_csv import load

class TestLoadFunction(ut.TestCase):
    def test_valid_file(self):
        """Test loading a valid CSV file."""
        # Prepare a test CSV file
        test_file = "test_valid.csv"
        with open(test_file, "w") as f:
            f.write("country,1800,1801,1802\n")
            f.write("Afghanistan,28.2,28.2,28.2\n")
            f.write("Albania,29.2,29.3,29.4\n")
        
        # Call the function and verify results
        result = load(test_file)
        expected = np.array([['Afghanistan', 28.2, 28.2, 28.2],
                             ['Albania', 29.2, 29.3, 29.4]], dtype=object)
        np.testing.assert_array_equal(result, expected)

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
        self.assertEqual(result.shape, (0,))  # Should return an empty array

    def test_file_with_invalid_format(self):
        """Test handling of a CSV file with an invalid format."""
        invalid_file = "invalid.csv"
        with open(invalid_file, "w") as f:
            f.write("not,a,csv,file\n")
        
        result = load(invalid_file)
        self.assertIsNone(result)

if __name__ == "__main__":
    ut.main()

