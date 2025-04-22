# Lab 2
**by Eduardo Carrasco**

**email: ecarras6@jh.edu**
# Run program
python -m unittest test_prefix_to_postfix.py
## Installing Python Virtual Environment
1) `cd` into lab2/Scripts
2) Then activate the environment by running 
    - **Mac** or **Linux** using `source lab2/Scripts/activate`
    - `source lab2/Scripts/Activate.ps1`  if you are on **Windows**
    - Also may work if your **Windows** path for python is working by running `source lab2/Scripts/activate`
3) Then install the requirements.txt by running `pip install requirements.txt`
## Preface
This is module for Lab 2 for converting Prefix inputs to Postfix output using a stack Abstract Data Structure & Recursion.

This lab2 README.md also includes instructions on how to run it in your python environment.

## Motivation for Prefix to Postfix conversion
Humans can read Infix which is how we read mathmatics. 
Example: A+B is simple for us to read but difficult for computer to understand. Hence, why we use Prefix and Postfix.
The goal of this Lab2 is to convert Prefix to Postfix because for some programs only run in Prefix (such as LISP). 
Other programming languages only use Postfix and many old calculators (such as HP calculator) also only use Postfix. [Source](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

## Running Lab 1
##### Before running it should be noted that the values in the input.txt file must be values. If they are numerical numbers it will return the numerical string of the numbers. *Please see in.txt as example input and out.txt for output.*
1. Download and install Python on your computer. Python 3.12 or higher is required.
2. Navigate to [this](.) directory (containing the README.md). The Root Directory. 
3. Run the program as a module: `python -m lab2 -h`. This will print the help message:
   - `positional arguments: in_file Input File Pathname or directory. out_file Output File Pathname or directory.`
   
4. Run the program as a module (with real inputs): `python -m lab2 <some_input_file> <some_output_file>`
   a. IE: `python -m lab2 "resources/input/in.txt" "resources/output/out.txt"`
5. It will then print out the full path of where the output_file was created to.

Output will be written to the specified output file after processing the input file. 

### Lab 1 Usage:

```commandline
usage: python -m lab2 [-h] in_file out_file prefix_bool_flag

positional arguments:
    in_file                 Input File Pathname or directory path
    out_file                Output File Pathname or directory path
    prefix_bool_flag        Prefix to postfix conversion boolean flag. If True Prefix else Postfix conversion

```

```commandline
usage: python -m lab2 "resources/inputs/in.txt" "resources/output/out.txt" "True"

    File was created with the output in the following location: 'resources/output/out.txt'.

```
#### View the input and output files in resources to get an idea of what is to be expected as input and output.

Usage statements are very formalized

| Symbol        | Meaning                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |



## Project Lab 2 Layout

Packages are groups of modules that work together to act as a library or program. Having a single module in a package is
fine, but you can (and plenty of times should) have more. Each module is made up of related python script(s). Here is our
605.202.proj0 example package explained.

* [ECarrascoLab2/](.): The parent or "root" folder containing all of these files. 
    * [README.md](README.md):
      The guide you're reading. It explains how to use, example of how to run the project, and documentation of lab 1.
    * [lab2](lab2): 
      This is a *module* for *lab2*. Prefix to Postfix Conversion using a stack.
      * [`__init__.py`](lab2/__init__.py) 
        Initialization of the lab2 module. It exports the needs function code used to run lab2. 
      * [`__main__.py`](lab2/__main__.py) 
        This file is the entrypoint to the program. It usually just handles command line arguments, for the python program.
      * [`prefix_to_postfix.py`](lab2/prefix_to_postfix.py) 
        This is the Abstract Data Type for a stack for implementing a prefix to postfix conversion. 
      * [`postfix_to_prefix.py`](lab2/prefix_to_postfix.py) 
        This is the Abstract Data Type for a stack for implementing a postfix to prefix conversion.
      * [`lab2.py`](lab2/lab2.py) 
      This is the file that runs everything together to convert the input.txt from prefix to output.txt to postfix or vise versa if postfix is used. 
      * [`Scripts/`](lab2/Scripts) (*optional*)
        This directory contains the virtual environment files and requirement file to test the module.

    * [resources](resources):
      * [inputs](resources/inputs): All the input files will reside in this folder to keep things organized.
        * [`in.txt`]: This file is a sample input of Prefix, and it will be output into Postfix format.
        * [`prefix.txt`]: Prefix, and it will be output into Postfix format.
      * [output](resources/outputs): All the output files will reside in this folder to keep things organized.
        * [`out.txt`]: This is a sample of output text converted from Prefix to Postfix.
        * [`postfix.txt`]: Postfix example output to test in prefix conversion.
    
### Examples for Inputs arguments
These lines below are examples of what to expect from input and output for the given values.
Valid inputs
- input:-+ABC  
  - outputs: AB+C-
- input:$+-ABC+D-EF  
  - outputs: AB-C+DEF-+$
  
Invalid inputs
- input:/A+BC +C*BA  
  - output: ABC+/.

- input: *$A^BC+C-BA 
  - output: A^$B*
    
### Python Packages

- *typing* uses **TextIO** object
- *pathlib* uses *Path* 
- *argparse*

```python 
python -m lab2 "<input_file_location>" "<output_file_location>" "<prefix_bool_flag=True>"
```

Additionally, this allows the end user to run your code from any directory, so long as they run it as a module. This is
done with the previously demonstrated m flag to python: `python -m <module>`.

### Example Run
```bash
# assuming lab2 has been installed to the python environment (Not documented here). If not you can create a separate python module file to run. (Note: not shown in documentation.)
python -m lab2 resources/inputs/in.txt resources/outputs/out.txt True
```

### Running Unit Testing
```bash
# how to run the unit test
python -m lab2/unit_test.py
```

### Run Virtual Environment
```bash
# how to run the unit test
source lab2/Scripts/activate
pip install lab2/Scripts/requirements.txt
```