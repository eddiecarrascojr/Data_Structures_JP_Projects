from typing import TextIO

from lab2.prefix_to_postfix import PrefixToPostfix
from lab2.postfix_to_prefix import PostfixToPrefix

def split_line(text_line) -> list:
    """
    :param text_line: a single line of text
    :return: returns a list of each character separated by a newline
    """
    s = []
    for char in text_line:
        s.append(char)
    return s

def read_lines(filename) -> TextIO:
    """
    :param filename: the name of the file being read in this case the input/in.txt
    :return: return a read object to be used line by line.
    """
    file_read = open(filename, 'r')
    return file_read

def convert_prefix_to_postfix(prefix_str) -> PrefixToPostfix:
    """"
    :param prefix_str: a single line of text that is in prefix format to postfix.
    :return: a PreFixToPostfixStack list object ready to be used in postfix conversion.
    """
    # Special Operators to look out for in the read line


    prefix_postfix_obj = PrefixToPostfix()
    value = prefix_postfix_obj.convert(prefix_str)
    return value

def convert_postfix_to_prefix(postfix_str) -> PostfixToPrefix:
    """"
    :param postfix_str: a single line of text that is in postfix format to prefix.
    :return: a PostfixToPrefix list object ready to be used in prefix conversion.
    """
    postfix_obj = PostfixToPrefix()
    value = postfix_obj.convert(postfix_str)

    return value

def process_file(file_path_input: TextIO, file_path_output: TextIO, prefix=True) -> None:
    """
    :param file_path_input: gives the directory for the input file
    :param file_path_output: give the directory for the output file
    :param prefix: boolean if prefix should be converted to postfix if not visa versa.
    :return: None but writes the output to file of the Prefix to Postfix stack
    """

    if prefix:
        print("Converting prefix expression to postfix expression.")
        # Covert input file to read object
        file_r = read_lines(file_path_input)

        # Open the output file location.
        file_output = open(file_path_output, 'w')

        for line in file_r:
            postfix_value = convert_prefix_to_postfix(line)
            string_value = str(postfix_value)

            # Output the line in the out.txt file
            file_output.write(string_value)
            file_output.write('\n')
        # Close file and write new character.
        file_output.write("\n")
    else:
        print("Converting postfix expression to prefix expression.")
        file_r = read_lines(file_path_input)

        # Open the output file location.
        file_output = open(file_path_output, 'w')

        for line in file_r:
            postfix_value = convert_postfix_to_prefix(line)
            string_value = str(postfix_value)
            # Output the line in the out.txt file
            file_output.write(string_value)
            file_output.write('\n')
        # Close file and write new character.
        file_output.write("\n")