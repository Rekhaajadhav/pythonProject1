# Task #11 -
# The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones,
# usually starting with 0 and 1
#
n = int(input("Enter the number of digits that you want in the Fibonacci sequence: "))
a = 0
b = 1
if n <= 0:
    print("INVALID INPUT")
else:
    print("Fibonacci sequence up to the given terms will be: ")
    print(a, b, end=" ")
    for x in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

