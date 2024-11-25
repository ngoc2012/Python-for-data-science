import unittest
from give_bmi import give_bmi, apply_limit

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
        self.assertEqual(apply_limit([22.507863455018317, 29.0359168241966], 26), [False, True])
        self.assertEqual(apply_limit([22.507863455018317, 29.0359168241966], 0), [True, True])
        self.assertEqual(apply_limit([22.507863455018317, 29.0359168241966], -1), [True, True])
        self.assertEqual(apply_limit([], 26), [])

class TestApplyLimitBMI(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(apply_limit(None, 26))
            self.assertEqual(apply_limit("smt", 26))
            self.assertEqual(apply_limit({}, 26))
            self.assertEqual(apply_limit((), 26))
            self.assertEqual(apply_limit([None], 26))
            self.assertEqual(apply_limit(["smt"], 26))
            self.assertEqual(apply_limit([{}], 26))
            self.assertEqual(apply_limit([()], 26))
            self.assertEqual(apply_limit([-1], 26))

class TestApplyLimitLimit(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            apply_limit([22.507863455018317, 29.0359168241966], None)
            apply_limit([22.507863455018317, 29.0359168241966], [])
            apply_limit([22.507863455018317, 29.0359168241966], "smt")


if __name__ == '__main__':
    unittest.main()
