# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m proj0'. This file is NOT run during
# imports. This whole file is basically the java equivalent of:
# public static void main(string args[]), or c's int main();

# Generally used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse

from lab4.lab4 import process_data_files
from lab4.quicksort import Iterative_Quick_Sort

# Argument parser is an amazing tool. It's worth mastering
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
# arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

# pathlib.Path is also a fantastic built in tool and has a lot of great
# features. Please look it up! I promise it's worth it.
in_path = Path(args.in_file)
# out_path = Path(args.out_file)
in_path = 'resources/input/Lab4_Inputs/asc1K.dat'
retured_values = process_data_files(in_path, output_file=None)
result_arr, swap_count, comparison_count, run_time = Iterative_Quick_Sort(array=retured_values, low_index=0, high_index=len(retured_values)-1)
