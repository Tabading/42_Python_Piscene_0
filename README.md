
enter venv
.venv\Scripts\Activate.ps1
check norm
python3 -m flake8 building.py 

# Exersises

## Ex00
Learn about collection data types and how to work with them:

**Lists**:		ordered and changeable. Allows duplicate members. \
**Tuple**:		ordered and unchangeable. Allows duplicate members. \
**Set**:		unordered, unchangeable(add/remove allowed), and unindexed. No duplicate members. \
**Dictionary**:	ordered(since 3.7) and changeable. No duplicate members. 

## Ex01
Learn about Unix time and formating strings and numbers

Unix time is a date and time representation widely used in computing. It measures time by the number of non-leap seconds that have elapsed since 00:00:00 UTC on 1 January 1970, the Unix epoch.

## Ex02
Learn about type checking, type hints (: type and -> type) and handling unknown input types

## Ex03
Learn how to identify and handle different null-like values in Python, such as None, NaN, 0, empty strings, and False.

## Ex04
Learn how to handle command-line arguments

## Ex05
Learn how to build a Python command-line program with a main(), handle arguments and user input, validate errors, and process strings character by character.

Method				| Reads					| Stops when		| Keeps \n?			| Ctrl+D behavior
----------------------|-----------------------|-------------------|-------------------|--------------------
input()				| One line				| Enter				| No				| Can raise EOFError
sys.stdin.readline()	| One line				| Enter or EOF		| Yes, if Enter		| Returns buffered text, or "" at EOF
sys.stdin.readlines()	| All remaining input	| EOF / Ctrl+D		| Yes				| Waits for EOF
sys.stdin.read()		| All remaining input	| EOF / Ctrl+D		| Yes				| Waits for EOF
fileinput.input()		| Lines from files/stdin| Each line / EOF	| Yes				| Similar to readline() for stdin

## Ex06
Learn how use list comprehensions, use lambda functions, validate command-line arguments, and process/filter data based on conditions.

**List comprehension**:	offers a shorter syntax when you want to create a new list based on the values of an existing list. \
**Lambda**:				a small, unnamed function that takes input and immediately returns a result. commonly used with built-in functions like map(), filter(), and sorted().

## Ex07
Learned how to use a dictionary, loops, string manipulation, and input validation to convert a string into Morse code.

## Ex08
Learned how to use generators with yield, terminal control, and dynamic string formatting to create a progress bar similar to tqdm.

**enumerate(iterable, start)**: enumerate takes a collection (e.g. a list) and returns it as an enumerate object. \
**enumerate object**: adds a counter as the key of the enumerate object, start dictates where counting starts. \
ex: 

	x = ('apple', 'banana', 'cherry') 
	print(enumerate(x))
	-> [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

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

norm:
- https://www.geeksforgeeks.org/python/python-docstrings/

ex05:
- https://realpython.com/python-main-function/
- KI for finding string methods

ex06:
- https://www.w3schools.com/python/python_strings_modify.asp
- https://www.w3schools.com/python/ref_func_filter.asp
- https://www.w3schools.com/python/python_lists_comprehension.asp
- https://www.w3schools.com/python/python_lambda.asp

ex07:
- https://www.w3schools.com/python/python_strings_methods.asp
- https://www.w3schools.com/python/python_for_loops.asp
- https://www.w3schools.com/python/python_dictionaries.asp

ex08:
- https://www.w3schools.com/python/ref_keyword_yield.asp
- https://www.w3schools.com/python/ref_func_enumerate.asp
- KI for finding enumerate, f-string options, percentage math

## KI Usage
KI was generally used to save time searching for specific functions, explaining specifics and finding shorter solutions, ie. how MY code could be reformated to be shorter/less lines for learning purposes.