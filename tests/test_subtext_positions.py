import unittest
from main import get_subtext_positions


class TestFindSubtextPositions(unittest.TestCase):

    def test_basic(self):
        text_to_search = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"
        subtext = "Peter"
        expected_output = "Peter 1, 20, 75"
        self.assertEqual(get_subtext_positions(text_to_search, subtext), expected_output)

    def test_case_insensitivity(self):
        text_to_search = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"
        subtext = "PETER"
        expected_output = "PETER 1, 20, 75"
        self.assertEqual(get_subtext_positions(text_to_search, subtext), expected_output)

    def test_no_output(self):
        text_to_search = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"
        subtext = "z"
        expected_output = "z <No Output>"
        self.assertEqual(get_subtext_positions(text_to_search, subtext), expected_output)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            get_subtext_positions(None, "Peter")
        with self.assertRaises(TypeError):
            get_subtext_positions("Peter", None)
        with self.assertRaises(TypeError):
            get_subtext_positions(123, "Peter")
        with self.assertRaises(TypeError):
            get_subtext_positions("Peter", 123)

    def test_empty_inputs(self):
        text_to_search = ""
        subtext = ""
        expected_output = "<No Output>"
        self.assertEqual(get_subtext_positions(text_to_search, subtext), expected_output)

if __name__ == '__main__':
    unittest.main()