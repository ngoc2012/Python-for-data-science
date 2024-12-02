import unittest as ut
from load_image import zoom_image, ft_load


class TestZoomImage(ut.TestCase):
    """Test zoom_image function."""

    def test_file_name(self):
        """Test the value of the path input."""
        with self.assertRaises(FileNotFoundError):
            zoom_image("dsfsadfdsfsd", 0, 0, 0, 0)

    def test_file_format(self):
        """Test the type of the path input."""
        with self.assertRaises(TypeError):
            zoom_image("meotravaux.mp4", 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            zoom_image("animal_empty.jpeg", 0, 0, 0, 0)

    def test_file_type(self):
        """Test the type of the path input."""
        with self.assertRaises(TypeError):
            zoom_image(None, 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            zoom_image({}, 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            zoom_image([], 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            zoom_image((), 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            zoom_image(0, 0, 0, 0, 0)

    def test_index(self):
        """Test the value of the path input."""
        with self.assertRaises(IndexError):
            zoom_image("animal.jpeg", -1, 0, 0, 0)


#class TestZoomImage(ut.TestCase):
#    """Test ft_load function."""
#
#    def test_value(self):
#        """Test the value of the path input."""
#        with self.assertRaises(FileNotFoundError):
#            ft_load("dsfsadfdsfsd")
#        with self.assertRaises(TypeError):
#            ft_load("/home/ngoc/Downloads/meotravaux.mp4")
#
#    def test_type(self):
#        """Test the type of the path input."""
#        with self.assertRaises(TypeError):
#            ft_load(None)
#        with self.assertRaises(TypeError):
#            ft_load({})
#        with self.assertRaises(TypeError):
#            ft_load([])
#        with self.assertRaises(TypeError):
#            ft_load(())
#        with self.assertRaises(TypeError):
#            ft_load(0)


if __name__ == '__main__':
    ut.main()
