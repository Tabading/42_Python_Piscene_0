*This project has been created as part of the 42 advanced curriculum by tabading.*

# Table of Contents
- [Description](#description)
    - [Project Specifications](#project-specifications)
    - [Mandetory Modules](#mandetory-modules)
        - [Ex00](#ex00)
        - [Ex01](#ex01)
        - [Ex02](#ex02)
        - [Ex03](#ex03)
        - [Ex04](#ex04)
    - [Bonus Modules](#bonus-modules)
        - [Ex05](#ex05)
        - [Ex06](#ex06)
        - [Ex07](#ex07)
        - [Ex08](#ex08)
        - [Ex09](#ex09)
- [Instructions](#instructions)
    - [Compilation](#compilation)
    - [Norm](#norm)
- [Resources](#resources)
    - [KI Usage](#ki-usage)

# Description
*Training Piscine Python for Data Science - 0* is the first of 5 Projects serving as an intoduction to Python. It encompasses 10 Modules, 7 of which are mandetory.

### Project Specifications
After Project 5, these additional Rules must be followed:
- No code in the global scope. Use functions!
- Each program must have its main and not be a simple script: 

        def main():
            # your tests and your error handling

        if __name__ == "__main__":
            main()

- Any exception not caught will invalidate the exercises, even in the event of an error
that you were asked to test.
- All your functions must have documentation (\_\_doc\_\_)
- Your code must follow the norm
    - pip install flake8

## Mandetory Modules

### Ex00
Learn about collection data types and how to work with them:

**Lists**:		ordered and changeable. Allows duplicate members. \
**Tuple**:		ordered and unchangeable. Allows duplicate members. \
**Set**:		unordered, unchangeable(add/remove allowed), and unindexed. No duplicate members. \
**Dictionary**:	ordered(since 3.7) and changeable. No duplicate members. 

### Ex01
Learn about Unix time and formating strings and numbers

***Unix time*** is a date and time representation widely used in computing. It measures time by the number of non-leap seconds that have elapsed since 00:00:00 UTC on 1 January 1970, the Unix epoch.

### Ex02
Learn about type checking, type hints and handling unknown input types

***type(object)***: gives a string coresponding to the object Type, eg. "List".\
***Type hints*** are a feature in Python that allow developers to annotate their code with expected types for variables and function arguments. This helps to improve code readability and provides an opportunity to catch errors before runtime. \
For example:
- variable: age: int = 24
- function: def hello(greet: str):
- return: def hello() -> int:

### Ex03
Learn how to identify and handle different null-like values in Python, such as None, NaN, 0, empty strings, and False.

### Ex04
Learn how to handle command-line arguments

## Bonus Modules

### Ex05
Learn how to build a Python command-line program with a main(), handle arguments and user input, validate errors, and process strings character by character.

Method				| Reads					| Stops when		| Keeps \n?			| Ctrl+D behavior
----------------------|-----------------------|-------------------|-------------------|--------------------
input()				| One line				| Enter				| No				| Can raise EOFError
sys.stdin.readline()	| One line				| Enter or EOF		| Yes, if Enter		| Returns buffered text, or "" at EOF
sys.stdin.readlines()	| All remaining input	| EOF / Ctrl+D		| Yes				| Waits for EOF
sys.stdin.read()		| All remaining input	| EOF / Ctrl+D		| Yes				| Waits for EOF
fileinput.input()		| Lines from files/stdin| Each line / EOF	| Yes				| Similar to readline() for stdin

### Ex06
Learn how use list comprehensions, use lambda functions, validate command-line arguments, and process/filter data based on conditions.

**List comprehension**:	offers a shorter syntax when you want to create a new list based on the values of an existing list. \
**Lambda**:				a small, unnamed function that takes input and immediately returns a result. commonly used with built-in functions like map(), filter(), and sorted().

### Ex07
Learned how to use a dictionary, loops, string manipulation, and input validation to convert a string into Morse code.

### Ex08
Learned how to use generators with yield, terminal control, and dynamic string formatting to create a progress bar similar to tqdm.

**enumerate(iterable, start)**: enumerate takes a collection (e.g. a list) and returns it as an enumerate object. \
**enumerate object**: adds a counter as the key of the enumerate object, start dictates where counting starts. \
ex: 

	x = ('apple', 'banana', 'cherry') 
	print(enumerate(x))
	-> [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

### Ex09
Learned how to create my own Package.

Python packages are a way to organize and structure code by grouping related modules into directories. 
- A package is essentially a folder that contains an \_\_init\_\_.py file and one or more Python files (modules).
- Allows modules to be easily shared and distributed across different applications. 

#### Key Components of a Python Package

- **Module**: A single Python file containing reusable code (e.g., math.py).
- **Package**: A directory containing modules and a special \_\_init\_\_.py file.
- **Sub-Packages**: Packages nested within other packages for deeper organization.

# Instructions

### Compilation

    python3 *.py

for ex09 look at [How to Test](ex09/README.md#how-to-test)

### Norm 

    python3 -m flake8 *.py


# Resources
ex00:
- https://www.w3schools.com/python/python_lists.asp
- https://www.w3schools.com/python/python_tuples.asp
- https://www.w3schools.com/python/python_sets.asp
- https://www.w3schools.com/python/python_dictionaries.asp

ex01:
- https://www.w3schools.com/python/ref_module_time.asp
- https://www.w3schools.com/python/python_datetime.asp
- https://alexwlchan.net/notes/2025/python-comma-n/

ex02:
- https://www.geeksforgeeks.org/python/how-to-check-the-type-of-an-object-in-python/
- https://www.geeksforgeeks.org/python/type-hints-in-python/

ex03:
- https://www.geeksforgeeks.org/python/null-in-python/
- https://www.geeksforgeeks.org/python/check-for-nan-values-in-python/

ex04:
- https://www.w3schools.com/python/ref_module_sys.asp
- https://www.w3schools.com/python/ref_exception_assertionerror.asp

norm:
- https://www.geeksforgeeks.org/python/python-docstrings/

ex05:
- https://realpython.com/python-main-function/
- https://www.w3schools.com/python/python_ref_string.asp
- https://www.geeksforgeeks.org/python/take-input-from-stdin-in-python/

ex06:
- https://www.w3schools.com/python/python_strings_modify.asp
- https://www.w3schools.com/python/ref_func_filter.asp
- https://docs.python.org/3/library/functions.html#filter
- https://www.w3schools.com/python/python_lists_comprehension.asp
- https://www.w3schools.com/python/python_lambda.asp
- https://www.w3schools.com/python/python_arguments.asp

ex07:
- https://www.w3schools.com/python/python_strings_methods.asp
- https://www.w3schools.com/python/python_for_loops.asp
- https://www.w3schools.com/python/python_dictionaries.asp

ex08:
- https://www.w3schools.com/python/ref_keyword_yield.asp
- https://www.w3schools.com/python/ref_func_enumerate.asp
- KI for finding enumerate, f-string options, percentage math

ex09:
- https://www.geeksforgeeks.org/python/python-packages/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/

### KI Usage
KI was generally used to save time searching for specific functions, explaining specifics, figuring out what what i'm trying to do is called and finding shorter solutions, ie. how MY code could be reformated to be shorter/less lines for learning purposes.