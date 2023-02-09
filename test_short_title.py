import unittest
from short_title import short_title

class TestShortTitle(unittest.TestCase):
    def test_positive(self):
        # Positive test case, with a title that is short enough
        title = "Volvo released a new car"
        length = 25
        expected_output = "Volvo released a new car"
        self.assertEqual(short_title(title, length), expected_output)

        # Positive test case, with a title that needs to be shortened
        title = "Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be sold in New York only"
        length = 25
        expected_output = "Volvo released a new..."
        self.assertEqual(short_title(title, length), expected_output)

    def test_negative(self):
        # Negative test case, with a length that is less than or equal to 0
        title = "Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be sold in New York only"
        length = 0
        expected_output = "..."
        self.assertEqual(short_title(title, length), expected_output)

        # Negative test case, with a length that is less than or equal to 3
        title = "Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be sold in New York only"
        length = 3
        expected_output = "..."
        self.assertEqual(short_title(title, length), expected_output)

        # Negative test case, with a negative length value
        title = "Volvo released a new car with the following spec: V6 236HP. It will cost $22647 and going to be sold in New York only"
        length = -3
        expected_output = "..."
        self.assertEqual(short_title(title, length), expected_output)

    def test_i18n(self):
        # Internationalization test case, with a title containing non-ASCII characters
        title = "Volvo lanzó un nuevo coche con las siguientes especificaciones: V6 236HP. Costará $22647 y se venderá solo en Nueva York"
        length = 25
        expected_output = "Volvo lanzó un nuevo..."
        self.assertEqual(short_title(title, length), expected_output)

    def test_l10n(self):
        # Localization test case, with a title containing characters from a different language/script
        title = "वोल्वो नया गाड़ी जारी किया है"
        length = 25
        expected_output = "वोल्वो नया गाड़ी जारी..."
        self.assertEqual(short_title(title, length), expected_output)

    def test_destructive(self):
        # Destructive test case, with a title that consists of only spaces
        title = "   "
        length = 25
        expected_output = "Title cannot be empty or consist of only spaces."
        self.assertEqual(short_title(title, length), expected_output)

if __name__ == '__main__':
    unittest.main()
