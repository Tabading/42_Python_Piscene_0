
import sys

if len(sys.argv) < 2:
	exit()
try:
	if len(sys.argv) > 2:
		raise AssertionError("AssertionError: more than one argument is provided")
	if sys.argv[1].isdigit() is False:
		raise AssertionError("AssertionError: argument is not an integer")
	if int(sys.argv[1]) % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")
except AssertionError as e:
	print(e)

