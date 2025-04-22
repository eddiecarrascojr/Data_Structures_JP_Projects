from lab3.lab3 import build_huffman_tree_custom_heap, print_tree_preorder, generate_huffman_codes,  encode_huffman, decode_huffman

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse

def read_frequency_table(filename):
    """
    :param filename: reads a frequency table file
    :return: a dictionary mapping characters to frequencies from the file
    """
    freq_table = {}
    with open(filename, 'r') as freq_file_read:
        for line in freq_file_read:
            line = line.lower()
            line = line.strip()
            line = line.replace(' ', '')
            letter = line[0]
            freq_letter = line[2:]
            freq_table[letter] = freq_letter
        return freq_table

def read_encoded_file(filename):
    """
    :param filename: file to read that is encoded
    :return: list of each line to encoded from file
    """
    list_to_read = []
    with open(filename, 'r') as freq_file_read:
        for line in freq_file_read:
            line = line.lower()
            line = line.strip()
            # line = line.replace(' ', '')
            line = line.replace('\n', '')
            list_to_read.append(line)

        return list_to_read

def read_clear_text_file(filename):
    """
    :param filename: file of text to encode
    :return: list of cleaned text with no punctuation marks.
    """
    list_to_read = []
    with open(filename, 'r') as freq_file_read:
        for line in freq_file_read:
            line = line.lower()
            line = line.strip()

            # Remove Punctuations
            line = line.replace('\n', '')
            line = line.replace('.', '')
            line = line.replace('?', '')
            line = line.replace('!', '')
            line = line.replace(' ', '')
            line = line.replace(',', '')
            list_to_read.append(line)

        return list_to_read

# Argument parser for help and input and output files
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("freq_table_path", type=str, help="Location of FreqTable.txt file.")
arg_parser.add_argument("encoded_file_path", type=str, help="Location of Encoded.txt Binary codes file.")
arg_parser.add_argument("clear_text_path", type=str, help="Location of ClearText.txt file.")

args = arg_parser.parse_args()

# create input and output file path handlers
freq_file = Path(args.freq_table_path)
encoded_file = Path(args.encoded_file_path)
decoded_file = Path(args.clear_text_path)

# 1. Define the Frequency Table, Decode Data and then Encode the Clear Text
if freq_file is None:
    freq_file = 'resources/inputs/ClearText.txt'
frequency_table = read_frequency_table(freq_file)

if encoded_file is None:
    encoded_file = 'resources/inputs/Encoded.txt'
encoded_data_ = read_encoded_file(encoded_file)

if decoded_file is None:
    decoded_file = 'resources/inputs/ClearText.txt'
decoded_data = read_clear_text_file(decoded_file)


print(f"Input Frequency Table: {frequency_table}")
print(f"Input Encoded file: {encoded_data_}")
print(f"Input ClearText Processed File: {decoded_data}")


# 2. Build the Huffman Tree using the CUSTOM HEAP function
root_tree = build_huffman_tree_custom_heap(frequency_table)
print(f"Printing the Preorder Traversal of Huffman Codes:{print_tree_preorder(root_tree)}")
if root_tree:
    print("\nHuffman Tree built successfully using custom heap.")
else:
    print("\nFailed to build Huffman Tree.")
    exit() # Exit if tree building failed

# 3. Generate Huffman Codes
huff_codes = generate_huffman_codes(root_tree)
print(f"\nGenerated Huffman Codes: {huff_codes}")


# 4. Define a Message to Encode
# Decode the string
print("\n--- Encoding the original message ---")
encoded_results = []
for message_to_encode in decoded_data:
    print(f"\nOriginal Message: {message_to_encode}")

    # 5. Encode the Message
    encoded_data_message = encode_huffman(message_to_encode, huff_codes)

    if encoded_data_message is not None:
        print(f"Encoded Data: {encoded_data_message}")

        # 6. Decode the Encoded Data
        decoded_text = decode_huffman(encoded_data_message, root_tree)
        print(f"Decoded Text: {decoded_text}")

        # 7. Verify that the input message is encoded then decoded to the original message.
        print(f"\nVerification (Original == Decoded): {message_to_encode == decoded_text}")
    else:
        print("\nEncoding failed.")

print("\n--- Decoding the original message from the file ---")
decoded_results = []
for message_to_decode in encoded_data_:
    print(f"\nOriginal Encoded Message: {message_to_decode}")

    # 5. Encode the Message
    decoded_data_message = decode_huffman(message_to_decode, root_tree)

    if decoded_data_message is not None:
        print(f"Encoded Data: {decoded_data_message}")

        # 6. Encoded Data
        encoded_text = encode_huffman(decoded_data_message, huff_codes)
        print(f"Encoded Text: {encoded_text}")

        # 7. Verify that the input message is encoded then decoded to the original message.
        print(f"\nVerification (Original == Decoded): {message_to_decode == encoded_text}")

    else:
        print("\nEncoding failed.")