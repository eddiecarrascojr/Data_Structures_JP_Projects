import unittest
from prefix_to_postfix import PrefixToPostfix
# Assuming you saved the class in a file named prefix_to_postfix.py
# No time for unittest on PostfixToPrefix class.
class TestPrefixToPostfix(unittest.TestCase):
    def setUp(self):
        self.converter = PrefixToPostfix()

    def test_basic_cases(self) -> None:
        """
        :return: results of simple cases results
        """
        # these are cases used in previous homework assignment
        test_cases = [
            ("-+ABC", "AB+C-"),
            ("-A+BC", "ABC+-"),
            ("$+-ABC+D-EF", "AB-C+DEF-+$"),
            ("/A+BC +C*BA", "ABC+/"),
        ]

        for prefix, expected in test_cases:
            with self.subTest(prefix=prefix):
                self.assertEqual(self.converter.convert(prefix), expected)
                print("Test Case {} passed".format(expected))

    def test_edge_cases(self) -> None:
        """
        :return: results of edge cases results
        """
        test_cases = [
            ("A", "A"),  # Single operand
            ("", ""),  # Empty string
            (" +AB ", "AB+"),  # Whitespace
            ("ABA", "A")
        ]

        for prefix, expected in test_cases:
            with self.subTest(prefix=prefix):
                self.assertEqual(self.converter.convert(prefix), expected)
                print("Test Case {} passed".format(expected))


if __name__ == "__main__":
    unittest.main()