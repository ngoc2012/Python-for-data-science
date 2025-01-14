import unittest as ut
import subprocess
from S1E9 import Character
# from S1E7 import Baratheon, Lannister
from DiamondTrap import King


class TestAllClass(ut.TestCase):
    def test_tester_output_matches_expected(self):
        result = subprocess.run(['python3', 'tester.py'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        with open('output', 'r') as file:
            expected_output = file.read().strip()
        actual_output = result.stdout.strip()

        self.assertEqual(
            actual_output,
            expected_output,
            "Output of tester.py does not match the expected output.")


class TestKingClass(ut.TestCase):
    def test_value(self):
        with self.assertRaises(TypeError):
            King("Joffrey", None)
    def test_value(self):
        with self.assertRaises(TypeError):
            King("Joffrey", 0)
    def test_value(self):
        with self.assertRaises(TypeError):
            King("Joffrey", [])


if __name__ == "__main__":
    ut.main()
