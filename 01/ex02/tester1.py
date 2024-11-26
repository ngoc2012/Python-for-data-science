import unittest as ut
from load_image import ft_load


class TestLoadPath(ut.TestCase):
    """Test cases for the family input."""

    def test_value(self):
        """Test the type of the family input."""
        with self.assertRaises(ValueError):
            ft_load("dsfsadfdsfsd")
        with self.assertRaises(ValueError):
            ft_load("/home/ngoc/Downloads/meotravaux.mp4")

    def test_type(self):
        """Test the type of the family input."""
        with self.assertRaises(TypeError):
            slice_me(None, 1, -2)


if __name__ == '__main__':
    ut.main()
