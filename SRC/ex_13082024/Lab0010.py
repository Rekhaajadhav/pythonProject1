# The format() method insert values into a string with placeholders ({}).It is just replacement of value
# Using F-Strings (Python 3.6+)
# F-strings is used to format strings, using curly braces {} directly in the string.
# Formatting Numbers:
# format numbers to control the number of decimal places

value = 1234.5678
formatted_string = f"{value:.2f}"
print(formatted_string)

# List [] - contain items of different data types,we can change the content of a list
shoppling_list=["apples","butter","cheese"] #list of string
# A list of integers
numbers = [1, 2, 3, 4, 5]

# A mixed list
mixed = ["Rekha",26,"C","Python",-32,09.45]

# string functions

name = "Rekha"
print(name.upper())
print(name.lower())
print(len(name))
print(name.capitalize())
print(name.index("k"))

# none (noneType)

# Indicating Absence of a Value it means a variable does not currently hold a meaningful value.
print(type(None))  # Output: <class 'NoneType'>

# id() is the identity of an object. it returns the memory address of the object.
a = 10
b = 10

print(id(a))  # Output: unique id (memory address) for 10
print(id(b))  # Output: same id as a because integers are immutable and Python reuses the same object
