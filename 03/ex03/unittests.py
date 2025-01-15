import unittest as ut
import subprocess
from ft_calculator import calculator


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


class TestCalculatorClass(ut.TestCase):
    def test_value(self):
        with self.assertRaises(ZeroDivisionError):
            calculator([10.0, 15.0, 20.0]) / 0

    def test_value(self):
        with self.assertRaises(TypeError):
            calculator([10.0, 15.0, 20.0]) + None

    def test_value(self):
        with self.assertRaises(TypeError):
            calculator([10.0, 15.0, 20.0]) + []

if __name__ == "__main__":
    ut.main()
