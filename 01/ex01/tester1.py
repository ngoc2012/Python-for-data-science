import unittest as ut
from array2D import slice_me


class TestSlideOutput(ut.TestCase):
    """Test cases for the output of the slide_me function."""

    def test_output(self):
        """Test the output of the slide_me function."""
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
    """Test cases for the family input."""

    def test_type(self):
        """Test the type of the family input."""
        with self.assertRaises(TypeError):
            slice_me(
                [[1.80, 78.4],
                 [2.15, 102.7],
                 [2.10, 98.5],
                 [1.88, 75.2]]
            , 1, -2)

    def test_size(self):
        """Test the size of the family input."""
        with self.assertRaises(TypeError):
            slice_me(
                [[1.80, 78.4],
                 [2.15],
                 [2.10, 98.5],
                 [1.88, 75.2]]
            , 1, -2)


class TestSlideStart(ut.TestCase):
    """Test cases for the family input."""

    def test_type(self):
        """Test the type of the family input."""
        with self.assertRaises(TypeError):
            slice_me(
                [[1.80, 78.4],
                 [2.15, 102.7],
                 [2.10, 98.5],
                 [1.88, 75.2]]
            , 1, -2)

    def test_value(self):
        """Test the type of the family input."""
        with self.assertRaises(TypeError):
            slice_me(
                [[1.80, 78.4],
                 [2.15, 102.7],
                 [2.10, 98.5],
                 [1.88, 75.2]]
            , 1, -2)


if __name__ == '__main__':
    ut.main()
