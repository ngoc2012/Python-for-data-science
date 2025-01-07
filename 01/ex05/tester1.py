import numpy as np
import unittest as ut
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


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

class TestImageFunctions(ut.TestCase):
    def setUp(self):
        """Set up test cases with valid and invalid inputs."""
        # Create a valid RGB image (3x3 pixels for simplicity)
        self.valid_rgb_image = np.array([
            [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
            [[255, 255, 0], [0, 255, 255], [255, 0, 255]],
            [[128, 128, 128], [64, 64, 64], [32, 32, 32]]
        ], dtype=np.uint8)

        # Create invalid inputs
        self.invalid_image_2d = np.array([[255, 0], [0, 255]])  # 2D array
        self.invalid_image_grayscale = np.array([[[128], [64], [32]]], dtype=np.uint8)  # 3D but not RGB
        self.invalid_image_type = "not an array"  # Not a numpy array

    def test_ft_invert(self):
        """Test ft_invert function."""
        # Valid input
        expected_output = 255 - self.valid_rgb_image
        np.testing.assert_array_equal(ft_invert(self.valid_rgb_image), expected_output)

        # Invalid inputs
        with self.assertRaises(TypeError):
            ft_invert(self.invalid_image_2d)
        with self.assertRaises(TypeError):
            ft_invert(self.invalid_image_grayscale)
        with self.assertRaises(TypeError):
            ft_invert(self.invalid_image_type)

    def test_ft_red(self):
        """Test ft_red function."""
        # Valid input
        expected_output = self.valid_rgb_image.copy()
        expected_output[:, :, 1] = 0
        expected_output[:, :, 2] = 0
        np.testing.assert_array_equal(ft_red(self.valid_rgb_image), expected_output)

        # Invalid inputs
        with self.assertRaises(TypeError):
            ft_red(self.invalid_image_2d)
        with self.assertRaises(TypeError):
            ft_red(self.invalid_image_grayscale)
        with self.assertRaises(TypeError):
            ft_red(self.invalid_image_type)

    def test_ft_green(self):
        """Test ft_green function."""
        # Valid input
        expected_output = self.valid_rgb_image.copy()
        expected_output[:, :, 0] = 0
        expected_output[:, :, 2] = 0
        np.testing.assert_array_equal(ft_green(self.valid_rgb_image), expected_output)

        # Invalid inputs
        with self.assertRaises(TypeError):
            ft_green(self.invalid_image_2d)
        with self.assertRaises(TypeError):
            ft_green(self.invalid_image_grayscale)
        with self.assertRaises(TypeError):
            ft_green(self.invalid_image_type)

    def test_ft_blue(self):
        """Test ft_blue function."""
        # Valid input
        expected_output = self.valid_rgb_image.copy()
        expected_output[:, :, 0] = 0
        expected_output[:, :, 1] = 0
        np.testing.assert_array_equal(ft_blue(self.valid_rgb_image), expected_output)

        # Invalid inputs
        with self.assertRaises(TypeError):
            ft_blue(self.invalid_image_2d)
        with self.assertRaises(TypeError):
            ft_blue(self.invalid_image_grayscale)
        with self.assertRaises(TypeError):
            ft_blue(self.invalid_image_type)

    def test_ft_grey(self):
        """Test ft_grey function."""
        # Valid input
        expected_output = np.dot(self.valid_rgb_image[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
        np.testing.assert_array_equal(ft_grey(self.valid_rgb_image), expected_output)

        # Invalid inputs
        with self.assertRaises(TypeError):
            ft_grey(self.invalid_image_2d)
        with self.assertRaises(TypeError):
            ft_grey(self.invalid_image_grayscale)
        with self.assertRaises(TypeError):
            ft_grey(self.invalid_image_type)

if __name__ == '__main__':
    ut.main()
