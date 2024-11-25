import unittest as ut
from array2D import slice_me


class TestSlideOutput(ut.TestCase):
    """Test cases for the output of the give_bmi function."""

    def test_output(self):
        """Test the output of the give_bmi function with valid inputs."""
        self.assertEqual(
            slice_me(
                [[1.80, 78.4],
                 [2.15, 102.7],
                 [2.10, 98.5],
                 [1.88, 75.2]]
            , 0, 2),
            [[1.8, 78.4], [2.15, 102.7]]
        )
        self.assertEqual(
            slice_me(
                [[1.80, 78.4],
                 [2.15, 102.7],
                 [2.10, 98.5],
                 [1.88, 75.2]]
            , 1, -2),
            [[2.15, 102.7]]
        )


class TestSlideFamily(ut.TestCase):
    """Test cases for the height input of the give_bmi function."""

    def test_type(self):
        """Test the type of the family input."""
        with self.assertRaises(TypeError):
            give_bmi(None, [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi("smt", [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi({}, [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi((), [165.3, 38.4])
        with self.assertRaises(TypeError):
            give_bmi([[2.71], [1.15]], [165.3, 38.4])
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


if __name__ == '__main__':
    ut.main()
