import unittest
from src.text_cleaner import RedditTextCleaner

class TestRedditTextCleaner(unittest.TestCase):
    """
    Unit tests for the RedditTextCleaner class.

    This test suite verifies the functionality of the RedditTextCleaner class,
    which is responsible for cleaning and preprocessing text data. The tests
    cover various scenarios to ensure the cleaning process works as expected.

    Test Cases:
    - test_basic_cleaning: Tests the cleaning of a string containing mentions,
        URLs, emojis, and hashtags, ensuring only the desired text remains.
    - test_empty_string: Verifies that an empty string input returns an empty string.
    - test_none_input: Ensures that a None input is handled gracefully and returns an empty string.
    - test_numbers_and_special_chars: Tests the cleaning of a string containing
        numbers, special characters, and text, ensuring only the desired content remains.
    """

    def setUp(self):
        self.cleaner = RedditTextCleaner()

    def test_basic_cleaning(self):
        raw_text = "@user Hello World! Visit http://example.com 😊 #hashtag"
        cleaned = self.cleaner.clean(raw_text)
        expected = "hello world visit"
        print("\n[TEST] Input:", raw_text)
        print("[TEST] Cleaned Output:", cleaned)
        print("[TEST] Expected Output:", expected)
        self.assertEqual(cleaned, expected)

    def test_empty_string(self):
        self.assertEqual(self.cleaner.clean(""), "")

    def test_none_input(self):
        self.assertEqual(self.cleaner.clean(None), "")

    def test_numbers_and_special_chars(self):
        raw_text = "12345 $$$%%% hello!!!"
        cleaned = self.cleaner.clean(raw_text)
        expected = "12345 hello"
        print("\n[TEST] Input:", raw_text)
        print("[TEST] Cleaned Output:", cleaned)
        print("[TEST] Expected Output:", expected)
        self.assertEqual(cleaned, expected)

if __name__ == '__main__':
    unittest.main()
