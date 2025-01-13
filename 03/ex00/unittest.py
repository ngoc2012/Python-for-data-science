import unittest as ut
from S1E9 import Character, Stark


class TestCharacterClass(ut.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError) as context:
            Character("hodor")  # Passing a string instead of an integer
        
        # Optionally, check the exception message
        self.assertEqual(str(context.exception), "Can't instantiate abstract class Character with abstract method")


class TestCharacterClass(ut.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError) as context:
            Character("hodor")  # Passing a string instead of an integer
        
        # Optionally, check the exception message
        self.assertEqual(str(context.exception), "Can't instantiate abstract class Character with abstract method")
        
if __name__ == "__main__":
    ut.main()
