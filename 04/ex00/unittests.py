import random
import unittest as ut
import subprocess
from S1E9 import Character, Stark


def args_to_list(*args):
    return list(args)


# Function to generate random lists
def generate_random_lists(num_lists, min_length, max_length, min_value, max_value):
    random_lists = []
    for _ in range(num_lists):
        length = random.randint(min_length, max_length)  # Random length for each list
        random_list = [random.randint(min_value, max_value) for _ in range(length)]
        random_lists.append(random_list)
    return random_lists


class TestAllClass(ut.TestCase):
    def test_tester_output_matches_expected(self):
        result = subprocess.run(['python3', 'tester.py'], 
                                stdout=subprocess.PIPE, 
                                stderr=subprocess.PIPE, 
                                text=True)
        with open('output', 'r') as file:
            expected_output = file.read().strip()
        actual_output = result.stdout.strip()

        self.assertEqual(actual_output, expected_output, 
                         "Output of tester.py does not match the expected output.")


class TestMeanFunction(ut.TestCase):
    samples = generate_random_lists(10, 5, 1000, -1000000, 1000000)

    def test_output(self):
        # import pandas as pd
    # data_series = pd.Series(data)
    # print("Quartile: ", [data_series.quantile(0.25), data_series.quantile(0.75)])
        for input_list, expected in samples:
            with self.subTest(input_list=input_list, expected=expected):
                result = process_list(input_list)
                self.assertEqual(result, expected)
                

if __name__ == "__main__":
    ut.main()
