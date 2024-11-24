from give_bmi import give_bmi, apply_limit


#print(" ========================================== ")
#print("Checking give_bmi function: height")
#weight = [165.3, 38.4]
#height = [2.71]
#height = None
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#height = "smt"
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#print(" ========================================== ")
#print("Checking give_bmi function: weight")
#height = [2.71, 1.15]
#weight = [165.3]
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#weight = [165.3, 0]
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#weight = [165.3, -1]
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#weight = [165.3, None]
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#weight = [165.3,"smt"]
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#weight = "none"
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#weight = None
#try:
#    bmi = give_bmi(height, weight)
#except Exception as e:
#    print(e)
#height = [2.71, 1.15]
#weight = [165.3, 38.4]
#bmi = give_bmi(height, weight)
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

class TestBMIHeight(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            give_bmi(None, [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi("smt", [165.3, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, 0], [165.3, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, -1], [165.3, 38.4])

    def test_size(self):
        with self.assertRaises(TypeError):
            give_bmi([2.71], [165.3, 38.4])

    def test_value(self):
        with self.assertRaises(ValueError):
            give_bmi([2.71, 0], [165.3, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, -1], [165.3, 38.4])

if __name__ == '__main__':
    unittest.main()
