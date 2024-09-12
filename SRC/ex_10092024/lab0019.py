bal=1000
wtdrw=int(input("Enter withdraw amount:"))
class ex(Exception):
    def __init__(self,m):
        self.m=m
        super().__init__(m)

    pass


if bal>wtdrw:
    print("please collect amount",wtdrw,"\nBalance=",bal-wtdrw)
else:
    raise ex("Balance IS LOW!!!")
