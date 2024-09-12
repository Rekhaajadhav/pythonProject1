print("start")
try:
    a=int(input("Enter no1:"))
    b=int(input("Enter no2:"))
    c=a/b
except ZeroDivisionError as z:
    print(z)
    print("other than 0")
except ValueError as v:
    print(v)
    print("Enter integer value")

else:
    print(f"result=",{c})
finally:
    print("Thank you")