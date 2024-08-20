# Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

length1 = int(input("Enter length of 1st side:"))
length2 = int(input("Enter length of 2nd side:"))
length3 = int(input("Enter length of 3rd side:"))

if length1 == length2 == length3:
    print(f"This is equilateral triangle with {length1},{length2},{length3}")


elif length1 == length2 or length1 == length3 or length2 == length3:
    print(f"This is Isosceles triangle with {length1},{length2},{length3}")

else :
    print(f"This is scalene triangle with {length1},{length2},{length3}")

