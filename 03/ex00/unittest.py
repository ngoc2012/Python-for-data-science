import unittest as ut
from S1E9 import Character, Stark


class TestCharacterClass(ut.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError) as context:
            function_to_test("not an integer")  # Passing a string instead of an integer
        
        # Optionally, check the exception message
        self.assertEqual(str(context.exception), "Expected an integer.")

    def test_nonexistent_file(self):
        """Test handling of a nonexistent file."""
        result = load("nonexistent.csv")
        self.assertIsNone(result)

    def test_invalid_path_type(self):
        """Test handling of an invalid path type."""
        result = load(12345)
        self.assertIsNone(result)

    def test_empty_file(self):
        """Test handling of an empty CSV file."""
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

        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)
        self.assertListEqual(
            list(result.columns),
            ["country", "1800", "1801", "1802"]
            )

    def test_file_with_invalid_format(self):
        """Test handling of a CSV file with an invalid format."""
        invalid_file = "invalid.csv"

        result = load(invalid_file)
        self.assertIsNone(result)

    def tearDown(self):
        """Clean up test files after each test."""
        test_files = ["test_valid.csv", "empty.csv", "header_only.csv"]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)


if __name__ == "__main__":
    ut.main()
