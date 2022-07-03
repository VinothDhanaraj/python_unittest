import unittest

print("Welcome, human.")
print("dir() is a function, returning a list.")
print("This has no output")
a_list = dir(unittest)
print("but this does", dir(unittest))
print("The help() command uses pydoc to print to stdout")
help(unittest)
print("This program is gratified to be of use.")