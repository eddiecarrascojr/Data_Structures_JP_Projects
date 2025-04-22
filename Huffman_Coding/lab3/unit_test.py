import unittest
from io import StringIO
import sys

try:
    from huffman_logic import (HuffmanNode, MinHeap,
                               build_huffman_tree_custom_heap,
                               generate_huffman_codes, encode_huffman,
                               decode_huffman)
    print("Imported Huffman logic from huffman_node.py")
except ImportError:
    print("Could not import from huffman_logic.py. Ensure the file exists.")
    print("You might need to paste the classes/functions directly below.")
    sys.exit("Required Huffman logic not found.") # Stop tests if logic isn't available

# --- Unit Test Class ---
class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        """Set up common data structures for tests."""
        # Small frequency table for basic tests
        self.freq_table_small = {'a': 1, 'b': 2, 'c': 3}
        # Build tree and codes for the small table
        self.root_small = build_huffman_tree_custom_heap(self.freq_table_small)
        self.codes_small = generate_huffman_codes(self.root_small)
        # Manually verify expected codes (may vary based on tie-breaks)
        # Example: {'c': '0', 'a': '10', 'b': '11'} or {'c': '1', 'a': '00', 'b': '01'}
        # The tests below will rely on consistency rather than hardcoded values

        # Larger frequency table for more complex tests
        self.freq_table_larger = {
            'a': 19, 'b': 16, 'c': 17, 'd': 11, 'e': 42, 'f': 12, 'g': 14,
            'h': 17, 'i': 16, 'j': 5, 'k': 10, 'l': 20, 'm': 19, 'n': 24,
            'o': 18, 'p': 13, 'q': 1, 'r': 25, 's': 35, 't': 25, 'u': 15,
            'v': 5, 'w': 21, 'x': 2, 'y': 8, 'z': 3
        }
        self.root_larger = build_huffman_tree_custom_heap(self.freq_table_larger)
        self.codes_larger = generate_huffman_codes(self.root_larger)

        # Single character table
        self.freq_single = {'z': 10}
        self.root_single = build_huffman_tree_custom_heap(self.freq_single)
        self.codes_single = generate_huffman_codes(self.root_single)

    # --- HuffmanNode Tests ---
    def test_huffman_node_creation(self):
        node = HuffmanNode('x', 99)
        self.assertEqual(node.char, 'x')
        self.assertEqual(node.freq, 99)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_huffman_node_comparison(self):
        node_low = HuffmanNode('l', 10)
        node_high = HuffmanNode('h', 50)
        node_low2 = HuffmanNode('l2', 10)
        self.assertTrue(node_low < node_high)
        self.assertFalse(node_high < node_low)
        # Comparison is based on frequency only for heap ordering
        self.assertFalse(node_low < node_low2)
        self.assertFalse(node_low2 < node_low)
        # Equality check
        self.assertEqual(node_low, node_low2)
        self.assertNotEqual(node_low, node_high)

    # --- MinHeap Tests ---
    def test_min_heap_operations(self):
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        self.assertEqual(len(heap), 0)
        self.assertIsNone(heap.extract_min())

        n1 = HuffmanNode('c', 3)
        n2 = HuffmanNode('a', 1)
        n3 = HuffmanNode('b', 2)

        heap.insert(n1) # [c:3]
        heap.insert(n2) # [a:1, c:3]
        heap.insert(n3) # [a:1, c:3, b:2] -> heapify -> [a:1, c:3, b:2] -> [a:1, b:2, c:3] after heapify

        self.assertEqual(len(heap), 3)
        self.assertFalse(heap.is_empty())

        # Extract in ascending order of frequency
        extracted1 = heap.extract_min()
        self.assertEqual(extracted1.char, 'a')
        self.assertEqual(extracted1.freq, 1)
        self.assertEqual(len(heap), 2)

        extracted2 = heap.extract_min()
        self.assertEqual(extracted2.char, 'b')
        self.assertEqual(extracted2.freq, 2)
        self.assertEqual(len(heap), 1)

        extracted3 = heap.extract_min()
        self.assertEqual(extracted3.char, 'c')
        self.assertEqual(extracted3.freq, 3)
        self.assertEqual(len(heap), 0)
        self.assertTrue(heap.is_empty())

        self.assertIsNone(heap.extract_min()) # Empty again

    # --- Tree Building Tests ---
    def test_build_tree_empty_input(self):
        root = build_huffman_tree_custom_heap({})
        self.assertIsNone(root)

    def test_build_tree_single_node(self):
        # setUp already builds self.root_single
        self.assertIsNotNone(self.root_single)
        self.assertIsNone(self.root_single.char, "Root of single-char tree should be internal")
        self.assertEqual(self.root_single.freq, 10)
        self.assertIsNotNone(self.root_single.left, "Single char node should be child (e.g., left)")
        self.assertIsNone(self.root_single.right, "Single char tree parent should have only one child connection used")
        if self.root_single.left: # Check the actual leaf
            self.assertEqual(self.root_single.left.char, 'z')
            self.assertEqual(self.root_single.left.freq, 10)

    def test_build_tree_properties_small(self):
        # For {'a': 1, 'b': 2, 'c': 3} -> Total Freq = 6
        self.assertIsNotNone(self.root_small)
        self.assertEqual(self.root_small.freq, 6, "Root freq should be sum of all freqs")
        self.assertIsNone(self.root_small.char, "Root node should be internal")
        self.assertIsNotNone(self.root_small.left)
        self.assertIsNotNone(self.root_small.right)

    def test_generate_codes_single(self):
        self.assertEqual(self.codes_single, {'z': '0'})

    def test_generate_codes_prefix_property(self):
        # No code should be a prefix of another code
        codes_list = list(self.codes_larger.values())
        for i, code1 in enumerate(codes_list):
            for j, code2 in enumerate(codes_list):
                if i != j:
                    self.assertFalse(code1.startswith(code2), f"Code '{code1}' is prefix of '{code2}' or vice versa")
                    self.assertFalse(code2.startswith(code1), f"Code '{code2}' is prefix of '{code1}' or vice versa")

    def test_generate_codes_all_chars_present(self):
        # Ensure all characters from the frequency table have a code
        self.assertEqual(set(self.codes_larger.keys()), set(self.freq_table_larger.keys()))

    def test_encode_simple(self):
        # Use the small table/codes
        message = "cab"
        expected_encoding = self.codes_small['c'] + self.codes_small['a'] + self.codes_small['b']
        encoded = encode_huffman(message, self.codes_small)
        self.assertEqual(encoded, expected_encoding)

    def test_encode_empty_string(self):
        encoded = encode_huffman("", self.codes_small)
        self.assertEqual(encoded, "")

    def test_encode_unknown_character(self):
        message = "cat" # 't' is not in self.codes_small
        # Capture stdout to check for error message
        captured_output = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            encoded = encode_huffman(message, self.codes_small)
            self.assertIsNone(encoded, "Encoding should fail if char not in codes")
            output = captured_output.getvalue()
            self.assertIn("Character 't' not found", output)
        finally:
            sys.stdout = original_stdout # Restore stdout

    def test_decode_simple(self):
        # Use the small table/codes/tree
        encoded = self.codes_small['c'] + self.codes_small['a'] + self.codes_small['b']
        decoded = decode_huffman(encoded, self.root_small)
        self.assertEqual(decoded, "cab")

    def test_decode_single_char_message(self):
        # Use single char table/codes/tree
        encoded = "0000" # Corresponds to "zzzz"
        decoded = decode_huffman(encoded, self.root_single)
        self.assertEqual(decoded, "zzzz")

    def test_decode_empty_string(self):
        decoded = decode_huffman("", self.root_small)
        self.assertEqual(decoded, "")

    def test_decode_invalid_bits(self):
        # Use small table
        valid_code = self.codes_small['a']
        encoded_invalid = valid_code + "2" + self.codes_small['b'] # Contains '2'
        # Capture stdout for warning
        captured_output = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            decoded = decode_huffman(encoded_invalid, self.root_small)
            # Expect decoding to work for valid parts, skipping invalid
            self.assertEqual(decoded, "ab", "Decoder should skip invalid bits")
            output = captured_output.getvalue()
            self.assertIn("Invalid character '2'", output)
        finally:
            sys.stdout = original_stdout

    def test_decode_incomplete_final_code(self):
        # Find a code longer than 1 bit, e.g., 'a' or 'b' from small table
        code_a = self.codes_small.get('a')
        if code_a and len(code_a) > 1:
            incomplete_code = code_a[:-1] # All but the last bit
            # Capture stdout for warning
            captured_output = StringIO()
            original_stdout = sys.stdout
            try:
                sys.stdout = captured_output
                decoded = decode_huffman(incomplete_code, self.root_small)
                self.assertEqual(decoded, "", "Incomplete code should not yield char")
                output = captured_output.getvalue()
                self.assertIn("finished mid-character traversal", output)
            finally:
                sys.stdout = original_stdout

    def test_round_trip_small_message(self):
        message = "abacaba"
        encoded = encode_huffman(message, self.codes_small)
        self.assertIsNotNone(encoded)
        decoded = decode_huffman(encoded, self.root_small)
        self.assertEqual(decoded, message)

    def test_round_trip_larger_message(self):
        message = "thequickbrownfoxjumpsoverthelazydog"
        encoded = encode_huffman(message, self.codes_larger)
        self.assertIsNotNone(encoded)
        decoded = decode_huffman(encoded, self.root_larger)
        self.assertEqual(decoded, message)

    def test_round_trip_repeated_chars(self):
        message = "sssssaaaaabbbbbccccc" # Test with repeated chars
        encoded = encode_huffman(message, self.codes_larger)
        self.assertIsNotNone(encoded)
        decoded = decode_huffman(encoded, self.root_larger)
        self.assertEqual(decoded, message)

    def test_round_trip_all_chars_larger_table(self):
        message = "".join(sorted(self.freq_table_larger.keys())) # String with all chars
        encoded = encode_huffman(message, self.codes_larger)
        self.assertIsNotNone(encoded)
        decoded = decode_huffman(encoded, self.root_larger)
        self.assertEqual(decoded, message)


# --- Run the tests ---
if __name__ == '__main__':
    # Use exit=False if running in interactive environments like Jupyter
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)