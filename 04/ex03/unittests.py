from io import StringIO
import sys

import random
import pandas as pd
import numpy as np
import unittest as ut
import subprocess


def args_to_list(*args):
    return list(args)


def generate_random_lists(num_lists, min_length, max_length, min_value, max_value):
    random_lists = []
    for _ in range(num_lists):
        length = random.randint(min_length, max_length)
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


# class TestOutputFunction(ut.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.samples = generate_random_lists(100, 1, 100, -1000000, 1000000)

#     def test_mean(self):
#         for input_list in self.samples:
#             with self.subTest(input_list=input_list):
#                 captured_output = StringIO()
#                 sys.stdout = captured_output
#                 ft_statistics(*input_list, toto="mean")
#                 sys.stdout = sys.__stdout__
#                 self.assertEqual(captured_output.getvalue(), panda_mean(input_list))


if __name__ == "__main__":
    ut.main()
