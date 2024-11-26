import unittest as ut
from load_image import ft_load


class TestLoadPath(ut.TestCase):
    """Test ft_load function."""

    def test_value(self):
        """Test the value of the path input."""
        with self.assertRaises(ValueError):
            ft_load("dsfsadfdsfsd")
        with self.assertRaises(ValueError):
            ft_load("/home/ngoc/Downloads/meotravaux.mp4")

    def test_type(self):
        """Test the type of the path input."""
        with self.assertRaises(TypeError):
            ft_load(None)
        with self.assertRaises(TypeError):
            ft_load({})
        with self.assertRaises(TypeError):
            ft_load([])
        with self.assertRaises(TypeError):
            ft_load(())
        with self.assertRaises(TypeError):
            ft_load(0)


if __name__ == '__main__':
    ut.main()
