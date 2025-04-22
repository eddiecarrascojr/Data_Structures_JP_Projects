# This file is used to help expose what functions, classes, etc are available
# to other scripts when the module is imported.

# This python script will run EVERY TIME the module is imported and can contain
# any code you desire

# Here we're very simply making it easier for other scripts to access the
# process_files function. Note: other scripts and functions are still
# accessible
from lab2.lab2 import process_file
from lab2.prefix_to_postfix import PrefixToPostfix
from lab2.postfix_to_prefix import PostfixToPrefix