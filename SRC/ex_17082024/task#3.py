### Task #3


# Explain the difference between the = operator and the == operator in Python.

# The = operator is used for assignment, such as when assigning a value to a variable.
# The == operator is the relational operator for checking equality of two values.

# What does the ** operator do in Python, and how is it used?

#  ** is the exponentiation operator.
#  This operator raises the left operand (base) to the power of the right operand (exponent)
#  (a**b)
a = 2
b = 3
print(f"2 power 3 is ", a ** b)

# What does the ^ operator do in Python, and in what context is it commonly used?
# The ^ operator does a binary xor. a ^ b will return a value with only the bits set in a or in b but not both
# It is exclusive OR operator. If the bits are different, it returns 1; otherwise, it returns 0.
# Take two bit values a and b, where a = 7= (111)2 and b = 4 = (100)2 . Take Bitwise and of both a & b
# 111 ^ 100 =011(3)
a = 7
b = 4

# print bitwis XOR operation
print("a ^ b =", a ^ b)



