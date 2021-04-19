import unittest

from jorkol.discord_cage_bot.src.string_utils import (
    string_contains_word,
    cagify_string,
    cagify_word,
    is_to_be_verb,
    is_cagifyable,
    is_cage,
    strip_non_alpha,
    is_signal_word,
)


class TestStringUtils(unittest.TestCase):
    def test_string_contains_word(self):
        self.assertTrue(string_contains_word("I like dropping cage", ["cage"]))
        self.assertFalse(string_contains_word("I like playing caustic", ["cage"]))

    def test_cagify_string(self):
        self.assertTrue("cage" in cagify_string("one two three four"))
        self.assertEqual("Cage", cagify_string("Be"))
        self.assertEqual("Cage", cagify_string("Cage"))
        # 1/1024 chance to fail this test
        self.assertEqual("Be cage", cagify_string("Be happy"))
        self.assertEqual("Cage!", cagify_string("Hello!"))

    def test_cagify_word(self):
        self.assertEqual("cage", cagify_word("one"))
        self.assertEqual("Cage", cagify_word("One"))
        self.assertEqual("cage.", cagify_word("one."))
        self.assertEqual("caged", cagify_word("walked"))
        self.assertEqual("caging", cagify_word("walking"))
        self.assertEqual("cagism", cagify_word("elitism"))
        self.assertEqual("cage", cagify_word("cage"))
        self.assertEqual("cage!", cagify_word("!"))
        self.assertEqual("cage", cagify_word(""))

    def test_is_to_be_verb(self):
        self.assertTrue(is_to_be_verb("be"))
        self.assertTrue(is_to_be_verb("is"))
        self.assertTrue(is_to_be_verb("am"))
        self.assertTrue(is_to_be_verb("are"))
        self.assertTrue(is_to_be_verb("was"))
        self.assertTrue(is_to_be_verb("were"))
        self.assertTrue(is_to_be_verb("Were"))
        self.assertTrue(is_to_be_verb("were!"))
        self.assertTrue(is_to_be_verb("#were"))
        self.assertFalse(is_to_be_verb("drop"))

    def test_is_cage(self):
        self.assertTrue(is_cage("cage"))
        self.assertTrue(is_cage("caged"))
        self.assertTrue(is_cage("Cage"))
        self.assertTrue(is_cage("cage!"))
        self.assertFalse(is_cage("caustic"))

    def test_is_cagifyable(self):
        self.assertFalse(is_cagifyable("cage"))
        self.assertFalse(is_cagifyable("is"))
        self.assertFalse(is_cagifyable("but"))
        self.assertTrue(is_cagifyable("caustic"))

    def test_strip_non_alpha(self):
        self.assertEqual("cage", strip_non_alpha("cage!"))
        self.assertEqual("cage", strip_non_alpha(" cage"))
        self.assertEqual("cage", strip_non_alpha("ca@ge"))
        self.assertEqual("", strip_non_alpha("!"))
        self.assertEqual("", strip_non_alpha(""))

    def test_is_signal_word(self):
        self.assertFalse(is_signal_word("cage"))
        self.assertTrue(is_signal_word("but"))
        self.assertFalse(is_signal_word(""))


if __name__ == "__main__":
    unittest.main()
