# Dynamically typed

# At the run time, data of the variable can be changed. and you don't need to
# mention the data type

# debug
# click on line number (basically make it red )
# click on debug button near run button


x = 56
print(type(x))
x = "Dynamic Type"
print(x)
print(type(x))

a = 10
b = 10
c = 10
sum = a + b + c
sum = sum - 11
sum = sum + 1
sum = sum + 1
print(sum)

x, y, z = 76, 34, 23
print(x, y, z, sep=",")
