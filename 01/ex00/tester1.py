import unittest as ut
from give_bmi import give_bmi, apply_limit

class TestBMIOutput(ut.TestCase):
    """Test cases for the output of the give_bmi function."""

    def test_output(self):
        """Test the output of the give_bmi function with valid inputs."""
        self.assertEqual(
            give_bmi(
                [2.71, 1.15],
                [165.3, 38.4]
            ),
            [22.507863455018317, 29.0359168241966]
        )
        self.assertEqual(give_bmi([], []), [])

class TestBMIHeight(ut.TestCase):
    """Test cases for the height input of the give_bmi function."""

    def test_type(self):
        """Test the type of the height input."""
        with self.assertRaises(TypeError):
            give_bmi(None, [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi("smt", [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi({}, [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi((), [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi([2.71, None], [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi([2.71, "smt"], [165.3, 38.4])

    def test_size(self):
        """Test the size of the height input."""
        with self.assertRaises(TypeError):
            give_bmi([2.71], [165.3, 38.4])

    def test_value(self):
        """Test the value of the height input."""
        with self.assertRaises(ValueError):
            give_bmi([2.71, 0], [165.3, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, -1], [165.3, 38.4])

class TestBMIWeight(ut.TestCase):
    """Test cases for the weight input of the give_bmi function."""

    def test_type(self):
        """Test the type of the weight input."""
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], None)
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], "smt")
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], {})
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [])
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [165.3, None])
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [165.3, "smt"])

    def test_size(self):
        """Test the size of the weight input."""
        with self.assertRaises(TypeError):
            give_bmi([2.71, 1.15], [38.4])

    def test_value(self):
        """Test the value of the weight input."""
        with self.assertRaises(ValueError):
            give_bmi([2.71, 1.15], [0, 38.4])
        with self.assertRaises(ValueError):
            give_bmi([2.71, 1.15], [165.3, -1])

class TestApplyLimitOutput(ut.TestCase):
    """Test cases for the output of the apply_limit function."""

    def test_output(self):
        """Test the output of the apply_limit function with valid inputs."""
        self.assertEqual(
            apply_limit(
                [22.507863455018317, 29.0359168241966],
                26
            ),
            [False, True]
        )
        self.assertEqual(
            apply_limit(
                [22.507863455018317, 29.0359168241966],
                0
            ),
            [True, True]
        )
        self.assertEqual(
            apply_limit(
                [22.507863455018317, 29.0359168241966],
                -1
            ),
            [True, True]
        )
        self.assertEqual(apply_limit([], 26), [])

class TestApplyLimitBMI(ut.TestCase):
    """Test cases for the BMI input of the apply_limit function."""

    def test_type(self):
        """Test the type of the BMI input."""
        with self.assertRaises(TypeError):
            apply_limit(None, 26)
        with self.assertRaises(TypeError):
            apply_limit("smt", 26)
        with self.assertRaises(TypeError):
            apply_limit({}, 26)
        #with self.assertRaises(TypeError):
        #    apply_limit((), 26)
        with self.assertRaises(TypeError):
            apply_limit([None], 26)
        with self.assertRaises(TypeError):
            apply_limit(["smt"], 26)
        with self.assertRaises(TypeError):
            apply_limit([{}], 26)
        #with self.assertRaises(TypeError):
        #    apply_limit([()], 26)
        with self.assertRaises(TypeError):
            apply_limit([-1], 26)

class TestApplyLimitLimit(ut.TestCase):
    """Test cases for the limit input of the apply_limit function."""

    def test_type(self):
        """Test the type of the limit input."""
        with self.assertRaises(TypeError):
            apply_limit([22.507863455018317, 29.0359168241966], None)
        with self.assertRaises(TypeError):
            apply_limit([22.507863455018317, 29.0359168241966], [])
        with self.assertRaises(TypeError):
            apply_limit([22.507863455018317, 29.0359168241966], "smt")

if __name__ == '__main__':
    ut.main()
