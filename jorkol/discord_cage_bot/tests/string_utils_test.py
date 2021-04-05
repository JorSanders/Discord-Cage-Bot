import unittest

from jorkol.discord_cage_bot.src.string_utils import string_contains_word, cagify_string


class TestStringUtils(unittest.TestCase):
    def test_string_contains_word(self):
        self.assertTrue(string_contains_word("I like dropping cage", ["cage"]))
        self.assertFalse(string_contains_word("I like playing caustic", ["cage"]))

    def test_cagify_string(self):
        self.assertTrue("cage" in cagify_string("one two three four"))
        self.assertEqual("Cage", cagify_string("One"))
        self.assertEqual("cage.", cagify_string("one."))
        self.assertEqual("cage,", cagify_string("one,"))


if __name__ == "__main__":
    unittest.main()
