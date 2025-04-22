# This file is the entry point for lab1 module.


# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
import os

from lab2 import *

# Argument parser for help and input and output files
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname or directory.")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname or directory.")
arg_parser.add_argument("prefix_bool", type=str, help="True if prefix conversion, False if post conversion.")

args = arg_parser.parse_args()

# create input and output file path handlers
in_path = Path(args.in_file)
out_path = Path(args.out_file)
prefix_bool = Path(args.prefix_bool)

process_file(in_path, out_path, prefix_bool)
cwd = os.getcwd()
print(f"File was created with the output in the following location: '{cwd}/{out_path}'.")
