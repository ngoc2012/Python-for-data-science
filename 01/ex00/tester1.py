from give_bmi import give_bmi, apply_limit


print(" ========================================== ")
print("Checking give_bmi function: height")
weight = [165.3, 38.4]
height = [2.71]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, 0]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, -1]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, "smt"]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, None]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = None
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = "smt"
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
print(" ========================================== ")
print("Checking give_bmi function: weight")
height = [2.71, 1.15]
weight = [165.3]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, 0]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, -1]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3, None]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = [165.3,"smt"]
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = "none"
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
weight = None
try:
    bmi = give_bmi(height, weight)
except Exception as e:
    print(e)
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(" ========================================== ")
print("Checking apply_limit function: limit")
try:
    print(apply_limit(bmi, []))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, [None]))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, None))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, -1))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, 0))
except Exception as e:
    print(e)
try:
    print(apply_limit(bmi, "hello"))
except Exception as e:
    print(e)
print(" ========================================== ")
print("Checking apply_limit function: bmi")
try:
    print(apply_limit([], 0))
except Exception as e:
    print(e)
try:
    print(apply_limit(None, 0))
except Exception as e:
    print(e)
try:
    print(apply_limit([None], 0))
except Exception as e:
    print(e)
try:
    print(apply_limit([-1], 0))
except Exception as e:
    print(e)

import numpy as np

data = np.array(None)
print(data)
print("Data type of the array:", data.dtype)
data = np.array("smt")
print(data)
print("Data type of the array:", data.dtype)
data = np.array([])
print(data)
print("Data type of the array:", data.dtype)



import unittest

class TestHeight(unittest.TestCase):

    def test_positive_value(self):
        self.assertEqual(ensure_positive(5), 5)

    def test_size(self):
        with self.assertRaises(TypeError):
            ensure_positive(0)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            ensure_positive(-5)

if __name__ == '__main__':
    unittest.main()
