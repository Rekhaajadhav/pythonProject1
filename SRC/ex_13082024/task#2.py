#Task #2
"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""

num1= int(input("Enter 1st Number:"))
num2= int(input("Enter 2nd number:"))

print(f"The maximum number between ({num1},{num2}) is " ,max(num1,num2))

print(f"The base {num1} raised to the power of exponent {num2} is {num1**num2}")

print(f"{num1} plus {num2} is {num1+num2} ")

print(f"{num1} minus {num2} is {num1 - num2} ")

print(f"{num1} multiplied by {num2} is {num1 * num2}")

print(f"{num1} divided by {num2} is {num1 / num2} ")

