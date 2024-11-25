from give_bmi import give_bmi, apply_limit


#print(" ========================================== ")
#print("Checking apply_limit function: limit")
#try:
#    print(apply_limit(bmi, []))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit(bmi, [None]))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit(bmi, None))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit(bmi, -1))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit(bmi, 0))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit(bmi, "hello"))
#except Exception as e:
#    print(e)
#print(" ========================================== ")
#print("Checking apply_limit function: bmi")
#try:
#    print(apply_limit([], 0))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit(None, 0))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit([None], 0))
#except Exception as e:
#    print(e)
#try:
#    print(apply_limit([-1], 0))
#except Exception as e:
#    print(e)
#
#import numpy as np
#
#data = np.array(None)
#print(data)
#print("Data type of the array:", data.dtype)
#data = np.array("smt")
#print(data)
#print("Data type of the array:", data.dtype)
#data = np.array([])
#print(data)
#print("Data type of the array:", data.dtype)



import unittest

class TestBMIOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(give_bmi([2.71, 1.15], [165.3, 38.4]), [22.507863455018317, 29.0359168241966])
        self.assertEqual(give_bmi([], []), [])

class TestBMIHeight(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            give_bmi(None, [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi("smt", [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi([2.71, None], [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi([2.71, "smt"], [165.3, 38.4])

    def test_size(self):
        with self.assertRaises(TypeError):
            give_bmi([2.71], [165.3, 38.4])

    def test_value(self):
        with self.assertRaises(ValueError):
            give_bmi([2.71, 0], [165.3, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, -1], [165.3, 38.4])

class TestBMIWeight(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], None)
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], "smt")
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [165.3, None])
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [165.3, "smt"])

    def test_size(self):
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [38.4])

    def test_value(self):
        with self.assertRaises(ValueError):
            give_bmi([2.71, 1.15], [0, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, 1.15], [165.3, -1])

class TestApplyLimitOutput(unittest.TestCase):

    def test(self):
        self.assertEqual(apply_limit([22.507863455018317, 29.0359168241966], 26)
        self.assertEqual(apply_limit([], 26))

class TestApplyLimitBMI(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            apply_limit([22.507863455018317, 29.0359168241966], None)
            apply_limit([22.507863455018317, 29.0359168241966], [])
            apply_limit([22.507863455018317, 29.0359168241966], "smt")


if __name__ == '__main__':
    unittest.main()
