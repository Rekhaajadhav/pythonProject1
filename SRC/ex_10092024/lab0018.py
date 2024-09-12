import os

try:

    path=r'C:\Users\HP\PycharmProjects\pythonProject1\SRC\ex_29082024\lab0014.py'
    print(path)
    a=open(path,'r')
    for i in a:
        print(i)
except FileNotFoundError as f:
    print(f)
    print("Please enter valid path or correct file name:")
finally:
    try:
        a.close()
    except Exception as e:
        print(e)
        print("file not foumd")