#Task #4


# Write a Python program to calculate the area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)
import math

radius=float(input("Enter the radius:"))

area=math.pi*radius**2

print(f"The area of the given circle with radius {radius} is : {area:.2f}")
