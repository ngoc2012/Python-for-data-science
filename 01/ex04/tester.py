import unittest as ut
from load_image import rotate_image, ft_load


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
        with self.assertRaises(PermissionError):
            zoom_image("unreadable", 0, 0, 0, 0)
        with self.assertRaises(TypeError):
            zoom_image("bigfile", 0, 0, 0, 0)

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

    def test_index_value(self):
        """Test the value of the path input."""
        with self.assertRaises(IndexError):
            zoom_image("animal.jpeg", 0, 0, 0, 100)
        with self.assertRaises(IndexError):
            zoom_image("animal.jpeg", 0, 100, 0, 0)
        with self.assertRaises(IndexError):
            zoom_image("animal.jpeg", 10, 0, 0, 100)
        with self.assertRaises(IndexError):
            zoom_image("animal.jpeg", 0, 100, 10, 0)
        with self.assertRaises(IndexError):
            zoom_image("animal.jpeg", -1, 0, 0, 100)

    def test_index_type(self):
        """Test the value of the path input."""
        with self.assertRaises(TypeError):
            zoom_image("animal.jpeg", None, 100, 0, 100)
        with self.assertRaises(TypeError):
            zoom_image("animal.jpeg", 0, None, 0, 100)
        with self.assertRaises(TypeError):
            zoom_image("animal.jpeg", 0, 100, None, 100)


class TestLoadPath(ut.TestCase):
    """Test ft_load function."""

    def test_value(self):
        """Test the value of the path input."""
        with self.assertRaises(FileNotFoundError):
            ft_load("dsfsadfdsfsd")
        with self.assertRaises(PermissionError):
            ft_load("unreadable")
        with self.assertRaises(TypeError):
            ft_load("empty.jpg")
        with self.assertRaises(TypeError):
            ft_load("meotravaux.mp4")
        with self.assertRaises(TypeError):
            ft_load("bigfile")

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
