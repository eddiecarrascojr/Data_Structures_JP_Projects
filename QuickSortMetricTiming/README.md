# Lab4: Quick Sort Partitioning

In this lab/module you will find python files that help run an **array** (Dad joke) of sorting comparisons of quick sort on diverse arrays.

Since quick sort is the fasted and easiest implementation of O(n log n). 

You can learn more about [quick sort algorithm from Wikipedia](https://en.wikipedia.org/wiki/Quicksort).

## Running Lab 4
Please Run these Steps in the correct order to produce and output.

1. Download and install Python on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m lab4 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m lab4 <some_input_file> <some_output_file>`
   a. IE: `python -m lab4 resources/input/in.txt output.txt`

Output will be written to the specified output file after processing the input file.

### Lab 4 Usage:

```commandline
usage: python -m lab4 [-h] File_Directory

positional arguments:
 TODO: Add arguements here

optional arguments:
  -h, --help  show this help message and exit
```

Usage statements are very formalized

| Symbol        | Meaning                                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------------------|
| [var]         | variable var is optional.                                                                                          |
| var           | variable var is required. All positional arguments are required.                                                   |
| -v, --version | This refers to a flag. One dash + one letter OR two dashes and a whole word. Some flags take one or more arguments |
| +             | This argument consumes 1 or more values                                                                            |
| *             | This argument consumes 0 or more values                                                                            |

## Lab 4 Packaging

To make code more portable, you need to package (especially in the real world) python modules. This is just a special
directory layout with a few optional files.

### Lab 4 Layout

Packages are groups of modules that work together to act as a library or program. Having a single module in a package is
fine, but you can (and plenty of times should) have more. Each module is made up of related python script(s). Here is our
605.202.lab4 example package explained.

* [lab4/](.): The parent or "root" folder containing all of these files. Can technically have any name.
    * [README.md](README.md):
      The guide you're reading. All software should come with a readme!
    * [lab4](lab4/): 
      This is a *module* in our *package*. Be sure to name it appropriately
      * [`__init__.py`](lab4/__init__.py) 
        helps create the module format for use of files within lab4.
      * [`__main__.py`](lab4/__main__.py) 
        This file is the entrypoint to the program, basically just reads in inputs.
      * `quick_sort.py` 
        python class of the quick sort function.
      * `runtime_metrics.py` 
        run time metrics to return the after sorting one of the files.
      * `partition.py`
        python partition class that helps to creat the divide and conquer scheme. 
      * `unit_test`.py`
        python partition class that helps to creat the divide and conquer scheme.
    * [inputs](resources/input/Lab4_Inputs): 

### Enhancements to lab 4
Below are the enhancements made to Lab 4
- Python Virtual Environment.
- Unit Tests.
- Statistics of Runtime Metrics.

### Python Virtual Environment
Run these commands to install the virtual environment. 


```python
from pathlib import Path
# Reminder, to import this way, there are more undocumented steps that require installing lab4 to the system libraries
import lab4

# open input file as read, output file as write
with Path('input.txt').open('r') as my_input_file, Path('output.txt').open('w') as my_output_file:
    lab4.process_files(my_input_file, my_output_file)
```

Additionally, this allows the end user to run your code from any directory, so long as they run it as a module. This is
done with the previously demonstrated m flag to python: `python -m <module>`.

```bash
# assuming lab4 has been installed to the python environment (Not documented here)
python -m lab4 input.txt output.txt
```

