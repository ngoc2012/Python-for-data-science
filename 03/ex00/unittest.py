import unittest as ut
from S1E9 import Character, Stark


class TestStarkClass(ut.TestCase):
    def test_tester_output_matches_expected(self):
        # Command to run the tester.py script directly
        result = subprocess.run(['python3', 'tester.py'], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                text=True)
        with open('output', 'r') as file:
            expected_output = file.read().strip()
        actual_output = result.stdout.strip()

        self.assertEqual(actual_output, expected_output, 
                         "Output of tester.py does not match the expected output.")


class TestCharacterClass(ut.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError) as context:
            Character("hodor")
        self.assertEqual(str(context.exception), "Can't instantiate abstract class Character with abstract method")

if __name__ == "__main__":
    ut.main()
