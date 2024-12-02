import unittest as ut
from load_image import ft_load
from PIL import Image


class TestLoadPath(ut.TestCase):
    """Test ft_load function."""

    def test_value(self):
        """Test the value of the path input."""
        with self.assertRaises(FileNotFoundError):
            ft_load("dsfsadfdsfsd")
        with self.assertRaises(TypeError):
            ft_load("empty.jpg")
        with self.assertRaises(TypeError):
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
