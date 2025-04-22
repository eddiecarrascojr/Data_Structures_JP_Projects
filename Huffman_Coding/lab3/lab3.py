from lab3.huffman_node import MinHeap, HuffmanNode

def build_huffman_tree_custom_heap(freq_table):
    """
    Builds a Huffman Tree from a frequency table using the custom MinHeap.
    Args: freq_table (dict): A dictionary mapping characters to frequencies.
    Returns:  HuffmanNode: The root node of the Huffman Tree, or None if input is empty.
    """
    if not freq_table:
        return None

    # Initialize the custom MinHeap
    priority_queue = MinHeap()

    # Create leaf nodes and insert them into the heap
    for char, freq in freq_table.items():
        node = HuffmanNode(char, freq)
        priority_queue.insert(node)

    # Handle edge case: only one unique character in the input
    if len(priority_queue) == 1:
        lonely_node = priority_queue.extract_min()
        # Create a dummy parent node to maintain tree structure for encoding/decoding
        # This ensures even a single character gets a code (e.g., '0')
        internal_node = HuffmanNode(None, lonely_node.freq)
        internal_node.left = lonely_node
        priority_queue.insert(internal_node) # Put the parent back into the 'heap'

    # Merge nodes until only the root node remains in the heap
    while len(priority_queue) > 1:
        # Extract the two nodes with the smallest frequencies
        left_node = priority_queue.extract_min()
        right_node = priority_queue.extract_min()

        # This check should ideally not fail if len > 1, but good practice
        if left_node is None or right_node is None:
            raise RuntimeError("Heap failed. please retry")

        # Create a new internal node (parent)
        merged_freq = left_node.freq + right_node.freq
        internal_node = HuffmanNode(None, merged_freq) # Internal nodes have no char
        internal_node.left = left_node
        internal_node.right = right_node

        # Insert the new internal node back into the heap
        priority_queue.insert(internal_node)

    # The last remaining node in the heap is the root of the Huffman tree
    return priority_queue.extract_min() if not priority_queue.is_empty() else None

def generate_huffman_codes(root_node):
    """
    :param root_node:
    :return: root_tree (HuffmanNode)
    """
    codes = {}
    def _generate_codes_recursive(node, current_code):
        if node is None: return
        if node.char is not None:
            codes[node.char] = current_code if current_code else "0"
            return
        _generate_codes_recursive(node.left, current_code + "0")
        _generate_codes_recursive(node.right, current_code + "1")
    _generate_codes_recursive(root_node, "")
    return codes

# --- Encode Huffman ---
def encode_huffman(message, huffman_codes):
    """
    :param message: text message to encode
    :param huffman_codes: a tree of the huffman codes
    :return: encoded text message
    """
    encoded_message_parts = []
    for char in message:
        if char in huffman_codes:
            encoded_message_parts.append(huffman_codes[char])
        else:
            print(f"Error: Character '{char}' not found in Huffman codes. Cannot encode message.")
            return None
    return "".join(encoded_message_parts)

# --- Decode Huffman ---
def decode_huffman(encoded_data, root_node):
    """
    :param encoded_data: encoded text message
    :param root_node: root node of the Huffman codes
    :return: decoded text message
    """
    if root_node is None: return ""
    if root_node.left and not root_node.right and root_node.left.char is not None:
        single_char = root_node.left.char
        if any(bit != '0' for bit in encoded_data):
             print("Warning: Invalid bits found for single-character encoding.")
             return ""
        return single_char * len(encoded_data)

    decoded_string = ""
    current_node = root_node
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right
        else:
             print(f"Warning: Encountered invalid character '{bit}' in encoded data. Skipping.")
             continue
        if current_node is None:
            print("Error: Traversed to a non-existent node. Data might be corrupt.")
            return decoded_string
        if current_node.char is not None:
            decoded_string += current_node.char
            current_node = root_node
    if current_node != root_node:
        print("Warning: Encoded data finished mid-character traversal.")
    return decoded_string

def print_tree_preorder(root_node):
    """
    :param root_node: root node of the Huffman codes
    :return: None prints the tree in preorder traversal
    """
    print("\n--- Huffman Tree (Pre-order Traversal) ---")
    if root_node is None:
        print("Tree is empty.")
        print("--- End of Tree ---")
        return

    # Inner recursive function for traversal logic
    def _print_recursive(node, indent=""):
        """
        :param node:
        :param indent:
        :return: printed value of current node of tree
        """
        # Base case: If node is None, stop recursion for this path
        if node is None:
            return

        # 1. Visit the current node: Print its details
        print(f"{indent}Freq: {node.freq}", end="")
        if node.char is not None:
            # It's a leaf node, print the character
            print(f", Char: '{node.char}'")
        else:
            # It's an internal node
            print(" (Internal)")

        # 2. Recursively visit the left subtree
        _print_recursive(node.left, indent + "  ") # Increase indentation for children
        # 3. Recursively visit the right subtree
        _print_recursive(node.right, indent + "  ") # Increase indentation for children

    # Start the recursive printing process from the root node
    _print_recursive(root_node)
    print("--- End of Tree ---")